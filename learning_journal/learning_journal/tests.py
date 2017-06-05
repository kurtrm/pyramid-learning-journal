"""Test our app."""
from pyramid import testing
import pytest
import transaction
from learning_journal.models import (
    Entry,
    get_tm_session,
)
from learning_journal.models.meta import Base

SITE_ROOT = 'http://localhost'


@pytest.fixture(scope='session')
def configuration(request):
    config = testing.setUp(settings={
        'sqlalchemy.url': 'postgres://kurtrm:hofbrau@localhost:5432/test_journal'
    })
    config.include("learning_journal.models")
    config.include("learning_journal.routes")

    def teardown():
        testing.tearDown()

    request.addfinalizer(teardown)
    return config


@pytest.fixture
def db_session(configuration, request):
    SessionFactory = configuration.registry["dbsession_factory"]
    session = SessionFactory()
    engine = session.bind
    Base.metadata.create_all(engine)

    def teardown():
        session.transaction.rollback()
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)
    return session


@pytest.fixture
def dummy_request(db_session):
    from pyramid import testing
    req = testing.DummyRequest()
    req.dbsession = db_session
    return req


@pytest.fixture
def post_request(dummy_request):
    dummy_request.method = 'POST'
    return dummy_request


def test_create_view_post_empty_dict(post_request):
    """Create view returns a reponse object."""
    from learning_journal.views.default import new_entry
    response = new_entry(post_request)
    assert response == {}


def test_create_view_post_returns_error(post_request):
    """Create view returns error."""
    from learning_journal.views.default import new_entry
    data = {
        'title': '',
        'price': ''
    }
    post_request.POST = data
    response = new_entry(post_request)
    assert 'error' in response


def test_create_view_post_incomplete_ok(post_request):
    """New entry will take empty fields and be fine."""
    from learning_journal.views.default import new_entry
    data = {
        'title': 'Testing 1-2-3',
        'body': ''
    }
    post_request.POST = data
    response = new_entry(post_request)
    assert 'title' in response
    assert 'body' in response
    assert response['title'] == 'Testing 1-2-3'
    assert response['body'] == ''


def test_create_view_redirects_after_post(post_request):
    """Ensure it puts us back on the homepage when done."""
    from learning_journal.views.default import new_entry
    from pyramid.httpexceptions import HTTPFound
    data = {
        'title': 'Testing 1-2-3',
        'body': 'This is a test of the database.',
        'creation_date': ''
    }
    post_request.POST = data
    response = new_entry(post_request)
    assert response.status_code == 302
    assert isinstance(response, HTTPFound)


#  ====== Functional Tests ======

@pytest.fixture(scope='session')
def testapp(request):
    from webtest import TestApp
    from pyramid.config import Configurator

    def main(global_config, **settings):
        settings['sqlalchemy.url'] = 'postgres://kurtrm:hofbrau@localhost:5432/learning_journal'
        config = Configurator(settings=settings)
        config.include('pyramid_jinja2')
        config.include('.models')
        config.include('.routes')
        config.scan()
        return config.make_wsgi_app()

    app = main({})
    testapp = TestApp(app)

    SessionFactory = app.registry['dbsession_factory']
    engine = SessionFactory().bind
    Base.metadata.create_all(bind=engine)

    def tearDown():
        Base.metadata.drop_all(bind=engine)

    request.addfinalizer(tearDown)

    return testapp


def test_new_entry_redirects_to_home(testapp):
    data = {
        'title': 'Testing 1-2-3',
        'body': 'This is a test of the database.',
        'creation_date': ''
    }
    response = testapp.post('/journal/new-entry', data)
    assert response.location == SITE_ROOT + '/'


def test_new_entry_redirects_and_shows_html(testapp):
    data = {
        'title': 'Testing 1-2-3',
        'body': 'This is a test of the database.',
        'creation_date': ''
    }
    response = testapp.post('/journal/new-entry', data).follow()
    assert "<h1>Testing 1-2-3</h1>" in response.text

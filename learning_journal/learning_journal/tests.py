"""Test our app."""
from pyramid import testing
from pyramid.httpexceptions import HTTPNotFound
from learning_journal.data.entries import ENTRIES
import pytest
import os


HERE = os.path.dirname(__file__)


@pytest.fixture
def home_response():
    """Return a response from the home page."""
    from learning_journal.views.default import list_view
    req = testing.DummyRequest()
    response = list_view(req)
    return response


@pytest.fixture
def detail_response():
    """Return a single item from the ENTRIES dict for testing."""
    from learning_journal.views.default import detail_view
    req = testing.DummyRequest()
    req.matchdict['id'] = '1'
    response = detail_view(req)
    return response


def test_home_view_returns_proper_content(home_response):
    """Home view returns a reponse object."""
    assert 'title' in home_response
    assert 'entries' in home_response
    assert home_response['entries'] == ENTRIES


def test_detail_view_returns_one_response(detail_response):
    """Test detail view has one entry on it."""
    assert detail_response['entries'] == ENTRIES[1]


def test_detail_view_returns_bad():
    """Test that we get a 404 if id is bad."""
    from learning_journal.views.default import detail_view
    req = testing.DummyRequest()
    req.matchdict['id'] = '70'
    with pytest.raises(HTTPNotFound):
        detail_view(req)


@pytest.fixture
def testapp():
    """Create a test application."""
    from learning_journal import main
    from webtest import TestApp
    app = main({})
    return TestApp(app)


def test_home_route_returns_home_content(testapp):
    """Test that we get the list_view content."""
    response = testapp.get('/')
    html = response.html
    assert 'Kurt\'s Public Journal' in str(html.find('h1').text)
    assert 'May 15, 2017' in str(html.find('h6').text)


def test_list_view_has_all_entries(testapp):
    """Test that we get all the entries back."""
    response = testapp.get('/')
    html = response.html
    assert len(ENTRIES) == len(html.find_all('h6'))


def test_detail_route_has_the_correct_content(testapp):
    """Ensure detail routes return the correct entry."""
    response = testapp.get('/journal/3', status=200)
    html = response.html
    assert 'May 18, 2017' in html.find_all('h1')[1]

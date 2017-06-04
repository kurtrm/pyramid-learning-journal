"""Test our learning journal application."""
from pyramid import testing
from pyramid.response import Response
import pytest


@pytest.fixture
def request():
    """Request object for testing."""
    request = testing.DummyRequest()
    return request


def test_list_view_returns_response(request):
    """Ensure list_view returns a Response object."""
    from learning_journal.views.default import list_view
    response = list_view(request)
    assert isinstance(response, Response)


def test_list_view_checks_out(request):
    """Ensure list view returns a 200 OK response."""
    from learning_journal.views.default import list_view
    response = list_view(request)
    assert response.status_code == 200


def test_list_view_returns_content(request):
    """Ensure response has proper content."""
    from learning_journal.views.default import list_view
    response = list_view(request)
    assert 'The Bootstrap Blog' in response.text


def test_detail_view_returns_ok(request):
    """Ensure response from detail view has 200 OK."""
    from learning_journal.views.default import detail_view
    response = detail_view(request)
    assert response.status_code == 200


def test_detail_view_has_a_link_home(request):
    """Ain't much content on this page, it only has a link home."""
    from learning_journal.views.default import detail_view
    response = detail_view(request)
    assert '<button><a href="/">Home</a></button>' in response.text

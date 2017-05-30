from pyramid.response import Response
import os
import io


HERE = os.path.dirname(__file__)


def list_view(request):
    """List of journal entries."""
    with io.open(os.path.join(HERE, '../scripts/index.html')) as file:
        imported_html = file.read()
    #import pdb; pdb.set_trace()
    return Response(imported_html)


def detail_view(request):
    """Single journal entry."""
    with io.open(os.path.join(HERE, '../scripts/detail.html')) as file:
        imported_html = file.read()
    return Response(imported_html)


def create_view(request):
    """Create new view."""
    with io.open(os.path.join(HERE, '../scripts/new_entry.html')) as file:
        imported_html = file.read()
    return Response(imported_html)


def update_view(request):
    """Update existing view."""
    with io.open(os.path.join(HERE, '../scripts/edit.html')) as file:
        imported_html = file.read()
    return Response(imported_html)

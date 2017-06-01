from pyramid.view import view_config
from learning_journal.data.entries import ENTRIES
from pyramid.httpexceptions import HTTPNotFound
from learning_journal.models.entries import Entry


@view_config(
    route_name="list_view",
    renderer='../templates/index.jinja2'
)
def list_view(request):
    """List of journal entries."""
    entries = request.dbsession.query(Entry).all()
    return {
        'title': 'Main',
        'entries': entries
    }


@view_config(
    route_name="detail_view",
    renderer='../templates/detail.jinja2'
)
def detail_view(request):
    """Single journal entry."""
    entry_id = int(request.matchdict['id'])
    entry = request.dbsession.query(Entry).get(entry_id)
    if entry:
        return {
            'id': entry.id,
            'title': entry.title,
            'body': entry.body,
            'creation_date': entry.creation_date
        }
    else:
        raise HTTPNotFound

@view_config(
    route_name="create_view",
    renderer='../templates/new_entry.jinja2'
)
def create_view(request):
    """Create new view."""
    return {}


# @view_config(
#     route_name="update_view",
#     renderer='../templates/edit.jinja2'
# )
# def update_view(request):
#     """Update existing view."""
#     return {}

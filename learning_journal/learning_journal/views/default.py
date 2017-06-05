from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from learning_journal.models.entries import Entry
import datetime


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
            'entry_id': entry.id,
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
    """Create new entry."""
    if request.method == "POST" and request.POST:
        if not request.POST['title'] or not request.POST['body']:
            return {
                'title': request.POST['title'],
                'body': request.POST['body'],
                'error': 'Please provide a title and/or body.'
            }
        new_entry = Entry(
            title=request.POST['title'],
            body=request.POST['body'],
            creation_date=datetime.datetime.now()
        )
        request.dbsession.add(new_entry)
        return HTTPFound(
            location=request.route_url('list_view')
        )
    return {}


@view_config(
    route_name="update_view",
    renderer='../templates/edit.jinja2'
)
def update_view(request):
    """Update existing journal entry."""
    the_id = int(request.matchdict['id'])
    session = request.dbsession
    entry = session.query(Entry).get(the_id)
    if not entry:
        raise HTTPNotFound
    if request.method == 'GET':
        return {
            'page': 'Edit Entry',
            'title': entry.title,
            'body': entry.body,
        }
    if request.method == "POST":
        entry.title = request.POST['title']
        entry.body = request.POST['body']
        request.dbsession.flush()
        return HTTPFound(request.route_url('detail_view', id=entry.id))

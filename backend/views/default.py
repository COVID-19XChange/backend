import requests
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.threadlocal import get_current_registry


from sqlalchemy.exc import DBAPIError

from ..models import MyModel


@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def my_view(request):
    try:
        query = request.dbsession.query(MyModel)
        one = query.filter(MyModel.name == 'one').first()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'one': one, 'project': 'backend'}


@view_config(route_name='maps')
def my_maps(_):
    settings = get_current_registry().settings
    googlemaps_api_key = settings.get('googlemaps.api_key')
    googlemaps_api_uri = 'https://www.google.com/maps/embed/v1/view'
    params = {
        'zoom': 11,
        'center': '45.4642,9.1900',
        'key': googlemaps_api_key
    }

    req = requests.Request('GET', googlemaps_api_uri, params=params).prepare()

    response_html = '<iframe width="600" height="450" frameborder="0" style="border:0" ' \
        'src="' + req.url + '" allowfullscreen></iframe>'

    return Response(response_html)


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_backend_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

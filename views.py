from pyramid.response import Response
from pyramid.httpexceptions import HTTPOk
from pyramid.view import view_config, view_defaults
import db
import uuid
from pyramid.config import Configurator


@view_config(route_name = 'viewComponents', request_method='GET', renderer='json')
def view_components(context,request):
    print('Incoming request')
    request.session['id'] = uuid.uuid1()
    print 'This is the session id!', request.session['id']
    db.connectToDb()
    print db.dictionary
    return (db.dictionary)

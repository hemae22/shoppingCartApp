from pyramid.response import Response
from pyramid.httpexceptions import HTTPOk
from pyramid.view import view_config, view_defaults
import db
import uuid

from pyramid.config import Configurator


@view_config(route_name = 'viewComponents', request_method='GET', renderer='json')
def view_components(context,request):
    print('Incoming request')
    #my_session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
    #config = Configurator(session_factory = my_session_factory)
    request.session['id'] = uuid.uuid1()
    print session['id']
    #session = Request.session
    #session['id'] = uuid.uuid1()
    db.connectToDb()
    print db.dictionary
    return (db.dictionary)

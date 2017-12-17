from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.httpexceptions import HTTPOk
from pyramid.view import view_config, view_defaults
#from pyramid.session import SignedCookieSessionFactory
from pyramid.session import SignedCookieSessionFactory
import db
import uuid
import views


#@view_config(request_method='GET', renderer='json')
#def view_components(context,request):
    #print('Incoming request')
    #session = Request.session
    #session['id'] = uuid.uuid1()
    #db.connectToDb()
    #print db.dictionary
    #return (db.dictionary)
    #return Response('<body>hello</body>')


if __name__ == '__main__':
    my_session_factory = SignedCookieSessionFactory('itsaseekreet')
    config = Configurator(settings=settings, session_factory=my_session_factory)
    config.include('pyramid_chameleon')
    #config = Configurator()
    #config.include('views')
    #confg.add_route('viewComponents', '/viewComponents')
    #config = Configurator()
    #my_session_factory = SignedCookieSessionFactory('itsaseekret')
    #config.set_session_factory(my_session_factory)
    config.add_route('viewComponents', '/viewComponents')
    #config.scan('.views')
    config.add_view(views.view_components, route_name='viewComponents', renderer = 'json')
    #config.add_route('cartService', '/cartService')
    #config.add_view(cartService, route_name='cartService', renderer= 'json')
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=6543)

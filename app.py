from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.httpexceptions import HTTPOk
from pyramid.view import view_config, view_defaults
from pyramid.session import SignedCookieSessionFactory
import db


@view_config(request_method='GET', context=shoppingCartApp, renderer='json')
def view_components(context,request):
    print('Incoming request')
    r = context.retrieve()
    if r is None:
        raise HTTPNotFound()
    else:
        db.connectToDb()
        print db.dictionary
        return [db.dictionary]
    #return Response('<body>hello</body>')


if __name__ == '__main__':
    config = Configurator()
    my_session_factory = SignedCookieSessionFactory('itsaseekret')
    config.set_session_factory(my_session_factory)
    config.add_route('viewComponents', '/viewComponents')
    #config.scan('.views')
    config.add_view(view_components, route_name='viewComponents', renderer = 'json')
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=6543)

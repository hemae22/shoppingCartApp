from waitress import serve
from pyramid.config import Configurator

from pyramid.response import Response
from pyramid.httpexceptions import HTTPOk
from pyramid.view import view_config, view_defaults
from pyramid.session import SignedCookieSessionFactory

import db
import uuid
import views
import cartService
import orderService


if __name__ == '__main__':
    my_session_factory = SignedCookieSessionFactory('itsaseekreet')
    config = Configurator()
    config.set_session_factory(my_session_factory)
    config.add_route('viewComponents', '/viewComponents')
    config.add_view(views.view_components, route_name='viewComponents', renderer = 'json')
    config.add_route('addToCart', '/cartService/addToCart')
    config.add_view(cartService.addToCart, route_name='addToCart', renderer= 'json')
    config.add_route('removeFromCart', '/cartService/removeFromCart')
    config.add_view(cartService.removeFromCart, route_name='removeFromCart', renderer= 'json')
    config.add_route('clearCart', '/cartService/clearCart')
    config.add_view(cartService.clearCart, route_name='clearCart', renderer= 'json')
    config.add_route('viewCart', '/cartService/viewCart')
    config.add_view(cartService.viewCart, route_name='viewCart', renderer= 'json')
    config.add_route('orderService', '/orderService')
    config.add_view(orderService.order, route_name='orderService', renderer= 'json')
    config.add_route('viewOrder', '/orderService/viewOrder')
    config.add_view(orderService.viewOrder, route_name='viewOrder', renderer= 'json')
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=6543)

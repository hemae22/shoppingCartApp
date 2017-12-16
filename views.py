from pyramid.response import Response
from pyramid.view import view_config
import db

@view_config(route_name='viewComponents')
#@view_config(request_method='GET', context=shoppingCartApp, renderer='json')
#def view_components(context,request):
def view_components(request):
    return Response(db.dictionary)
    #r = context.retrieve()

    #if r is None:
    #    raise HTTPNotFound()
    #else:
    #    return r

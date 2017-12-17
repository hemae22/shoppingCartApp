from pyramid.view import view_config, view_defaults
from pyramid.response import Response

cart = {}

@view_config(route_name = 'addToCart', request_method='POST', renderer='json')
def addToCart(context,request):
    product_id = request.params.get('product_id')
    print product_id
    no_of_products = request.params.get('no_of_products')
    print no_of_products
    test_value = no_of_products * 10
    product_description = request.params.get('description')
    print product_description
    price = request.params.get('price')
    print price
    #print "This is session product is", request.session['product_id']
    #if product_id != request.session['product_id'] or request.session['product_id'] is None:
    if 'product_id' in request.session:
        print 'In session!'
        no_of_products = cart[product_id].get('no_of_products')
        no_of_products = no_of_products + 1
        cart[product_id] = {'no_of_products':no_of_products.encode("utf-8"), 'product_description':product_description.encode("utf-8"), 'price':price.encode("utf-8")}
        #cart[product_id].set('no_of_products') = no_of_products + 1
    else:
        print 'not in session'
        request.session['product_id'] = product_id
        request.session['no_of_products'] = no_of_products
        cart[product_id] = {'no_of_products': no_of_products.encode("utf-8"), 'product_description': product_description.encode("utf-8"), 'price': price.encode("utf-8")}
        print cart
        #cart[product_id] = {no_of_products + 1, product_description, price}

@view_config(route_name = 'removeFromCart', request_method='POST', renderer='json')
def removeFromCart(context,request):
    product_id = request.params.get('product_id')
    no_of_products = request.params.get('no_of_products')
    number_products = int(no_of_products)
    number_products = number_products - 1
    product_description = request.params.get('description')
    price = request.params.get('price')
    cart[product_id] = {'no_of_products':number_products, 'product_description': product_description.encode("utf-8"), 'price': price.encode("utf-8")}
    request.session['no_of_products'] = cart[product_id].get('no_of_products')
    print cart

@view_config(route_name = 'clearCart', request_method='POST', renderer='json')
def clearCart(context,request):
    cart.clear()
    request.session.pop['product_id']
    request.session.pop['no_of_products']

@view_config(route_name = 'viewCart', request_method='GET', renderer='json')
def viewCart(context,request):
    return cart;

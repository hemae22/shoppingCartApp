cart = [{}]

@view_config(route_name = 'addToCart', request_method='POST', renderer='json')
def addToCart(context,request):
    product_id = request.params.get('product_id')
    no_of_products = request.params.get('no_of_products')
    product_description = request.params.get('description')
    price = request.params.get('price')
    if product_id != request.session['product_id']:
        request.session['product_id'] = product_id
        request.session['no_of_products'] = no_of_products
        cart[product_id] = {'no_of_products':no_of_products, 'product_description':product_description, 'price':price}
    else:
        cart[product_id] = {no_of_products + 1, product_description, price}

@view_config(route_name = 'removeFromCart', request_method='POST', renderer='json')
def removeFromCart(context,request):
    product_id = request.params.get('product_id')
    no_of_products = request.params.get('no_of_products')
    if cart[product_id] != 0:
        cart[product_id] = {'no_of_products':no_of_products - 1, 'product_description':product_description, 'price':price}
        request.session['no_of_products'] = cart[product_id].get('no_of_products')
    else
        request.session['product_id'].del

@view_config(route_name = 'clearCart', request_method='POST', renderer='json')
def clearCart(context,request):
    cart.clear()
    request.session['product_id'].del
    request.session['no_of_products'].del

@view_config(route_name = 'viewCart', request_method='GET', renderer='json')
def viewCart(context,request):
    return cart;

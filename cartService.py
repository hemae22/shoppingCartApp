


cart = [{}]

def addToCart:


    cart[session['product_id']] = {session['product_name'], session['no_of_products'], session['client_id']}


def removeFromCart:
    cart.clear()

def modifyCart:


def viewCart:
    cart.value()

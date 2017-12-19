from pyramid.view import view_config, view_defaults
import cartService
import db
import uuid
orderItems = {}

@view_config(route_name ='orderService', request_method='POST', renderer='json')
def order(context,request):
    clientName =  request.params.get('client_Name')
    order_id = uuid.uuid1()
    address = request.params.get('address')
    date_of_delivery = request.params.get('date_of_delivery')
    time_of_delivery = request.params.get('time_of_delivery')
    clientInformation = {'clientName':clientName, 'address':address, 'date_of_delivery':date_of_delivery, \
    'time_of_delivery':time_of_delivery, 'order_id':order_id}
    orderID = str(order_id)
    request.session['order_id'] = orderID
    print cartService.cart
    orderItems = cartService.cart
    print "order items are", orderItems
    db.placeOrder(orderItems,clientInformation)
    return clientInformation['order_id']

@view_config(route_name ='viewOrder', request_method='POST', renderer='json')
def viewOrder(context,request):
    orderID = request.params.get('orderID')
    resultset = db.viewOrderDetails(orderID)
    return resultset

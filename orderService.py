from pyramid.view import view_config, view_defaults
import cartService
import db
import uuid
import json
orderItems = {}

@view_config(route_name ='orderService', request_method='POST', renderer='json')
def order(context,request):
    request.session['id'] = uuid.uuid1()
    sessionID = request.session['id']
    clientName =  request.params.get('client_Name')
    address = request.params.get('address')
    if request.params.get('client_ID') is None:
        client_ID = db.createClient(clientName, address)
    else:
        client_ID = request.params.get('client_ID')
    date_of_delivery = request.params.get('date_of_delivery')
    time_of_delivery = request.params.get('time_of_delivery')
    print cartService.cart
    orderItems = cartService.cart
    order_ID = db.placeOrder(orderItems,client_ID,sessionID,date_of_delivery,time_of_delivery)
    return order_ID


@view_config(route_name ='viewOrder', request_method='POST', renderer='json')
def viewOrder(context,request):
    orderID = request.params.get('orderID')
    resultset = db.viewOrderDetails(orderID)
    totalPrice = db.getTotalPrice(orderID)
    return resultset, totalPrice

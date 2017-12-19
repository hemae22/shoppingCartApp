import psycopg2
import json
import databaseconfig as cfg
dictionary = {}

conn = psycopg2.connect(database = cfg.mypsql['db'], user = cfg.mypsql['user'], password = cfg.mypsql['passwd'], host = cfg.mypsql['host'], port = cfg.mypsql['port'])
print "Opened database successfully"
curr = conn.cursor()

def retrieveProducts():
    curr = conn.cursor()
#view components table
    curr.execute("Select id, NAME, DESCRIPTION, PRICE FROM COMPONENTS")
    rows = curr.fetchall()
    j = 1
    for row in rows:
        dictionary[j] = [{'id':row[0], 'NAME':row[1], 'DESCRIPTION':row[2], 'PRICE':row[3]}]
        j = j + 1

    for i in dictionary:
        print dictionary[i]

    print "Operations completed successfully!"
    print len(dictionary)
    conn.close()

def placeOrder(orderItems, clientInformation):
    curr = conn.cursor()
    order_id = str(clientInformation['order_id'])
    print "order_id is", order_id
    curr.execute("UPDATE CLIENTS SET Name = %s, Address = %s, Order_ID = %s", (clientInformation['clientName'], clientInformation['address'], order_id))
    for item in orderItems:
        product_id = orderItems[item].get('product_id')
        print "PRODUCT ID", product_id
        product_name = orderItems[item].get('product_name')
        print "PRODUCT NAME", product_name
        product_description = orderItems[item].get('product_description')
        print "PRODUCT DESC", product_description
        no_of_products = orderItems[item].get('no_of_products')
        print "NO OF PRODUCTS", no_of_products
        price = orderItems[item].get('price')
        print "PRICE", price
        date_of_delivery = clientInformation['date_of_delivery']
        print "DOD", date_of_delivery
        time_of_delivery = clientInformation['time_of_delivery']
        print "TOD", time_of_delivery
        curr.execute("SET datestyle = dmy")
        curr.execute("UPDATE ORDERS SET Order_ID = %s, Product_ID = %s, Product_Name = %s, Description = %s, Number_of_Products = %s, Price = %s, Date_of_Delivery = %s, Time_of_Delivery = %s", (order_id, product_id, product_name, product_description, no_of_products, price, date_of_delivery, time_of_delivery))
        conn.commit()
    curr.execute("SELECT SUM(PRICE) FROM ORDERS INNER JOIN CLIENTS ON CLIENTS.ORDER_ID = ORDERS.ORDER_ID")
    rows = curr.fetchone()
    total_price = rows[0]
    print "this is total price", total_price
    curr.execute("UPDATE CLIENTS SET Total_Price = %s", [total_price])
    conn.commit()
    print "Order Operation Completed"

def viewOrderDetails(orderID):
    order_ID = str(orderID)
    print order_ID
    sql_text = "SELECT * FROM ORDERS WHERE Order_ID = %s"
    data = (order_ID)
    curr = conn.cursor()
    curr.execute(sql_text, [data])
    rows = curr.fetchall()
    resultset = {}
    j = 0
    for row in rows:
       resultset[j] = [{'Order_ID':str(row[0]), 'Product_ID':row[1], 'Product_Name':row[2], 'Description':row[3], 'Number_of_Products':row[4], 'Price':row[5], 'Date_of_Delivery':str(row[6]), 'Time_of_Delivery':str(row[7])}]
       j= j + 1
    return resultset

def getTotalPrice(orderID):
    order_ID = str(orderID)
    curr = conn.cursor()
    curr.execute("SELECT Total_Price from CLIENTS where Order_ID = %s", [order_ID])
    rows = curr.fetchone()
    total_price = rows[0]
    conn.close()
    return total_price

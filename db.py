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

def createClient(clientName, address):
    curr = conn.cursor()
    curr.execute("INSERT INTO CLIENTS(Name, Address) VALUES (%s,%s)", (clientName, address))
    curr.execute("SELECT Client_ID from CLIENTS where Name = %s", [clientName])
    rows = curr.fetchone()
    client_ID = rows[0]
    return client_ID

def placeOrder(orderItems,client_ID,sessionID,date_of_delivery,time_of_delivery):
    curr = conn.cursor()
    session_ID = str(sessionID)
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
        print "DOD", date_of_delivery
        print "TOD",time_of_delivery
        curr.execute("SET datestyle = dmy")
        curr.execute("INSERT INTO ORDERS(Session_ID, Client_ID, Product_ID, Product_Name, Description, Number_of_Products, Price, Date_of_Delivery, Time_of_Delivery) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (session_ID, client_ID, product_id, product_name, product_description, no_of_products, price, date_of_delivery, time_of_delivery))
        conn.commit()
    curr.execute("SELECT ORDER_ID FROM ORDERS where Session_ID = %s", [session_ID])
    rows = curr.fetchone()
    order_ID = rows[0]
    curr.execute("SELECT SUM(PRICE) FROM ORDERS where Session_ID=%s", [session_ID])
    items = curr.fetchone()
    total_price = items[0]
    curr.execute("INSERT INTO ORDERS_PRICE(Order_ID, Total_Price) VALUES (%s,%s)", (order_ID, total_price))
    print "this is total price", total_price
    conn.commit()
    print "Order Operation Completed"
    return order_ID

def viewOrderDetails(orderID):
    sql_text = "SELECT * FROM ORDERS WHERE Order_ID = %s"
    data = (orderID)
    curr = conn.cursor()
    curr.execute(sql_text, [data])
    rows = curr.fetchall()
    resultset = {}
    j = 0
    for row in rows:
       resultset[j] = [{'Order_ID':str(row[2]), 'Product_ID':row[3], 'Product_Name':row[4], 'Description':row[5], 'Number_of_Products':row[6], 'Price':row[7], 'Date_of_Delivery':str(row[8]), 'Time_of_Delivery':str(row[9])}]
       j= j + 1
    return resultset

def getTotalPrice(orderID):
    curr = conn.cursor()
    curr.execute("SELECT Total_Price from ORDERS_PRICE where Order_ID = %s", [orderID])
    rows = curr.fetchone()
    total_price = rows[0]
    conn.close()
    return total_price

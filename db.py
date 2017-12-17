import psycopg2

dictionary = {}
def connectToDb():
    conn = psycopg2.connect(database = "carcomponent_shopping", user = "postgres", password = "hema", host = "localhost", port = "5432")
    print "Opened database successfully"

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

Setup Info:
1. Installed Python intepreter
2. Installed pyrmaid 
 - Virtual env setup
3. Installed psycopg2
4. Application in - ..\Assignment-Project\shoppingCartApp 
5. Run application with following script
	..virtual env path\Scripts\python.exe app.py

   example : C:\Users\hema.elangovan\Documents\GitHub\Assignment-Project\shoppingCartApp>C:\%VENV%\Scripts\python.exe app.py
6. Testing the services (please refer Info - Services for Shopping Cart.txt file) 
	- Install curl 
	- in cmd run:
		POST Requests: curl -i -d "parameterName=parameterValue1&name2=nameValue" http://hostName:portNumber/resourcePath
			example: curl -i -d "orderID=3" http://localhost:6543/orderService/viewOrder
		GET Requests : curl http://hostName:portNumber/resourcePath



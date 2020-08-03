# hospital-fastapi
Hospital simulation in fastAPI 
### On Local machine
 - Create mysql database . Give it name 'zihospital';
 - To Migrate Database use command :
 - <code>python generate.py</code> 
 - Run application by using Command <code>uvicorn main:app --reload</code>.)


### Create an API for Patient reservation in hospital/clinic
 - Method : POST : http://127.0.0.1:8000/create
 - Example:
 - - Request:
     ```javascript
      {
      "username": "Zicaredev",
      "password": "hashpassword",
      "name":"Budi",
      "email":"budi@zicare.id",   
      "dob" : "29-9-1990"
      }
     ```
 - - Response :
      ```javascript
      {
      "message": {
        "messageCode": "000",
        "messageName": "SUCCESS",
        "messageDetail": "Service run successfully"
        },
      "result": {
        "password": "$2b$12$oEnjRNSvIdlRN",
        "patient_id": 7,
        "dob" : "29-9-1990"
        "name": "Budi",
        "username": "Zicarsedev",
        "email": "budi@zicare.id"
        }
      }  
      ```
### LOGIN
 - Method : POST : http://127.0.0.1:8000/login
 - Example:
 - - Response:
     ```javascript
      {
      "username": "Zicaredev",
      "password": "hashpassword"                      
      }
     ```
 - - Response :    
     ```javascript
     {
     "message": {
        "messageCode": "000",
        "messageName": "SUCCESS",
        "messageDetail": "Service run successfully"
        },
        "result": "Zicaredev"
      }
     ```

### Update

- Method  : PUT   : http://127.0.0.1:8000/update
- Example:
 - - Request  :
        ```javascript
        {
        "username": "Zicaredev",
        "password": "hashpassword",
        "name":"Budi",
        "email":"budi@zicare.id"   
        }
        ```
 - - Response     :
        ```javascript
        {
        "message": {
            "messageCode": "000",
            "messageName": "SUCCESS",
            "messageDetail": "Service run successfully"
        },
        "result": {
          "username": "Zicaredev",
          "name": "Budi",
          "email": "budi@zicare.id"
        }
      }
        ```

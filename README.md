### Objective

Your assignment is to build an internal API for a fake financial institution using Python and Flask.

### Brief

While modern banks have evolved to serve a plethora of functions, at their core, banks must provide certain basic features. Today, your task is to build the basic HTTP API for one of those banks! Imagine you are designing a backend API for bank employees. It could ultimately be consumed by multiple frontends (web, iOS, Android etc).

### Tasks

- A boilerplate is provided (optional to use):
  - Language: **Python**
  - Framework: **Flask**

- There should be API routes that allow them to:
  
  Plum Functional Requirement 1 - Create a new bank account for a customer, with an initial deposit amount.
  Plum Functional Requirement 2 - A single customer may have multiple bank accounts.
      (Naveen Suppala - Answer)
            Please refer to "step -1" of the detailed documentation below under "steps" section.
  
  Plum Functional Requirement 3 - Transfer amounts between any two accounts, including those owned by different customers.
      (Naveen Suppala - Answer)
            Please refer to "step -4" of the detailed documentation below under "steps" section.

  Plum Functional Requirement 4 - Retrieve balances for a given account.
      (Naveen Suppala - Answer)
            Please refer to "step -2" of the detailed documentation below under "steps" section.

  Plum Functional Requirement 5 - Write tests for your business logic
      (Naveen Suppala - Answer)
            Please refer to the test cases in "test_app.py" and also detailed documentation below under "Testing" section.

Feel free to pre-populate your customers with the following:

```json
[
  {
    "id": 1,
    "name": "Arisha Barron"
  },
  {
    "id": 2,
    "name": "Branden Gibson"
  },
  {
    "id": 3,
    "name": "Rhonda Church"
  },
  {
    "id": 4,
    "name": "Georgina Hazel"
  }
]
```

You are expected to design any other required models and routes for your API.

### Evaluation Criteria

- Engineering best practices
- Completeness: did you complete the features?
- Correctness: does the functionality act in sensible, thought-out ways?
- Maintainability: is it written in a clean, maintainable way?
- Testing: is the system adequately tested?

### CodeSubmit

Please organize, design, test and document your code as if it were going into production - then push your changes to the master branch. After you have pushed your code, you may submit the assignment on the assignment page.

All the best and happy coding,

The Plum Team

--------------------------------------------------Naveen Suppala-------------------------Flask Plum_API--------------------------Documentation------------------------
image.png

Project showing how to build a scalable, maintainable, modular Flask Banking API with a heavy emphasis on testing.

How to use ?
It has a development and a test set-up. 

To develop the web-service start-up the environment with docker-compose up.
Then you can develop the code locally on your computer.
To add packages to the environment, simply add them to the requirements.txt-file and rebuild the image with docker-compose up --build.

The Dockerfile then can be adapted to production and copies the current state of the flask-app and executes it.

Commands:
Open up Terminal -1 
  Run command - dockerd
Terminal -2
  Run command - sudo docker-compose build
  Run command - sudo docker-compose up

Then Access URL - 
http://localhost:5000

Then Access Swagger API documentation - swith to URL - 
http://localhost:5000/api/docs/

Steps--------------------------------------------------Steps--------------------------------------------------Steps--------------------------------------------------Steps--------------------------------------------------
USED POSTMAN TO TEST USING THESE JSON's
(1) Step - 1: Register as a new user
Method - POST
Path - /register
Parameters - user_name:str, password:str, account_id:str
URL - http://localhost:5000/register
Sample POST JSON - 
>>> Registering "Arisha Barron" with "account_id": "1"
user_1_register_1 = {
            "user_name": "Arisha Barron",
            "password": "secure",
            "account_id": "1"
        }
>>> Registering "Branden Gibson" with "account_id": "2"
user_2_register = {
            "user_name": "Branden Gibson",
            "password": "secure",
            "account_id": "2"
        }
>>> Registering "BANK user" with "account_id": "BANK"
user_BANK_register = {
            "user_name": "BANK user",
            "password": "secure",
            "account_id": "BANK"
        }
Note: Registering a "account_id": "BANK" is mandatory, as all transactions pass through this account_id.
>>> Registering "Arisha Barron" with another "account_id": "11"
user_1_register_second_account = {
            "user_name": "Arisha Barron",
            "password": "secure",
            "account_id": "11"
        }
Note: Registering a "account_id": "BANK" is mandatory, as all transactions pass through this account_id.
error-codes - 200 OK, 301 Invalid Username, 302 Invalid password


(2) Step - 2: Check balance of a user account
Method - POST
Path - /balance
Parameters - password:str, account_id:str
URL - http://localhost:5000/balance
Sample POST JSON - 
>>> Checking balance of "Arisha Barron" with "account_id": "1"
user_1_balance = {
            "password": "secure",
            "account_id": "1"
        }
>>> Checking balance of "BANK user" with "account_id": "BANK"
user_BANK_balance = {
            "password": "secure",
            "account_id": "BANK"
        }

(3) Step - 3: Add amount to a user account
Method - POST
Path - /add
Parameters - password:str, account_id:str, "amount": int
URL - http://localhost:5000/add
Sample POST JSON - 
>>> Add amount to "Arisha Barron's" account with "account_id": "1"
user_1_add = {
            "password": "secure",
            "account_id": "1",
            "amount": 2000
        }
     
(4) Step - 4: Transfer amount from one user account to another user account
Method - POST
Path - /transfer
Parameters - password:str, account_id:str, "amount": int, "to":str
URL - http://localhost:5000/transfer
Sample POST JSON - 
>>> Transfer amount from "Arisha Barron" account to "Branden Gibson" account
       #localhost:5000/transfer
user_1_transfer_to_user_2 = {
            "password": "secure",
            "account_id": "1",
            "to": "2",
            "amount": 200
        }
Note: "to" here is the account_id of the earlier registered user, to whoom you want to transfer an amount.
Note: "account_id" here is the account_id of the earlier registered user, from whoom you want to transfer an amount.

(5) Step - 5: Transfer amount from one user account to another account of the same user
Method - POST
Path - /transfer
Parameters - password:str, account_id:str, "amount": int, "to":str
URL - http://localhost:5000/transfer
Sample POST JSON - 
>>> Transfer amount from "Arisha Barron" account to "Branden Gibson" account
user_1_transfer_to_user_1_another_account = {
            "password": "secure",
            "account_id": "1",
            "to": "11",
            "amount": 200
        }
Note: "to" here is the account_id of the earlier registered user, to whoom you want to transfer an amount.
Note: "account_id" here is the account_id of the earlier registered user, from whoom you want to transfer an amount.


(6) Step - 6: user take loan
Method - POST
Path - /takeloan
Parameters - password:str, account_id:str, "amount": int
URL - http://localhost:5000/takeloan
Sample POST JSON - 
>>> user "Arisha Barron" taking loan amount 2000
user_1_takeloan = {
            "password": "secure",
            "account_id": "1",
            "amount": 2000
        }


(7) Step - 7: user pay back loan
Method - POST
Path - /payloan
Parameters - password:str, account_id:str, "amount": int
URL - http://localhost:5000/payloan
Sample POST JSON - 
>>> user "Arisha Barron" taking loan amount 2000
user_1_payloan = {
            "password": "secure",
            "account_id": "1",
            "amount": 200
        }


(8) Step - 8: user pay back loan
Method - POST
Path - /payloan
Parameters - password:str, account_id:str, "amount": int
URL - http://localhost:5000/payloan
Sample POST JSON - 
>>> user "Arisha Barron" paying back loan amount 200
user_1_payloan = {
            "password": "secure",
            "account_id": "1",
            "amount": 200
        }

(9) Step - 9: Delete all database entries
Method - POST
Path - /delete
Parameters - password:str, account_id:str, "amount": int
URL - http://localhost:5000/payloan
Sample POST JSON - 
>>> POST an empty JSON to clear DB 
delete_all_records = {
        }



Testing--------------------------------------------------Testing--------------------------------------------------Testing--------------------------------------------------Testing--------------------------------------------------

------- DEBUGGING HINTS ---------
Use Pdb for debugging - 
Debug commands
pdb.set_trace()
breakpoint()
print(response)
l-list
n-next line
continue
step
etc..

------- TESTING HINTS ---------
--Initial Setup--
Open new terminal-1 in <../plum-bank-tediac/web> project folder,
switch to root using - sudo su
then run command - dockerd
Note: You need to have docker pre installed

-------TESTING--------------------
Change the Docker file for testing.
>>>Wondering why change the Docker file ?
Because adding a change to Dockerfile calls test cases for testing after bringing up the app, unlike original Docker file whick only brings up the app.
What change?
In the last line of file add -
CMD [ "python", "test_app.py" ]
To revert to original Dockerfile, just remove the previously added last line
CMD [ "python", "app.py" ]

Dockers CMD, always picks the last line,
so, if the last line is CMD [ "python", "app.py" ], only app will launch
and , if the last line is CMD [ "python", "test_app.py" ], test cases will run after bring up the app.

After changing the docker file as explained above.
Now, open new terminal-2 in <../plum-bank-tediac/web> project folder,
Docker compose using commands below,
- sudo docker-compose build
- sudo docker-compose up

Test Results - All test 19 cases will pass with OK


SwaggerUI--------------------------------------------------SwaggerUI--------------------------------------------------SwaggerUI--------------------------------------------------SwaggerUI--------------------------------------------------

Server - http://localhost:5000
Swagger API documentation - URL - http://localhost:5000/api/docs/


REST API Best Practices--------------------------------------------------REST API Best Practices--------------------------------------------------REST API Best Practices--------------------------------------------------
This page lists out some of the Best Practices and Guidelines that are followed when designing a REST API to make it easy for the developers to use and implement.

1. HTTP Methods
HTTP methods define the types of actions that can be performed on a resource.
POST method requests the server to insert a resource into the database.
Examples -
POST /register - can be used to register new user into the database.

2. RESTful Endpoints
Endpoints should include nouns, not verbs or actions.

Avoid

/doRegister
/doAdd

Use

/register
Only Plural nouns should be used for consistency.

But how do you tell the endpoint what action to perform? Solution - Use HTTP verbs (GET, POST, PUT, PATCH, DELETE) to perform CRUD actions.
Examples -

GET /api will get a list.

GET /api/1 will get the list with ID 1.

POST /api can be used to insert one or more items into the database.
/api should be able to handle one or more items.

DELETE /api/1 will delete the item with ID 1.

PUT/PATCH /api/1 will update the item with ID 1.

3. HTTP Responses
HTTP defines a set of Status Codes that must be included in your API responses to tell the developer that status of his/her request.
Here are some of the commonly used Status Codes -

200 OK - GET, PUT, PATCH or DELETE was successful.
201 Created - POST request was successful.
204 No Content - DELETE was successful.
400 Bad Request - There were inavlid parameters in the request. Developer must fix them.
401 Unauthorized - Invalid Credentials were provided.
404 Not Found - URL does not exist.
405 Method Not Allowed - Requested method is not allowed on the resource.
500 Internal Server Error - Problem with the server.

4. Documentation
Docs should be easily accessible and readable. Should provide examples of requests and responses. Should always be upto date. Your docs should follow the Open API standards. We have used two types of docs in this example, both of which depend on the Open API spec.

Swagger UI - Lets users test out the various endpoints.
Access Swagger API documentation - URL - http://localhost:5000/api/docs/

5. Validation
Your API should validate the requests being sent to the server and provide appropriate responses. 


-------------------------------------------------------TEST CASES OUTPUT-------------------------------------------------------
uccessfully tagged plum-bank-tediac_web:latest
root@LAPTOP-GSISA7EO:/mnt/d/plum-bank-tediac/web# sudo docker-compose up
Starting plum-bank-tediac_db_1 ... done
Recreating plum-bank-tediac_web_1 ... done
Attaching to plum-bank-tediac_db_1, plum-bank-tediac_web_1
db_1   | 2022-05-21T21:21:59.314+0000 I CONTROL  [initandlisten] MongoDB starting : pid=1 port=27017 dbpath=/data/db 64-bit host=bc8bfeec4206
db_1   | 2022-05-21T21:21:59.314+0000 I CONTROL  [initandlisten] db version v3.6.4
db_1   | 2022-05-21T21:21:59.314+0000 I CONTROL  [initandlisten] git version: d0181a711f7e7f39e60b5aeb1dc7097bf6ae5856
db_1   | 2022-05-21T21:21:59.314+0000 I CONTROL  [initandlisten] OpenSSL version: OpenSSL 1.0.1t  3 May 2016
db_1   | 2022-05-21T21:21:59.314+0000 I CONTROL  [initandlisten] allocator: tcmalloc
db_1   | 2022-05-21T21:21:59.314+0000 I CONTROL  [initandlisten] modules: none
db_1   | 2022-05-21T21:21:59.314+0000 I CONTROL  [initandlisten] build environment:
db_1   | 2022-05-21T21:21:59.314+0000 I CONTROL  [initandlisten]     distmod: debian81
db_1   | 2022-05-21T21:21:59.314+0000 I CONTROL  [initandlisten]     distarch: x86_64
db_1   | 2022-05-21T21:21:59.314+0000 I CONTROL  [initandlisten]     target_arch: x86_64
db_1   | 2022-05-21T21:21:59.314+0000 I CONTROL  [initandlisten] options: { net: { bindIpAll: true } }
db_1   | 2022-05-21T21:21:59.314+0000 W -        [initandlisten] Detected unclean shutdown - /data/db/mongod.lock is not empty.
db_1   | 2022-05-21T21:21:59.314+0000 I -        [initandlisten] Detected data files in /data/db created by the 'wiredTiger' storage engine, so setting the active storage engine to 'wiredTiger'.
db_1   | 2022-05-21T21:21:59.314+0000 W STORAGE  [initandlisten] Recovering data from the last clean checkpoint.
db_1   | 2022-05-21T21:21:59.314+0000 I STORAGE  [initandlisten] 
db_1   | 2022-05-21T21:21:59.314+0000 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
db_1   | 2022-05-21T21:21:59.314+0000 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
db_1   | 2022-05-21T21:21:59.314+0000 I STORAGE  [initandlisten] wiredtiger_open config: create,cache_size=1406M,session_max=20000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),cache_cursors=false,log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000),statistics_log=(wait=0),verbose=(recovery_progress),
db_1   | 2022-05-21T21:21:59.994+0000 I STORAGE  [initandlisten] WiredTiger message [1653168119:994648][1:0x7f6d82ef2a00], txn-recover: Main recovery loop: starting at 89/22784
db_1   | 2022-05-21T21:21:59.995+0000 I STORAGE  [initandlisten] WiredTiger message [1653168119:995409][1:0x7f6d82ef2a00], txn-recover: Recovering log 89 through 90
db_1   | 2022-05-21T21:22:00.067+0000 I STORAGE  [initandlisten] WiredTiger message [1653168120:67977][1:0x7f6d82ef2a00], txn-recover: Recovering log 90 through 90
db_1   | 2022-05-21T21:22:00.201+0000 I STORAGE  [initandlisten] WiredTiger message [1653168120:201527][1:0x7f6d82ef2a00], txn-recover: Set global recovery timestamp: 0
db_1   | 2022-05-21T21:22:00.249+0000 I CONTROL  [initandlisten] 
db_1   | 2022-05-21T21:22:00.249+0000 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
db_1   | 2022-05-21T21:22:00.249+0000 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
db_1   | 2022-05-21T21:22:00.249+0000 I CONTROL  [initandlisten] 
db_1   | 2022-05-21T21:22:00.250+0000 I CONTROL  [initandlisten] 
db_1   | 2022-05-21T21:22:00.250+0000 I CONTROL  [initandlisten] ** WARNING: /sys/kernel/mm/transparent_hugepage/enabled is 'always'.
db_1   | 2022-05-21T21:22:00.250+0000 I CONTROL  [initandlisten] **        We suggest setting it to 'never'
db_1   | 2022-05-21T21:22:00.250+0000 I CONTROL  [initandlisten] 
db_1   | 2022-05-21T21:22:00.263+0000 I FTDC     [initandlisten] Initializing full-time diagnostic data capture with directory '/data/db/diagnostic.data'
db_1   | 2022-05-21T21:22:00.264+0000 I NETWORK  [initandlisten] waiting for connections on port 27017
db_1   | 2022-05-21T21:22:00.660+0000 I NETWORK  [listener] connection accepted from 172.19.0.3:41290 #1 (1 connection now open)
db_1   | 2022-05-21T21:22:00.665+0000 I NETWORK  [conn1] received client metadata from 172.19.0.3:41290 conn1: { driver: { name: "PyMongo", version: "4.1.1" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "5.10.102.1-microsoft-standard-WSL2" }, platform: "CPython 3.10.4.final.0" }
db_1   | 2022-05-21T21:22:00.677+0000 I NETWORK  [listener] connection accepted from 172.19.0.3:41292 #2 (2 connections now open)
db_1   | 2022-05-21T21:22:00.677+0000 I NETWORK  [conn2] received client metadata from 172.19.0.3:41292 conn2: { driver: { name: "PyMongo", version: "4.1.1" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "5.10.102.1-microsoft-standard-WSL2" }, platform: "CPython 3.10.4.final.0" }
db_1   | 2022-05-21T21:22:01.006+0000 I FTDC     [ftdc] Unclean full-time diagnostic data capture shutdown detected, found interim file, some metrics may have been lost. OK
db_1   | 2022-05-21T21:22:02.821+0000 I COMMAND  [conn2] CMD: drop MoneyManagementDB.Users
db_1   | 2022-05-21T21:22:02.822+0000 I STORAGE  [conn2] Finishing collection drop for MoneyManagementDB.Users (4f0a3ab3-b84c-46ac-94cf-ead1ee121b41).
web_1  | ...................
web_1  | ----------------------------------------------------------------------
web_1  | Ran 19 tests in 2.165s
web_1  | 
web_1  | OK
db_1   | 2022-05-21T21:22:03.217+0000 I NETWORK  [conn2] end connection 172.19.0.3:41292 (1 connection now open)
db_1   | 2022-05-21T21:22:03.217+0000 I NETWORK  [conn1] end connection 172.19.0.3:41290 (0 connections now open)
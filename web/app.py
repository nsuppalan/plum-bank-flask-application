from flask import Flask, jsonify, request, render_template
from flask_restful import Api, Resource
from pymongo import MongoClient
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint
from flask import send_from_directory
import bcrypt
import os

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.MoneyManagementDB
users = db["Users"]

def Account_id_Exist(account_id):
    existing_user = users.find_one({"account_id":account_id})
    if existing_user:
        return True
    else:
        return False

def User_Exist(user_name):
    existing_user = users.find_one({"user_name":user_name})
    if existing_user:
        return True
    else:
        return False


class Register(Resource):
    def post(self):
        #Step 1 is to get posted data by the user
        postedData = request.get_json()

        #Get the data
        account_id = postedData["account_id"]#"123xyz"
        password = postedData["password"] #"123xyz"
        user_name = postedData["user_name"] #"123xyz"

        if Account_id_Exist(account_id):
            retJson = {
                'status':301,
                'msg': 'Invalid account_id'
            }
            return jsonify(retJson)

        hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

        #Store account_id and pw into the database
        users.insert_one({
            "account_id": account_id,
            "Password": hashed_pw,
            "user_name": user_name,
            "Own":0,
            "Debt":0
        })

        retJson = {
            "status": 200,
            "msg": "You successfully signed up for the API"
        }
        return jsonify(retJson)

def verifyPw(account_id, password):
    if not Account_id_Exist(account_id):
        return False

    hashed_pw = users.find({
        "account_id":account_id
    })[0]["Password"]

    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    else:
        return False

def cashWithUser(account_id):
    cash = users.find({
        "account_id":account_id
    })[0]["Own"]
    return cash

def debtWithUser(account_id):
    debt = users.find({
        "account_id":account_id
    })[0]["Debt"]
    return debt

def generateReturnDictionary(status, msg):
    retJson = {
        "status": status,
        "msg": msg
    }
    return retJson

def verifyCredentials(account_id, password):
    if not Account_id_Exist(account_id):
        return generateReturnDictionary(301, "Invalid account_id"), True

    correct_pw = verifyPw(account_id, password)

    if not correct_pw:
        return generateReturnDictionary(302, "Incorrect Password"), True

    return None, False

def updateAccount(account_id, balance):
    users.update_one({
        "account_id": account_id
    },{
        "$set":{
            "Own": balance
        }
    })

def updateDebt(account_id, balance):
    users.update_one({
        "account_id": account_id
    },{
        "$set":{
            "Debt": balance
        }
    })



class Add(Resource):
    def post(self):
        postedData = request.get_json()

        account_id = postedData["account_id"]
        password = postedData["password"]
        money = postedData["amount"]

        retJson, error = verifyCredentials(account_id, password)
        if error:
            return jsonify(retJson)

        if money<=0:
            return jsonify(generateReturnDictionary(304, "The money amount entered must be greater than 0"))

        cash = cashWithUser(account_id)
        money-= 1 #Transaction fee
        #Add transaction fee to bank account
        bank_cash = cashWithUser("BANK")
        updateAccount("BANK", bank_cash+1)

        #Add remaining to user
        updateAccount(account_id, cash+money)

        return jsonify(generateReturnDictionary(200, "Amount Added Successfully to account"))

class Transfer(Resource):
    def post(self):
        postedData = request.get_json()

        account_id = postedData["account_id"]
        password = postedData["password"]
        to       = postedData["to"]
        money    = postedData["amount"]


        retJson, error = verifyCredentials(account_id, password)
        if error:
            return jsonify(retJson)

        cash = cashWithUser(account_id)
        if cash <= 0:
            return jsonify(generateReturnDictionary(303, "You are out of money, please Add Cash or take a loan"))

        if money<=0:
            return jsonify(generateReturnDictionary(304, "The money amount entered must be greater than 0"))

        if not Account_id_Exist(to):
            return jsonify(generateReturnDictionary(301, "Recieved account_id is invalid"))

        cash_from = cashWithUser(account_id)
        cash_to   = cashWithUser(to)
        bank_cash = cashWithUser("BANK")

        updateAccount("BANK", bank_cash+1)
        updateAccount(to, cash_to+money-1)
        updateAccount(account_id, cash_from - money)

        retJson = {
            "status":200,
            "msg": "Amount added successfully to account"
        }
        return jsonify(generateReturnDictionary(200, "Amount added successfully to account"))

class Balance(Resource):
    def post(self):
        postedData = request.get_json()

        account_id = postedData["account_id"]
        password = postedData["password"]

        retJson, error = verifyCredentials(account_id, password)
        if error:
            return jsonify(retJson)

        retJson = users.find({
            "account_id": account_id
        },{
            "Password": 0, #projection
            "_id":0
        })[0]

        return jsonify(retJson)

class TakeLoan(Resource):
    def post(self):
        postedData = request.get_json()

        account_id = postedData["account_id"]
        password = postedData["password"]
        money    = postedData["amount"]

        retJson, error = verifyCredentials(account_id, password)
        if error:
            return jsonify(retJson)

        cash = cashWithUser(account_id)
        debt = debtWithUser(account_id)
        updateAccount(account_id, cash+money)
        updateDebt(account_id, debt + money)

        return jsonify(generateReturnDictionary(200, "Loan Added to Your Account"))

class PayLoan(Resource):
    def post(self):
        postedData = request.get_json()

        account_id = postedData["account_id"]
        password = postedData["password"]
        money    = postedData["amount"]

        retJson, error = verifyCredentials(account_id, password)
        if error:
            return jsonify(retJson)

        cash = cashWithUser(account_id)

        if cash < money:
            return jsonify(generateReturnDictionary(303, "Not Enough Cash in your account"))

        debt = debtWithUser(account_id)
        updateAccount(account_id, cash-money)
        updateDebt(account_id, debt - money)

        return jsonify(generateReturnDictionary(200, "Loan Paid"))

@app.route("/", methods=["GET", "POST"])
def home():
    #return 'hello world!\n'
    return jsonify({"secured": "Plum Bank App"})

@app.route("/delete", methods=["POST"])
def delete_all():
    #return 'deleted all\n'
    users.drop()
    return jsonify({"secured": "Plum Bank App Users cleared"})


@app.route("/api/spec")
def spec():
    swag = swagger(app, prefix='/api')
    swag['info']['base'] = "http://localhost:5000"
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Flask PlumAPI"
    return jsonify(swag)

SWAGGER_URL = "/api/docs"
API_URL = "/docs/swaggerurl.json"
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL,API_URL,config={'app_name': "Flask PlumAPI"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route("/docs/swaggerurl.json")
def specs():
    import os.path
    return send_from_directory(os.getcwd(), "swaggerurl.json")


api.add_resource(Register, '/register')
api.add_resource(Add, '/add')
api.add_resource(Transfer, '/transfer')
api.add_resource(Balance, '/balance')
api.add_resource(TakeLoan, '/takeloan')
api.add_resource(PayLoan, '/payloan')



if __name__=="__main__":
    app.run(host='0.0.0.0')
    #app.run(debug=True, ssl_context='adhoc', host='0.0.0.0')

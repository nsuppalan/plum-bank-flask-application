import unittest
import os
import json

from flask import json
from unittest import TestCase
import pdb;

from app import app, db, users


class AppTest(TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        #localhost:5000/register
        self.user_1_register_1 = {
            "user_name": "Arisha Barron",
            "password": "secure",
            "account_id": "1"
        }

        self.user_1_register_second_account = {
            "user_name": "Arisha Barron",
            "password": "secure",
            "account_id": "11"
        }
    
        self.user_2_register = {
            "user_name": "Branden Gibson",
            "password": "secure",
            "account_id": "2"
        }

        self.user_3_register = {
            "user_name": "Rhonda Church",
            "password": "secure",
            "account_id": "3"
        }

        self.user_4_register = {
            "user_name": "Georgina Hazel",
            "password": "secure",
            "account_id": "4"
        }

        self.user_BANK_register = {
            "user_name": "BANK user",
            "password": "secure",
            "account_id": "BANK"
        }

    #localhost:5000/balance
        self.user_1_balance = {
            "password": "secure",
            "account_id": "1"
        }
        
        self.user_2_balance = {
            "password": "secure",
            "account_id": "2"
        }

        self.user_3_balance = {
            "password": "secure",
            "account_id": "3"
        }

        self.user_4_balance = {
            "password": "secure",
            "account_id": "4"
        }

        self.user_BANK_balance = {
            "password": "secure",
            "account_id": "BANK"
        }
        
        #localhost:5000/add
        self.user_1_add = {
            "password": "secure",
            "account_id": "1",
            "amount": 2000
        }
                
        #localhost:5000/transfer
        self.user_1_transfer_to_user_2 = {
            "password": "secure",
            "account_id": "1",
            "to": "2",
            "amount": 200
        }

        #localhost:5000/transfer
        self.user_1_transfer_to_user_1_another_account = {
            "password": "secure",
            "account_id": "1",
            "to": "11",
            "amount": 200
        }
        
        #localhost:5000/takeloan
        self.user_1_takeloan = {
            "password": "secure",
            "account_id": "1",
            "amount": 2000
        }

        #localhost:5000/payloan
        self.user_1_payloan = {
            "password": "secure",
            "account_id": "1",
            "amount": 200
        }

        self.delete_all_records = {
        }

     #localhost:5000/register
     # create user 1
    with app.app_context():
        def test_home(self):
            url_path = '/'
            response = self.app.get(url_path)
            self.assertEqual(response.status_code, 200)

        def test_post(self):
            url_path = '/'
            response = self.app.post(url_path,data={"content": "this is a test"})
            self.assertEqual(response.status_code, 200)
        
        # create user 1
        def test_user_1_register_1(self):
            response = self.app.post('/register', data=json.dumps(self.user_1_register_1),content_type='application/json',)
            data = json.loads(response.get_data(as_text=True))
            self.assertEqual(response.status_code, 200)

            # create user 1 - another account
        def test_user_1_register_second_account(self):
            response = self.app.post('/register', data=json.dumps(self.user_1_register_second_account),content_type='application/json',)
            data = json.loads(response.get_data(as_text=True))
            self.assertEqual(response.status_code, 200)
            
        # create user 2
        def test_user_2_register(self):
            response = self.app.post("/register", data=json.dumps(self.user_2_register),content_type='application/json')
            data = json.loads(response.get_data(as_text=True))
            self.assertEqual(response.status_code, 200)
            
        # create user 3
        def test_user_3_register(self):
            response = self.app.post("/register", data=json.dumps(self.user_3_register),content_type='application/json')
            data = json.loads(response.get_data(as_text=True))
            self.assertEqual(response.status_code, 200)

        # create user 4
        def test_user_4_register(self):
            response = self.app.post("/register", data=json.dumps(self.user_4_register),content_type='application/json')
            data = json.loads(response.get_data(as_text=True))
            self.assertEqual(response.status_code, 200)

        # create user BANK
        def test_user_BANK_register(self):
            response = self.app.post("/register", data=json.dumps(self.user_BANK_register),content_type='application/json')
            data = json.loads(response.get_data(as_text=True))
            self.assertEqual(response.status_code, 200)
        
        #localhost:5000/balance
        # balance user 1
        def test_user_1_balance(self):
            response = self.app.post("/balance", data=json.dumps(self.user_1_balance),content_type='application/json')
            data = json.loads(response.get_data(as_text=True))
            self.assertEqual(response.status_code, 200)

        # balance user 2
        def test_user_2_balance(self):
            response = self.app.post("/balance", data=json.dumps(self.user_2_balance),content_type='application/json')
            data = json.loads(response.get_data(as_text=True))
            self.assertEqual(response.status_code, 200)

        # balance user 3
        def test_user_3_balance(self):
            response = self.app.post("/balance", data=json.dumps(self.user_3_balance),content_type='application/json')
            data = json.loads(response.get_data(as_text=True))
            self.assertEqual(response.status_code, 200)

        # balance user 4
        def test_user_4_balance(self):
            response = self.app.post("/balance", data=json.dumps(self.user_4_balance),content_type='application/json')
            data = json.loads(response.get_data(as_text=True))
            self.assertEqual(response.status_code, 200)

        # balance user BANK
        def test_user_BANK_balance(self):
            response = self.app.post("/balance", data=json.dumps(self.user_BANK_balance),content_type='application/json')
            data = json.loads(response.get_data(as_text=True))
            self.assertEqual(response.status_code, 200)

        #localhost:5000/add
        # add money user 1
        def test_user_1_add(self):
            response = self.app.post("/add", data=json.dumps(self.user_1_add),content_type='application/json')
            data = json.loads(response.get_data(as_text=True))
            self.assertEqual(response.status_code, 200)

        #localhost:5000/transfer
        # add money user 1
        def test_user_1_transfer_to_user_2(self):
            response = self.app.post("/transfer", data=json.dumps(self.user_1_transfer_to_user_2),content_type='application/json')
            data = json.loads(response.get_data(as_text=True))
            self.assertEqual(response.status_code, 200)

        # add money user 1
        def test_user_1_transfer_to_user_1_another_account(self):
            response = self.app.post("/transfer", data=json.dumps(self.user_1_transfer_to_user_1_another_account),content_type='application/json')
            data = json.loads(response.get_data(as_text=True))
            self.assertEqual(response.status_code, 200)

        #user_1_transfer_to_user_1_another_account
        #localhost:5000/takeloan
        # takeloan user 1
        def test_user_1_takeloan(self):
            response = self.app.post("/takeloan", data=json.dumps(self.user_1_takeloan),content_type='application/json')
            data = json.loads(response.get_data(as_text=True))
            self.assertEqual(response.status_code, 200)

        #localhost:5000/payloan
        # payloan user 1
        def test_user_1_payloan(self):
            response = self.app.post("/payloan", data=json.dumps(self.user_1_payloan),content_type='application/json')
            data = json.loads(response.get_data(as_text=True))
            self.assertEqual(response.status_code, 200)
        
        #localhost:5000/payloan
        # payloan user 1
        def test_user_delete_all_records(self):
            response = self.app.post("/delete", data=json.dumps(self.delete_all_records),content_type='application/json')
            data = json.loads(response.get_data(as_text=True))
            self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()

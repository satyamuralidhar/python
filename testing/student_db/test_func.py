from function import StudentDB
import pytest

#creating a custom module
db=None

def setup_module(module):
    print("******************** setup module ***********************")
    global db
    db = StudentDB()
    # connect the db
    db.connection("data.json")
    print()

def teardown_module(module):
    """
    if we want to use any functionality 
    after all test exectution is done we can use teardown module.
    for ex: i do want close connection of DB
    """
    print("******************** tear down ***********************")
    db.close()
    print()


def test_satya():
    #intianlize the DB form class
    # db = StudentDB()
    # #connect the db
    # db.connection('data.json')
    #get the user data form get_data method
    user_data = db.get_data('Satya')
    
    assert user_data['id'] == 1
    assert user_data['name'] == 'Satya'
    assert user_data["colleage"] == "JNTUK"
    assert user_data["course"] =="Btech"

def test_mohan():
#     #intianlize the DB form class
    # db = StudentDB()
    # #connect the db
#     db.connection('data.json')
#     #get the user data form get_data method
    user_data = db.get_data('Mohan')
    
    assert user_data['id'] == 2
    assert user_data['name'] == 'Mohan'
    assert user_data["colleage"]== "JNTUK"
    assert user_data["course"]=="MBA"


'''
OR we can achive this using fixtures 
'''
from function import StudentDB
import pytest

#creating a custom module

'''
By using fixtures we can add funtionality to multiple functions
'''

@pytest.fixture(scope="module")
def db():
    print("******************** setup module ***********************")
    db = StudentDB()
    db.connection("data.json")
    yield db
    print("******************** tear down ***********************")
    db.close()

def test_satya(db):

    user_data = db.get_data('Satya')
    
    assert user_data['id'] == 1
    assert user_data['name'] == 'Satya'
    assert user_data["colleage"] == "JNTUK"
    assert user_data["course"] =="Btech"

def test_mohan(db):
    user_data = db.get_data('Mohan')
    
    assert user_data['id'] == 2
    assert user_data['name'] == 'Mohan'
    assert user_data["colleage"]== "JNTUK"
    assert user_data["course"]=="MBA"
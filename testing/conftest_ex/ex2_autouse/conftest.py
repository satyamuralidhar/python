import pytest
from function import StudentDB 

@pytest.fixture(scope="module",autouse=True)
def db():
    print("******************** setup module ***********************")
    db = StudentDB()
    db.connection("data.json")
    yield db
    print("******************** tear down ***********************")
    db.close()
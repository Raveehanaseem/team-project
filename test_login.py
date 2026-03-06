from login import login

def test_valid_login():
    assert login("admin", "admin123") == True

def test_invalid_login():
    assert login("admin", "wrongpass") == False

def test_invalid_user():
    assert login("unknown", "pass123") == False

import pytest
from authentication import *

def  test_validate_user():
	username='admin'
	password='123456'
	assert validate_user(username,password) ==  True

def  test_validate_password():
	password='abc'
	with pytest.raises(AuthenticationException):
		authenticate(password)

def  test_validate_user_incorrect_pwd():
	username='admin'
	password='hello'
	assert validate_user(username,password) ==  False
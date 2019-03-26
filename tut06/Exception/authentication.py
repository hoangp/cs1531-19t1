class  AuthenticationException(Exception):
	pass

def authenticate(input_password):
	# business logic: password must be '123456'
    if input_password != '123456':
        raise AuthenticationException("Invalid password was provided")
    return True

def validate_user(username, password):
	try:
		# business logic: usename must be 'admin' and password must be authorized
		return username == "admin" and authenticate(password)

	except AuthenticationException as e:
		print("Invalid password. Please try again")
		print(e)
		print(e.args)
		print(type(e)) # print the type of Exception thrown
		return  False
		
	else:
		print("You have been successfully authenticated")
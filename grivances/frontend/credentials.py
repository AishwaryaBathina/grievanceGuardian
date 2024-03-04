loggedinUsername = ""

def get_credentials():
    global loggedinUsername
    username = loggedinUsername
    return username

def get_credentialsfromfile(username):
    global loggedinUsername
    loggedinUsername = username
    print("crede",loggedinUsername)
    return

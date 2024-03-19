user = 'zay'
passcode = '123'
username = input("Username : ")
password = input("Password : ")

if username == user and password == passcode:
    print("Hello, " + username)
elif username == user and password != passcode:
    print("wrong password")
elif username != user or passcode != passcode:
    print("Username or Password Error. Try again")
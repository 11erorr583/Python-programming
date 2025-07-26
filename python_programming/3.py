# Create a login system using username/password stored in a dictionary

credentials ={
    "zubia":1234,
    "Ali": 5555
}
while True:
    username = input("Enter username ").strip()
    password = int(input("Enter password "))
    if username in credentials and credentials[username] == password:
        print(" Access granted ")
        break
    else:
      print( 'invalid entry ')
      choise = int(input(" 1:signup,2:Try again "))
      if choise == 1:
           name = input(" Enter username ")
           passcode = int(input(" Enter password "))
           credentials[name]=passcode
           print("You have signed up ")
      elif choise !=1 :
            print(" Try login with correct credentials! ")
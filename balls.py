import pyfiglet
from fernet import Fernet

#Logo
logo1 = pyfiglet.figlet_format("PssManager")
print(logo1)
print(""" 
--------------------------------------------
- USE "save" <email> <password>             -
- USE "list"                               -
- USE "checken"                            -
--------------------------------------------
""")


key = Fernet.generate_key()
key2 = Fernet(key)


#Save function
def save(username, password):
    with open('psx2z.txt' 'wb') as file2:
        contents = file2.write(username, password)
        key2.encrypt(contents)


#checks passwords/username function
def list():
  with open('psx2z.txt', 'wb') as file:
     decryp = key2.decrypt(file.readlines())
     print(decryp)

#interactive shell
while 1:
    x = input(">>>")
    if x == 'check':
        try:
            list()
        except:
            print("[ERROR] Error has accured")
    if x == 'save':
        try:
            save()
        except:
            print("[ERROR] a error has accured")
    if x == 'checken':
        try:
         print(key)
        except:
            print("[ERROR] error has accured")





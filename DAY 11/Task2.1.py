username = input("Please enter your username: ")
password = input("Please enter your password: ")

if username == "admin" and password == "123456":
    print("Sistemə daxil oldunuz təşəkkür edirik")
    
elif username == "" and password == "":
    print("Dəyərlər boş buraxıla bilməz")
    
elif username != "admin " and password != "123456":
    print("Daxil olunan melumat sefdir")
    
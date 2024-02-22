
def password():
    user = input("User-nya=")
    passw = input("Password-nya =")
    username_from_db = "user"
    password_from_db = "admin"
    if user == username_from_db:
        if passw == password_from_db:
            print("username dan passsword cocok")
        else:
            print("password salah")
    else:
        print("user tidak ditemukan")



        
password()
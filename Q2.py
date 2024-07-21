email=input("Please enter your email: ")
def Emailcheck(email):
    if "@"  in email:
        if "."in email:
            return "Your email is valid"
        else:
            return "Your email is unvalid"
    else:
        return "Your email is unvalid"
print(Emailcheck(email))
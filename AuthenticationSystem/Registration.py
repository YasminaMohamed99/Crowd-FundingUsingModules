import  re

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def register():
    while True:
        First_Name=input("First_Name: ")
        if First_Name.isalpha():
            while True:
                Last_Name=input("Last_Name: ")
                if Last_Name.isalpha():
                    while True:
                        Email=input("Email: ")
                        if(re.fullmatch(email_regex, Email)):
                            while True:
                                Password=input("Password: ")
                                if len(Password) >= 8:
                                    while True:
                                        Confirm_Password=input("Confirm Password: ")
                                        if Confirm_Password == Password:
                                            while True:
                                                Phone=input("Enter Phone Number: ")
                                                if Phone.isdigit() and len(Phone) == 11 and (Phone.startswith("011") | Phone.startswith("012")| Phone.startswith("010")| Phone.startswith("015")):
                                                    print("Done")
                                                    data=[First_Name,Last_Name,Email,Password,Confirm_Password,Phone]
                                                    open("AuthenticationSystem/registerData.txt","a").write("|".join(data))
                                                    open("AuthenticationSystem/registerData.txt","a").write("\n")
                                                    break
                                                else:
                                                    print("Please enter valid phone number!")
                                            break
                                        else:
                                            print("Password not match!")
                                    break
                                else:
                                    print("Password length must 8 or more!")
                            break
                        else:
                            print("Please enter valid email")
                    break
                else:
                    print("Please enter last name without number!")        
            break                
        else:
            print("Please enter first name without number!")
    

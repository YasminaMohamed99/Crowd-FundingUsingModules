from Projects.createProject import create
 
def login():
    while True:
        Email=input("Email: ")
        Password=input("Password: ")
        check_data=open("AuthenticationSystem/registerData.txt","r").readlines()
        record_data=[]
        list_true=[]
        check_login = False
        valid_mail = ""
        for record in check_data:
            record_data=record.split("|")
            for item in record_data:
                if item == Email:
                    list_true = record_data
                    for i in list_true:
                        if Password == i:
                            check_login = True
                            valid_mail = Email
                 
        if check_login == True :
            create(valid_mail)
        else:
            print("Email or password not valid")            
        break
        
        
        
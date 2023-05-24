db={}
print("*"*82)
print("\t\t|| * || {:^15} || * ||".format("PLATINUM JUBLEE HIGH SCHOOL,GADCHIROLI"))
print("*"*82)
while True:
    print("-"*82)
    print("""
                          STUDENT DETAILS


                        1.Add Student Details
                        2.Display Student Details
                        3.Update Student Details
                        4.Delete Student Details
    """)
    print("-"*82)
    ch=int(input("Enter from above options:=> "))
    if ch==1:
        d={}
        roll_no=int(input("Enter your Roll No.:= "))
        name=input("Enter your name:= ")
        age=int(input("Enter your age:= "))
        city=input("Enter your city:= ")
        percentage=int(input("Enter your percentage:= "))
        d["Roll_no"]=roll_no
        d["Name"]=name
        d["Age"]=age
        d["City"]=city
        d["Percentage"]=percentage
        db[roll_no]=d
        
        print("-"*82)
    elif ch==2:
        print("-"*82)
        print("|{:^10}||{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format("Sr No.","Roll_No","Name","Age","City","Percentage"))
        print("-"*82)
        for i in db:
            print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(i,db[i]["Roll_no"],db[i]["Name"],db[i]["Age"],db[i]["City"],db[i]["Percentage"]))
            print("-"*82)
    elif ch==3:
        roll_no=int(input("Enter your Roll_no:=> "))
        print("""
                    1.Name
                    2.Age
                    3.City
                    4.Percentage   
        """)
        print("-"*82)
        c=int(input("Enter from the above options:=> "))
        print("-"*82)
        if c==1:
            updated_n=input("Enter your updated name:=> ")
            db[roll_no]["Name"]=updated_n
            print("Updated Name successfully")
        elif c==2:    
            updated_a=int(input("Enter your updated age:=> "))
            db[roll_no]["Age"]=updated_a
            print("Updated Age successfully")
        elif c==3:
            updated_c=input("Enter your updated city:=> ")
            db[roll_no]["City"]=updated_c
            print("Updated City successfully")
        elif c==4:
            updated_p=int(input("Enter your updated percentage:=> "))
            db[roll_no]["Percentage"]=updated_p
            print("Updated Percentage successfully")
        else:
            print("Invalid Option")
            print("-"*82)
    elif ch==4:
        roll_no=int(input("Enter roll number to delete details:=>  "))
        del db[roll_no]
        print("Details deleted successfully.")  
        print("*"*82)  
    c=input("Do you want to continue(Y/N):=> ")
    if c=="N":
            break

            
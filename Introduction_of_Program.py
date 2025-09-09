import time
import mysql.connector as con
def new_user():
    print("="*258)
    mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
    cur=mycon.cursor()
    F_name=input("\n\nEnter Your First Name:")
    while True:
        if F_name!="":
            M_name=input("\nEnter Your Middle Name(Please Enter if You Don't Have Any):")
            L_name=input("\nEnter Your Last Name(Please Enter if You Don't Have Any):")
            if M_name=="" and L_name=="":
                M_name=""
                L_name=""
                break
            elif M_name=="" and L_name!="":
                M_name=""
                break
            else:
                break
        else:
            F_name=input("\nPlease Enter Your First Name:")
    C_name=F_name+" "+M_name+" "+L_name
    E_mail=input("\nEnter Your email (In the form: user@____.com):")
    while True:
        if '@' and '.com' in E_mail:
            break
        else:
            E_mail=input("\nPlease Enter a correct Email(In the form: user@____.com):")
    No=int(input("\nEnter Your Mobile Number (In Digits:9999 XXXX XX):"))
    while True:
        if No>=1000000000 and No<=9999999999:
            break
        else:
            No=int(input("\nPlease Enter Correct Mobile Number (In Digits:9999 XXXX XX):"))
    username=input("\nEnter a username for Your profile:")
    c=0
    d=0
    e=0
    for i in username:
        if i.isalpha():
            c+=1
        elif i.isdigit():
            d+=1
        elif i=="":
            e=0
    while True:
        if c>1 and d>1 and e==0 and len(username)>4:
            break
        elif c>1 and e==0 and len(username)>4:
            break
        else:
            username=input("Enter a username that doesn't contain special characters and its length is greater than 4:")
    while True:
        qry="select Username from userid"
        cur.execute(qry)
        rs=cur.fetchall()
        found=False
        for i in rs:
            if i[0]==username:
                found=True
                username=input("\nPlease enter a unique username as this already exists in database:")
                break
        if not found:
                break
    password=input("\nEnter a unique password:")
    while True:
        x=0
        n=0
        c=0
        j=0
        for b in password:
            if b.isalpha():
                x+=1
            elif b.isdigit():
                c+=1
            elif b.isspace():
                n+=1
            else:
                j+=1
        if x>=1 and c>=1 and j>=1 and len(password)>=6 and n==0:
            print()
            break
        else:
            print("\nPassword is not valid.")
            print("Password Criterion:\n")
            print("1. Length of the password must be greater than 6")
            print("2. Must contain atleast one alphabet")
            print("3. Must contain atleast one numeric value")
            print("4. Must not contain any spaces")
            print("5. Must contain one special character")
            password=input("\nEnter the password again:")
    dob=input("\nEnter Your date of birth (Year-Month-Date:YYYY-MM-DD):")
    while True:
            if dob[0] in '12' and dob[1] in '98760' and dob[4]=="-" and dob[5] in '01' and dob[7]=="-" and len(dob)==10 and dob[8] in '0123':
                if dob[5] in '01' and dob[8] in '0123' and dob[9] in '1234567890':
                    break
                else:
                    dob=input("Please enter a correct date in the form(YYYY-MM-DD):")
            else:
                dob=input("Please enter a correct date in the form(YYYY-MM-DD):")
    qry="insert into userid values ('{0}','{1}',{2},'{3}','{4}','{5}')".format(C_name,E_mail,No,username,password,dob)
    cur.execute(qry)
    mycon.commit()
    mycon.close()
    cur.close()
    time.sleep(1.2)
    print("\n\n\t\t\t\t\tThank You for providing necessary information")
    time.sleep(0.5)
    print("\n\t\t\t\t\tHave A great experience with our software.......")
    return(username)
def old_user():
    print("\t\t\t\t\t\tHappy to see you back")
    print("="*258)
    mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
    cur=mycon.cursor()
    username=input("\nEnter your existing username:")
    while True:
        qry="select Username from userid"
        cur.execute(qry)
        rs=cur.fetchall()
        found=False
        for i in rs:
            if i[0]==username:
                found=True
                break
        if found:
            break
        else:
            username=input("\nPlease enter the username that you used earlier:")
    password=input("\nEnter the password:")
    k=0
    while k<2:
        qry="select Username,Login_password from userid"
        cur.execute(qry)
        rs=cur.fetchall()
        found=False
        for i in rs:
            if i[0]== username and i[1]== password:
                print("\n\t\t\t\t\t\tLoading.........")
                time.sleep(1.7)
                print("\n\t\t\t\t\t\tLogin is successfull")
                found=True
                break
        if found==True:
            break
        else:
            password=input("\nPlease enter the correct password:")
        k+=1
    if found==False:
        time
        print("\n\t\t\t\t\t\tSorry! Please try again Later")
        return("Incorrect username")
    mycon.commit()
    mycon.close()
    cur.close()
    return(username)

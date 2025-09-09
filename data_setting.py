#Data Export and Backup
import time
import mysql.connector as con
def settings(username):
    while True:
        print("\n\n▣▶▶◉1. Backup and Export data.")
        print("\n▣▶▶◉2. Delete your account.")
        print("\n▣▶▶◉3. Change your password.")
        print("\n▣▶▶◉4. Return back to main menu.")
        n=input("\n▶▶▶▶Choose the option from above(1-3):")
        if n in '1':
            print("\n\nLoading...Please Wait.............................\n")
            time.sleep(3)
            print("\nYour backup is completed")
            pp=input("Do you want to export all your data(Yes/No):")
            if pp in 'Yesyes':
                print("\nHere's your complete data..")
                mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
                cur=mycon.cursor()
                qr="show tables"
                cur.execute(qr)
                dd=cur.fetchall()
                l=[]
                for i in range(len(dd)):
                    if username in dd[i][0]:
                        l.append(dd[i][0])
                if f"{username}_plan_details" in l and f"{username}_daily_activity" in l:
                    print("\n\nDaily activity:\n")
                    time.sleep(1)
                    qry=f"select userid.Username, userid.FullName,{username}_plan_details.*,{username}_daily_activity.* from userid left join {username}_plan_details on userid.Username={username}_plan_details.Username left join {username}_daily_activity on userid.Username={username}_daily_activity.Username where userid.Username='{username}'"
                    cur.execute(qry)
                    rs=cur.fetchall()
                    for i in range(18):
                        b=rs[0][i]
                        if i==0:
                            print("\n Your username is:",b)
                            time.sleep(0.25)
                        elif i==1:
                            print("\n Name:  ",b)
                            time.sleep(0.25)
                        elif i==3:
                            print("\n Plan name chosen by you is : ",b)
                        elif i==4:
                            print("\n Description of the plan: ",b)
                        elif i==5:
                            print("\n Duration of per session class: ",b)
                        elif i==6:
                            print("\n Total number of months of the lasting of the plan:",b)
                        elif i==7:
                            print("\n Additional excersises that are needed to be performed are: ",b)
                            time.sleep(0.5)
                        else:
                            pass
                    print("\nDate \t\tDay \tTime_day \tActivity \tDuration \t\tCategory_act \tLevel \tCalorie \tAdditional_Info")
                    time.sleep(0.25)
                    for a in range(len(rs)):
                        for k in range(9,18):
                            if k==14:
                                b=rs[a][k]
                                print(b,end=' \t\t')
                            else:
                                b=rs[a][k]
                                print(b,end=' \t')
                            time.sleep(0.25)
                        print('\n')
                else:
                    print()
                mycon.commit()
                if f"{username}_goal" in l:
                    print("\n\nYour set Goals and achievements:")
                    time.sleep(1)
                    qry4=f"select * from {username}_goal"
                    cur.execute(qry4)
                    abc=cur.fetchall()
                    for i in range(1,7):
                        if i==1:
                            time.sleep(0.1)
                            print("\nGoal:: ",abc[0][1])
                            time.sleep(1)
                        elif i==2:
                            print("\nCurrent weight: ",abc[0][2]," kg")
                        elif i==3:
                            print("\nActual weight you want to achieve:",abc[0][3]," kg")
                        elif i==4:
                            print("\nAverage Running distance: ",abc[0][4]," km")
                        elif i==5:
                            print("\nWeight lifted by you(with repetitions):",abc[0][5]," kg")
                        elif i==6:
                            print("\nAchievement or success performance towards your goal is:",abc[0][6])
                        else:
                            break
                else:
                    print()
                print("\nFriends list:")
                time.sleep(1)
                qry=f"select C_Followers,C_Following from friend_connection where username='{username}'"
                cur.execute(qry)
                rs=cur.fetchall()
                if rs[0][0] not in '' and rs[0][1] not in '':
                    print("\nThe list of your Followers and Following as follows:\n")
                    time.sleep(1)
                    print("\nFull_Name\tFollowers\t\t\tFollowing")
                    follower=rs[0][0].split(',')
                    following=rs[0][1].split(',')
                    j=[]
                    if '' in follower:
                        follower.remove('')
                    if '' in following:
                        following.remove('')
                    for i in follower:
                        qry1=f"select fullname from friend_connection where username='{i}'"
                        cur.execute(qry1)
                        pc=cur.fetchall()
                        j.append(pc[0][0])
                    time.sleep(2)
                    for k in range(len(j)):
                        print(j[k],'\t',follower[k],'\t\t',following[k])
                else:
                    print("\nThere aren't any followers or following of your profile.\n")
                cur.close()
                mycon.close()
                print("\n\nPlease Download the following data..")
                time.sleep(1)
                a=input("\n\nPress enter to continue:")
            else:
                print()
        elif n in '2':
            print("\n\nAre you sure you want to delete your account...All your data will be completely cleared and you want be able to access it again.\n")
            time.sleep(2)
            r=input("\nPlease confirm (Yes/No):")
            while True:
                if r in 'yesYes':
                    pas=input("\nEnter your password once again correctly:")
                    mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
                    cur=mycon.cursor()
                    qry=f"select Login_password from userid where Username='{username}'"
                    cur.execute(qry)
                    f=cur.fetchall()
                    gg=f[0][0]
                    for i in range(1,3):
                        if pas==gg:
                            c=[]
                            qry11="show tables"
                            cur.execute(qry11)
                            rs=cur.fetchall()
                            for j in range(len(rs)):
                                c.append(rs[j][0])
                            for k in c:
                                if username in k:
                                    qry1=f"drop table {k}"
                                    cur.execute(qry1)
                                    mycon.commit()
                                else:
                                    pass
                            qry2=f"delete from userid where username='{username}'"
                            cur.execute(qry2)
                            mycon.commit()
                            qry3=f"select Follower,Follow,C_Followers from friend_connection where username='{username}'"
                            cur.execute(qry3)
                            dd=cur.fetchall()
                            aa=dd[0][0].split(',')
                            bb=dd[0][1].split(',')
                            cc=dd[0][2].split(',')
                            for tt in aa:
                                qry4=f"update friend_connection set Follow=replace(Follow,'{username}','') where username='{tt}'"
                                cur.execute(qry4)
                                mycon.commit()
                            for hh in bb:
                                qry5=f"update friend_connection set Follower=replace(Follower,'{username}','') where username='{hh}'"
                                cur.execute(qry5)
                                mycon.commit()
                            for ww in cc:
                                qry6=f"update friend_connection set C_Followers=replace(C_Followers,'{username}',''), C_Following=replace(C_Following,'{username}','') where username='{ww}'"
                                cur.execute(qry6)
                                mycon.commit()
                            qry7=f"delete from friend_connection where username='{username}'"
                            cur.execute(qry7)
                            mycon.commit()
                            print("\n\nYour complete data has been deleted")
                            time.sleep(0.2)
                            cur.close()
                            mycon.close()
                            break
                        else:
                            pas=input("\nEnter your password once again correctly:")
                    cur.close()
                    mycon.close()
                    break
                elif r in 'Nono':
                    print("\nYou decided not to delete your data.")
                    break
                else:
                    r=input("\n Please confirm correctly by typing (Yes/No):")
        elif n in '3':
            print("\n\nIn order to change your password please provide with some information.")
            mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
            cur=mycon.cursor()
            pas=input("\nEnter your current password:")
            qry=f"select Login_password from userid where username='{username}'"
            cur.execute(qry)
            rs=cur.fetchall()
            h=rs[0][0]
            for i in range(1,4):
                if pas ==h:
                    a=input("\nEnter a new password for your account:")
                    ff=pass_check(a)
                    qry1=f"update userid set Login_password='{ff}' where username='{username}'"
                    cur.execute(qry1)
                    mycon.commit()
                    print("\nYour new password has been updated.")
                    break
                else:
                    print("\nPassword not changed.")
                    pas=input("\nPlease enter your correct current password:")
            cur.close()
            mycon.close()
        elif n in '4':
            print("\n\t\t\t\t\t\tGetting back to main menu.")
            time.sleep(1.5)
            break
        elif h==1:
            break
        else:
            print("\n Please enter the choice from the following.")
def pass_check(password):
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
    return(password)

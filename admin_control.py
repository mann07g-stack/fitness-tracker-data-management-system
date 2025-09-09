import mysql.connector as con
import time
def admin_ask():
    name=input("\n\nↇↇ≊Enter your full name:")
    password=input("\n\nↇↇ≊Enter your password to access your database:")
    a='Mann Gupta mann gupta Mann gupta'
    b='mann_007'
    if name in a and password == b:
        admin_operations()
    else:
        print("\nYou are trying to be someone else..Please come back later.")
def admin_operations():
    print("\nIt's pleasure to see you here....Please check all the data and perform the task you want to...")
    print("\nHere's a complete list of data that your database contains....")
    time.sleep(1)
    print("\nLoading....")
    time.sleep(1)
    while True:
        print("\n\n⊠⊰⊰⊰1.See the list of all the users.")
        print("\n⊠⊰⊰⊰2.Select a particular user and see his/her complete stats.")
        print("\n⊠⊰⊰⊰3.See the mutual friends list completely.")
        print("\n⊠⊰⊰⊰4.Delete a User whom you think is misleading or fraud completely.")
        print("\n⊠⊰⊰⊰5.Send new notifications or updates of any upcoming events.")
        print("\n⊠⊰⊰⊰6.See all the events list that occured.")
        print("\n⊠⊰⊰⊰7.To exit the program.")
        n=input("\nEnter the number(1-7) of which task you want to perform:")
        if n in '1':
            mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
            cur=mycon.cursor()
            qry="select username,FullName,Login_password,DOB,Mobile_no,Email from userid"
            cur.execute(qry)
            rs=cur.fetchall()
            print("\nS.No.\tUsername\tFullName\tLogin Password\tDate_of_birth\tMobile no\tEmail Address")
            for i in range(1,len(rs)+1):
                print(i,end='\t')
                for j in rs[i-1]:
                    print(j,end='\t')
                time.sleep(0.05)
                print()
            print("\n\nThere is a complete list of all the users in your database above.....")
            time.sleep(3)
            cur.close()
            mycon.close()
        elif n in '2':
            mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
            cur=mycon.cursor()
            qry="select username from userid"
            cur.execute(qry)
            rs=cur.fetchall()
            us=[]
            for i in range(len(rs)):
                us.append(rs[i][0])
            print("\nUsernames are as follows:")
            for k in us:
                print(k)
            user=input("\nEnter the correct username whose data you want to see:")
            if user in us:
                qr="show tables"
                cur.execute(qr)
                dd=cur.fetchall()
                l=[]
                for i in range(len(dd)):
                    if user in dd[i][0]:
                        l.append(dd[i][0])
                if f"{user}_plan_details" in l and f"{user}_daily_activity" in l:
                    qry1=f"select userid.Username, userid.FullName,{user}_plan_details.*,{user}_daily_activity.* from userid left join {user}_plan_details on userid.Username={user}_plan_details.Username left join {user}_daily_activity on userid.Username={user}_daily_activity.Username where userid.Username='{user}'"
                    cur.execute(qry1)
                    rs=cur.fetchall()
                    for i in range(18):
                        b=rs[0][i]
                        if i==0:
                            print("\n Username is:",b)
                            time.sleep(0.25)
                        elif i==1:
                            print("\n Name:  ",b)
                            time.sleep(0.25)
                        elif i==3:
                            print("\n Plan name chosen is : ",b)
                        elif i==4:
                            print("\n Description of the plan: ",b)
                        elif i==5:
                            print("\n Duration of per session class: ",b)
                        if i==6:
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
                if f"{user}_goal" in l:
                    qry4=f"select * from {user}_goal"
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
                    print("\nHere's the complete data of the user as shown above.")
                    time.sleep(2)
                else:
                    print()
                mycon.close()
                cur.close()
            else:
                print("\nYou must have entered a wrong username that doesn't exist")
                time.sleep(0.2)
        elif n in '3':
            print("\nHere's a complete list of people their followers and following")
            mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
            cur=mycon.cursor()
            qry3="select Username,FullName,C_Followers,C_Following from friend_connection"
            cur.execute(qry3)
            rs=cur.fetchall()
            print("\nUsername\t\tFullName\t\tFollowers list\t\tFollowing List")
            for i in range(len(rs)):
                for j in rs[i]:
                    print(j,end="\t\t")
                print()
            time.sleep(3)
        elif n in '4':
            mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
            cur=mycon.cursor()
            qry="select username from userid"
            cur.execute(qry)
            rs=cur.fetchall()
            us=[]
            for i in range(len(rs)):
                us.append(rs[i][0])
            print("\nUsernames are as follows:")
            for k in us:
                print(k)
            user=input("\nEnter the username of the person whom you want to delete from the your database:")
            if user in us:
                c=[]
                qry11="show tables"
                cur.execute(qry11)
                rs=cur.fetchall()
                for j in range(len(rs)):
                    c.append(rs[j][0])
                for k in c:
                    if user in k:
                        qry1=f"drop table {k}"
                        cur.execute(qry1)
                        mycon.commit()
                    else:
                        pass
                qry2=f"delete from userid where username='{user}'"
                cur.execute(qry2)
                mycon.commit()
                qry3=f"select Follower,Follow,C_Followers from friend_connection where username='{user}'"
                cur.execute(qry3)
                dd=cur.fetchall()
                aa=dd[0][0].split(',')
                bb=dd[0][1].split(',')
                cc=dd[0][2].split(',')
                for tt in aa:
                    qry4=f"update friend_connection set Follow=replace(Follow,'{user}','') where username='{tt}'"
                    cur.execute(qry4)
                    mycon.commit()
                for hh in bb:
                    qry5=f"update friend_connection set Follower=replace(Follower,'{user}','') where username='{hh}'"
                    cur.execute(qry5)
                    mycon.commit()
                for ww in cc:
                    qry6=f"update friend_connection set C_Followers=replace(C_Followers,'{user}',''), C_Following=replace(C_Following,'{user}','') where username='{ww}'"
                    cur.execute(qry6)
                    mycon.commit()
                qry7=f"delete from friend_connection where username='{user}'"
                cur.execute(qry7)
                mycon.commit()
                print("\n\nThe complete data has been deleted")
                time.sleep(0.2)
            else:
                print("\nYou might have chosen a wrong username that doesn't exist in our database.")
            time.sleep(2)
        elif n in '5':
            print("\nLet's begin setting up a new event or schedule a new program for all the users who are our members.")
            name=input("\nEnter the complete name of the event that you are scheduling:")
            while True:
                if name!="":
                    break
                else:
                    name=input("Please enter a name to continue of the program:")
            while True:
                date_commence=input("\nEnter the date when it will start(YYYY-MM-DD):")
                while True:
                    if date_commence[0] in '12' and date_commence[1] in '90' and date_commence[4]=="-" and date_commence[5] in '01' and date_commence[7]=="-" and date_commence[8] in  '0321' and date_commence[9] in '0987654321':
                        break
                    else:
                        date_commence=input("Please enter a correct date in the form(YYYY-MM-DD):")
                break
            while True:
                date_over=input("\nEnter the date when the event will end(YYYY-MM-DD):")
                while True:
                    if date_over[0] in '12' and date_over[1] in '90' and date_over[4]=="-" and date_over[5] in '01' and date_over[7]=="-" and date_over[8] in  '0321' and date_over[9] in '0987654321':
                        break
                    else:
                        date_over=input("Please enter a correct date in the form(YYYY-MM-DD):")
                break
            timing=input("\nEnter the time duration of the event for each day:")
            while True:
                if timing.isdigit():
                    timing=int(timing)
                    break
                else:
                    timing=input("Please enter the correct duration:")
            start_time=input("\nEnter the time when the session of that event start(HH:MM):")
            while True:
                if start_time[0] in '021' and start_time[1] in '0987654321' and start_time[2] in ':' and start_time[3] in '0123456' and start_time[4] in '0987654321':
                    if int(start_time[:2])>=0 and int(start_time[:2])<=12 and  int(start_time[3:])>=0 and  int(start_time[3:])<=59:
                        start_time=start_time +"a.m."
                        break
                    elif int(start_time[:2])>12 and int(start_time[:2])<24 and  int(start_time[3:])>=0 and  int(start_time[3:])<=59:
                        start_time=start_time + "p.m."
                        break
                    else:
                        start_time=input("Please enter a correct time of the day(HH:MM):")
                else:
                    start_time=input("Please enter a correct time of the day(HH:MM):")
            description=input("\nEnter the description and necessary details other than given to the users:")
            while True:
                if description!="":
                    break
                else:
                    description=input("Please enter a description in order to continue (atleast some details related to acrtivity)")
            tim=f"From: {start_time}, Duration: {timing}"
            mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
            cur=mycon.cursor()
            qry=f"insert into events_and_programs values('{name}','{date_commence}','{date_over}','{tim}','{description}')"
            cur.execute(qry)
            mycon.commit()
            print("\n\nYou have successfully provided a event for your users.")
            print("\nHere's a detailed overlook of the event.")
            time.sleep(1)
            print("\n\nA new event is on your way...to achieve a more synchronised and healthy life.")
            qry1="select * from events_and_programs"
            cur.execute(qry1)
            rsa=cur.fetchall()
            for i in range(5):
                if i==0:
                    print("\nEvent name: ",rsa[-1][0])
                elif i==1:
                    print("\nDate of starting of the event:",rsa[-1][1])
                elif i==2:
                    print("\nLast date of theevent:",rsa[-1][2])
                elif i==3:
                    print("\nTimings of the event:",rsa[-1][3])
                elif i==4:
                    print("\nDescription and necessary details:",rsa[-1][4])
                else:
                    pass
            time.sleep(3)
            cur.close()
            mycon.close()
        elif n in '6':
            print("\nThe complete list of the programs as follows:")
            mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
            cur=mycon.cursor()
            qry1="select * from events_and_programs"
            cur.execute(qry1)
            rsa=cur.fetchall()
            for j in range(len(rsa)):
                for i in range(5):
                    if i==0:
                        print("\nEvent name: ",rsa[j][0])
                    elif i==1:
                        print("\nDate of starting of the event:",rsa[j][1])
                    elif i==2:
                        print("\nLast date of theevent:",rsa[j][2])
                    elif i==3:
                        print("\nTimings of the event:",rsa[j][3])
                    elif i==4:
                        print("\nDescription and necessary details:",rsa[j][4])
                    else:
                        pass
                print()
            print("\n\nThe list ends here.....")
            time.sleep(3)
            cur.close()
            mycon.close()
        elif n in '7':
            print("\nExiting from the program....")
            time.sleep(1)
            break
        else:
            print("\nPlease enter the correct choice from (1-7)")


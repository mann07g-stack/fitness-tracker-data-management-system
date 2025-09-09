#Activity Logging
#Create Your own activity logging table for each day
import time
import mysql.connector as con
def check_table_existence(username):
    global y
    global z
    mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
    cur=mycon.cursor()
    qry='show tables'
    cur.execute(qry)
    rs=cur.fetchall()
    for i in rs:
        if i[0]==username+"_daily_activity":
            y=username
            break
        else:
            y=""
    z=username
    cur.close()
    mycon.close()
    return(y,z)
def table_creation_new(z):
    mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
    cur=mycon.cursor()
    time.sleep(1)
    print("\nIt seems like you don't have any daily data record.")
    time.sleep(0.3)
    a=input("Do You want to create a daily data record for yourself(Yes/No):")
    if a in 'Yesyes':
        time.sleep(1)
        print("\n\n Start your daily tracking record by giving these data as follows:")
        time.sleep(0.4)
        qry=f"create table {z}_daily_activity(Username varchar(30),Date_done date,Day varchar(9),Time_of_day varchar(10),Activity varchar(20),Duration varchar(13),Category varchar(40),Level varchar(10),Calories varchar(7),Additional_Thing varchar(500), foreign key(Username) references userid(Username))"
        cur.execute(qry)
        mycon.commit()
        mycon.close()
        cur.close()
        while True:
            input_values(z)
            ch=input("Do you want to add more data(Yes/No):")
            if ch not in 'Yesyes':
                break
            else:
                continue
        return('YES')
    else:
        return('NO')
def input_values(username):
    mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
    cur=mycon.cursor()
    while True:
        date_done=input("\nEnter the date on which you performed the activity(YYYY-MM-DD):")
        while True:
            if date_done[0] in '12' and date_done[1] in '90' and date_done[4]=="-" and date_done[5] in '01' and date_done[7]=="-" and len(date_done)==10:
                if date_done[5] in '0':
                    break
                elif date_done[5] in '1' and date_done[6] in '120':
                    break
                else:
                    date_done=input("Please enter a correct date in the form(YYYY-MM-DD):")
            else:
                date_done=input("Please enter a correct date in the form(YYYY-MM-DD):")
        break
    day=input("\nEnter the day (Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday):")
    while True:
        if day.lower() in 'monday,tuesday,wednesday,thursday,friday,saturday,sunday':
            break
        else:
            day=input("Please Enter a correct day(Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday):")
    time_day=input("\nEnter the time of the day(HH:MM):")
    while True:
        if time_day[0] in '021' and time_day[1] in '0987654321' and time_day[2] in ':' and time_day[3] in '0123456' and time_day[4] in '0987654321':
            if int(time_day[:2])>=0 and int(time_day[:2])<=12 and  int(time_day[3:])>=0 and  int(time_day[3:])<=59:
                time_day=time_day +"a.m."
                break
            elif int(time_day[:2])>12 and int(time_day[:2])<24 and  int(time_day[3:])>=0 and  int(time_day[3:])<=59:
                time_day=time_day + "p.m."
                break
            else:
                time_day=input("Please enter a correct time of the day(HH:MM):")
        else:
            time_day=input("Please enter a correct time of the day(HH:MM):")
    activity=input("\nEnter the activity or excercise name that you performed(Cycling/Running/Swimming/Dancing/Yoga/Gym/etc.):")
    while True:
        if activity!="":
            break
        else:
            activity=input("Please Enter the activity to continue:")
    duration=input("\nEnter the time duration for which you performed the excercise(in minutes):")
    while True:
        if duration.isdigit():
            duration=int(duration)
            hr=duration//60
            minutes=duration%60
            t_duration=str(hr)+"Hrs."+" "+str(minutes)+"Min."
            break
        else:
            duration=input("Enter the time correctly please in numbers:")
    category=input("\nEnter the category or target muscle groups (e.g., cardio, strength) if applicable else press enter:")
    while True:
        if len(category)<40:
            break
        else:
            category=input("Please enter a valid category that the excercise belongs to(e.g., cardio, strength):")
    level=input("\nEnter the difficulty level that you choose(Hard,Moderate,Easy):")
    while True:
        if level.lower() in 'hardmoderateeasy':
            break
        else:
            level=input("Enter the level of your efforts correctly(Hard,Moderate,Easy):")
            break
    calories=input("\nEnter the calories you burnt (If known in calories):")
    if calories.isdigit():
        print()
    else:
        calories=""
    Additional=input("\nEnter any additional relevant information that you want to share along with the above information(If necessary else enter to continue):")
    qry=f"insert into {username}_daily_activity values('{username}','{date_done}','{day}','{time_day}','{activity}','{t_duration}','{category}','{level}','{calories}','{Additional}')"
    cur.execute(qry)
    mycon.commit()
    cur.close()
    mycon.close()
def Add_modify_old(username):
    print("\n\n**********************************************************Happy to see you********************************************************")
    print("\n\t\t\t\t\t       Select the option that you want to perform")
    while True:
        print("\n------------>1. Want to add a new excercise details performed by you.")
        print("------------>2. Want to see your progress and your records.")
        print("------------>3. Want to change any value or update any data(like date or activity name etc.) fed by you.")
        print("------------>4. Want to remove the data permanently from our database.")
        print("------------>5. If you have completed the necessary operations or don't want to do any.")
        ch=input("\nEnter the number next to the task that you want to perform on your daily activity data:")
        if ch in '1':
            input_values(username)
            print("\n\t\t\t\t\t       The values are added successfully in your record.")
        elif ch in '2':
            a=input("\nDo you want to see complete record with plan or not(Yes/No):")
            if a in 'Yesyes':
                mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
                cur=mycon.cursor()
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
                            print(rs[a][k],end=' \t\t')
                        else:
                            print(rs[a][k],end=' \t')
                        time.sleep(0.25)
                    print('\n')
                mycon.commit()
                cur.close()
                mycon.close()
                time.sleep(3)
                print('\n\n')
            elif a in 'Nono':
                while True:
                    print("\n## 1. See your complete plan that you selected for yourself")
                    print("\n## 2. See the daily activity the fields will be chosen by you")
                    choice2=input("\nEnter the digit that you want to see:")
                    if choice2 in '1':
                        mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
                        cur=mycon.cursor()
                        qry1=f"select * from {username}_plan_details"
                        cur.execute(qry1)
                        ak=cur.fetchall()
                        for l in range(5):
                            b=ak[0][l]
                            if l==0:
                                print("\n Your username is:",b)
                                time.sleep(0.25)
                            elif l==1:
                                print("\n Plan name chosen by you is : ",b)
                                time.sleep(0.25)
                            elif l==2:
                                print("\n Description of the plan: ",b)
                                time.sleep(0.25)
                            elif l==3:
                                print("\n Duration of per session class: ",b)
                                time.sleep(0.25)
                            elif l==4:
                                print("\n Total number of months of the lasting of the plan:",b)
                                time.sleep(0.25)
                            elif l==5:
                                print("\n Additional excersises that are needed to be performed are: ",b)
                                time.sleep(0.5)
                            else:
                                break
                        import Plan
                        Plan.schedule()
                        print('\n\n')
                        
                    elif choice2 in '2':
                        q=input("Enter the fields that you want to see of your daily activity(Date/Day/Time/Activity/Duration/Category/Level/Calories/Additional Information):")
                        tt=q.split()
                        na=""
                        for o in tt:
                            if o.lower() in 'date':
                                na+="Date_done,"
                            elif o.lower() in 'day':
                                na+="Day,"
                            elif o.lower() in 'time':
                                na+="Time_of_day,"
                            elif o.lower() in 'activity':
                                na+="Activity,"
                            elif o.lower() in "duration":
                                na+="Duration,"
                            elif o.lower() in "category":
                                na+="Category,"
                            elif o.lower() in "level":
                                na+="Level,"
                            elif o.lower() in "calories":
                                na+="Calories,"
                            elif o.lower() in "additional information additionalinformation":
                                na+="Additional_Thing,"
                            else:
                                pass
                        na=na[:-1]
                        mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
                        cur=mycon.cursor()
                        qry3=f"select {na} from {username}_daily_activity"
                        cur.execute(qry3)
                        ba=cur.fetchall()
                        ca="Date,Day,Time,Activity,Duration,Category,Level,Calories,Additional Information"
                        ma = ""
                        ca = ca.split(',')
                        na = na.split(',')
                        for l in range(len(na)) :
                            ha=na[l]
                            if ha in "Additional_Thing":
                                ma+="Additional Information\t"
                            else:
                                for k in range(len(ca)):
                                        if ca[k] in na[l]:
                                            ma+=ca[k]+"\t\t"
                        print('\n\nNo.\t',ma)
                        for g in range(1,len(ba)+1):
                            print('\n',g,end='\t')
                            for tt in range(len(ba[0])):
                                print(ba[g-1][tt],end='\t')
                            print('\n')
                        print('\n\n')
                    break
                mycon.commit()
                cur.close()
                mycon.close()
            else:
                a=input("\nDo you want to see complete record with plan or not(Yes/No):")
        elif ch in '3':
            r=input("\nEnter your choice of data that you want to update[ONLY ONE](Date/Day/Time/Activity/Duration/Category/Level/Calories/Additional Information):")
            b=input("\nEnter the new value that you want to assign to it:")
            c=input("\nIf you want to apply condition type yes else enter:")
            ca=""
            r=r.lower()
            na = "date_done,day,time_of_day,activity,duration,category,level,calories,additional_thing"
            na=na.split(',')
            for k in range(len(na)):
                if r in na[k]:
                    ca += na[k]
                    break
                elif "additional information" in r:
                    ca+=na[8]
                    break
                else:
                    continue
            if c=='YES' or c=='yes' or c=='Yes':
                q=input("Enter the category of the data that you want to select(Date/Day/Time/Activity/Duration/Category/Level/Calories/Additional Information):")
                t=input("Enter the value that you assigned to that category:")
                na = "date_done,day,time_of_day,activity,duration,category,level,calories,additional_thing"
                q=q.lower()
                na=na.split(',')
                ba=""
                for i in range(len(na)):
                    if q in na[i]:
                        ba += na[i]
                        break
                    elif "additional information" in q:
                        ba+=na[8]
                        break
                    else:
                        continue
                mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
                cur=mycon.cursor()
                qry9=f"update {username}_daily_activity set {ca}='{b}' where {ba}='{t}'"
                cur.execute(qry9)
                mycon.commit()
                mycon.close()
                cur.close()
                print("\nThe update has been successfull...returning back")
            else:
                mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
                cur=mycon.cursor()
                qry10=f"update {username}_daily_activity set {ca}='{b}'"
                cur.execute(qry10)
                mycon.commit()
                mycon.close()
                cur.close()
                print("\nThe update has been successfull...returning back")
        elif ch in '4':
            while True:
                print("\n>>>1. If you want to erase the complete activity data that you were maintaining each day.")
                print("\n>>>2. If you want to remove specific data in the record.")
                print("\n>>>3. If you don't want to go further.")
                choice4=input("\nEnter your choice that you want to perform:")
                if choice4 in '1':
                    mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
                    cur=mycon.cursor()
                    qry5=f"delete from {username}_daily_activity"
                    cur.execute(qry5)
                    mycon.commit()
                    mycon.close()
                    cur.close()
                    time.sleep(1)
                    print("\n\nYour complete data of daily activities has been deleted.\n")
                elif choice4 in '2':
                    while True:
                        print("\n\n||1. If you want to delete a specific value from records.")
                        print("\n||2.If you want to delete the complete record for given condition.")
                        ch3=input("\nEnter the choice that you want to proceed with:")
                        if ch3 in '1':
                            p=input("\nSelect the criterion that you want to choose(Date/Day/Time/Activity/Duration/Category/Level/Calories/Additional Information):")
                            d=input("\nEnter its value that you want to remove(eg:Monday if Day is chosen):")
                            na = "date_done,day,time_of_day,activity,duration,category,level,calories,additional_thing"
                            na=na.split(',')
                            p=p.lower()
                            ba=""
                            for i in range(len(na)):
                                if p in na[i]:
                                    ba += na[i]
                                    break
                                elif "additional information" in p:
                                    ba+=na[8].lower()
                                    break
                                else:
                                    continue
                            mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
                            cur=mycon.cursor()
                            qry6=f"update {username}_daily_activity set {ba}=Null where {ba}='{d}'"
                            cur.execute(qry6)
                            mycon.commit()
                            mycon.close()
                            cur.close()
                            print("\nYour data has been modified\n")
                            break
                        elif ch3 in '2':
                            p=input("\nSelect the criterion that you want to choose for deletion(Date/Day/Time/Activity/Duration/Category/Level/Calories/Additional Information):")
                            d=input("\n Enter the value of the criterion chosen(eg:Monday if Day is chosen):")
                            na = "date_done,day,time_of_day,activity,duration,category,level,calories,additional_thing"
                            na=na.split(',')
                            p=p.lower()
                            ba=""
                            for i in range(len(na)):
                                if p in na[i]:
                                    ba += na[i]
                                    break
                                elif "additional information" in p:
                                    ba+=na[8]
                                    break
                                else:
                                    continue
                            mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
                            cur=mycon.cursor()
                            qry6=f"delete from {username}_daily_activity where {ba}='{d}'"
                            cur.execute(qry6)
                            mycon.commit()
                            mycon.close()
                            cur.close()
                            print(f"\nThe rows containing {d} are deleted successfully.\n")
                            break
                        else:
                            print("\nPlease Enter a valid choice to proceed")
                elif choice4 in '3':
                    print("\nAlright getting back to the page...")
                    print("\n\t\t\t\t\t\t      Loading.......")
                    time.sleep(1.1)
                    break
                else:
                    print("\n\nEnter a valid choice from the following:\n")
        elif ch in '5':
            time.sleep(0.3)
            print("\n\n\t\t\t\t\tAll the operations are done....Getting back to the main menu.")
            break
        else:
            time.sleep(1)
            print("\n\n\t\t\t\t\t||Please Give the right command in order to continue||\n")

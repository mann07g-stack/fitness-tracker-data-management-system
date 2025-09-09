import time
import datetime
import mysql.connector as con
import Introduction_of_Program as intro
import Plan
import New_Plan_Input
import goal_setting
import friends
import data_setting
import admin_control
import Activity_each_day
def welcome():
    print("\n\n")
    time.sleep(0.4)
    print("\t\t\t\t\t\t\tFITNESS TRACKER")
    print("\n\t\t\t\t\t\t        Welcome to Fitness Tracker")
    time.sleep(0.6)
    print("\n\t\t\t'Fitness is not about being better than someone else; it's about being better than you used to be.'")
    current_date=datetime.datetime.now().date()
    current_time=datetime.datetime.now().time()
    time.sleep(1)
    print("\n Date:{} \t\t\t\t\t\t\t\t\t\t\t     Time:{}".format(current_date,current_time))
def start():
    print("\n\nHello I am here to assist you.Let's aim towards a collective healthy and wealthy life of all.\n")
    time.sleep(2)
    while True:
        print("\n₪⫸⫸⫸1. SIGN UP or ENROLL")
        print("\n₪⫸⫸⫸2. SIGN IN or LOGIN IN")
        print("\n₪⫸⫸⫸3. ADMIN")
        print("\n₪⫸⫸⫸4. EXIT THE FITNESS TRACKER")
        m1=input("\nEnter the choice that you want to go with:")
        if m1 in '1':
            new=intro.new_user()
            friends.user_follow_following_new_user_insertion(new)
            plan_name,t_money_paid=Plan.workout_plan()
            New_Plan_Input.sub_table(new,plan_name,t_money_paid)
            while True:
                print("\n◉1. Daily Activities data record.")
                print("◉2. Set Goal for yourself.")
                print("◉3. Connect with your Friends.")
                print("◉4. Go to Settings")
                print("◉5. Exit the FITNESS TRACKER")
                n=input("\nEnter any choice you want to:")
                if n in '1':
                    a,b=Activity_each_day.check_table_existence(new)
                    if a=="" and b!="":
                        d=Activity_each_day.table_creation_new(b)
                        if d in 'NO':
                            print()
                        else:
                            Activity_each_day.Add_modify_old(new)
                elif n in '2':
                    goal_setting.goal_setting_achievement(new)
                elif n in '3':
                    friends.follow_following(new)
                elif n in '4':
                    print("\nSince you are new you can't go to settings for the first time..Afterwhile you can go easily...")
                    print("\nThank you for cooperating")
                    time.sleep(0.4)
                elif n in '5':
                    break
                else:
                    print("\nPlease choice correctly.")
            break
        elif m1 in '2':
            old=intro.old_user()
            if old!='Incorrect username':
                while True:
                    print("\n\n⟭•••⁍⁍⁍⁍⁑1. Daily Activities data record")
                    print("⟭•••⁍⁍⁍⁍⁑2. Goals and Achievements")
                    print("⟭•••⁍⁍⁍⁍⁑3. Plan details")
                    print("⟭•••⁍⁍⁍⁍⁑4. Friend List on FITNESS TRACKER")
                    print("⟭•••⁍⁍⁍⁍⁑5. Upcoming events and Updates")
                    print("⟭•••⁍⁍⁍⁍⁑6. Settings")
                    print("⟭•••⁍⁍⁍⁍⁑7. Get back to Login Page")
                    choices=input("\nSelect the number alongside to go to following pages given above:")
                    if choices in '1':
                        c,d=Activity_each_day.check_table_existence(old)
                        if c=="" and d!="":
                            z=Activity_each_day.table_creation_new(old)
                            if z in 'NO':
                                print()
                            else:
                                Activity_each_day.Add_modify_old(old)
                        else:
                            Activity_each_day.Add_modify_old(old)
                    elif choices in '2':
                        goal_setting.goal_setting_achievement(old)
                    elif choices in '3':
                        while True:
                            print("\n\n1. View your plan details.")
                            print("\n2. Change your plan and cancel this existing plan.")
                            print("\n3. Return to the main menu.")
                            aaa=input("Enter the choice from (1-3):")
                            if aaa in '1':
                                mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
                                cur=mycon.cursor()
                                qry=f"select * from {old}_plan_details"
                                cur.execute(qry)
                                rs=cur.fetchall()
                                for i in range(6):
                                    b=rs[0][i]
                                    if i==0:
                                        print("\n Your username is:",b)
                                        time.sleep(0.25)
                                    elif i==1:
                                        print("\n Plan name chosen by you is : ",b)
                                    elif i==2:
                                        print("\n Description of the plan: ",b)
                                    elif i==3:
                                        print("\n Duration of per session class: ",b)
                                    elif i==4:
                                        print("\n Total number of months of the lasting of the plan:",b)
                                    elif i==5:
                                        print("\n Additional excersises that are needed to be performed are: ",b)
                                        time.sleep(0.5)
                                    else:
                                        pass
                                cur.close()
                                mycon.close()
                            elif aaa in '2':
                                mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
                                cur=mycon.cursor()
                                qry1=f"drop table {old}_plan_details"
                                cur.execute(qry1)
                                mycon.commit()
                                cur.close()
                                mycon.close()
                                plan_name,t_money_paid=Plan.workout_plan()
                                New_Plan_Input.sub_table(old,plan_name,t_money_paid)
                                print("\nNew plan has been set for you")
                            elif aaa in '3':
                                print("\nReturning to main menu.....")
                                break
                            else:
                                print("\nPlease enter the correct value from (1-3)")
                    elif choices in '4':
                        friends.follow_following(old)
                    elif choices in '5':
                        time.sleep(1)
                        mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
                        cur=mycon.cursor()
                        qry1="select * from events_and_programs"
                        cur.execute(qry1)
                        rsa=cur.fetchall()
                        if rsa!=[]:
                            print("\n\nA new event is on your way...to achieve a more synchronised and healthy life.")
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
                        else:
                            print("\nEvents list seems to be empty.")
                            time.sleep(0.3)
                            continue
                        cur.close()
                        mycon.close()
                    elif choices in '6':
                        data_setting.settings(old)
                    elif choices in '7':
                        break
                    else:
                        print("\nPLease enter the choices from the following.")
            else:
                break
        elif m1 in '3':
            admin_control.admin_ask()
            break
        elif m1 in '4':
            print()
            break
        else:
            print("\nPlease Enter a correct choice from the following.")
    print("\nThanks for visiting FITNESS TRACKER...It's a pleasure having you here.")
    print("\n\n'Some People Want It To Happen, Some Wish It Would Happen, Others Make It Happen..'")
    time.sleep(2)
    print("\n\nHope to see you again..")

welcome()
start()

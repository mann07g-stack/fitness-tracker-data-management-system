#Goal setting and achievement
import mysql.connector as con
import time
def goal_setting_achievement(username):
    ab=0
    mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
    cur=mycon.cursor()
    qry="show tables"
    cur.execute(qry)
    rs=cur.fetchall()
    sss=f"{username}_goal"
    for i in range(len(rs)):
        if rs[i][0]==sss:
            ab=1
            while True:
                print("\n⟫⟫⟫⟫1. Want to see your goal and achievement.")
                print("\n⟫⟫⟫⟫2. Want to update the goal that you set up.")
                print("\n⟫⟫⟫⟫3. To return to the main menu.")
                ch1=input("\nEnter your choice from the above:")
                if ch1 in '1':
                    qry4=f"select * from {username}_goal"
                    cur.execute(qry4)
                    abc=cur.fetchall()
                    print('\n')
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
                            pass
                    print('\n\n')
                elif ch1 in '2':
                    goal,C_weight,T_weight,Running,Weight_lift,Endurance=goals_progress(username)
                    qry5=f"delete from {username}_goal"
                    cur.execute(qry5)
                    mycon.commit()
                    qry6=f"insert into {username}_goal values('{username}','{goal}',{C_weight},{T_weight},{Running},{Weight_lift},'{Endurance}')"
                    cur.execute(qry6)
                    mycon.commit()
                    print("\nYour goal has been updated successfully.")
                elif ch1 in '3':
                    print("\nReturning to the main menu...Will see you again")
                    break
                else:
                    print("\nPlease Enter a valid choice given as followed.\n")
                                
    if ab==0:
        print("\nYou haven't started setting up your goals")
        b=input("Do you want to start set up with your first goal (Yes/No):")
        if b in 'Yesyes':
            qry1=f"create table {username}_goal (Username varchar(30),Goal varchar(100),Current_weight int,Target_weight int, Run_distance int,Weight_lift int,Endurance varchar(50), foreign key(Username) references userid(Username))"
            cur.execute(qry1)
            mycon.commit()
            goal,C_weight,T_weight,Running,Weight_lift,Endurance=goals_progress(username)
            qry2=f"insert into {username}_goal values('{username}','{goal}',{C_weight},{T_weight},{Running},{Weight_lift},'{Endurance}')"
            cur.execute(qry2)
            mycon.commit()
            print("\nYour data is stored and the analysis as follows:\n")
            time.sleep(1.4)
            qry3=f"select * from {username}_goal"
            cur.execute(qry3)
            ab=cur.fetchall()
            for i in range(1,7):
                if i==1:
                    time.sleep(0.1)
                    print("\nGoal:: ",ab[0][1])
                    time.sleep(1)
                elif i==2:
                    print("\nCurrent weight: ",ab[0][2]," kg")
                elif i==3:
                    print("\nActual weight you want to achieve:",ab[0][3]," kg")
                elif i==4:
                    print("\nAverage Running distance: ",ab[0][4]," km")
                elif i==5:
                    print("\nWeight lifted by you(with repetitions):",ab[0][5]," kg")
                elif i==6:
                    print("\nAchievement or success performance towards your goal is:",ab[0][6])
                else:
                    pass
            time.sleep(3)
            print("\n\nGetting back to main menu........\n")
        else:
            time.sleep(0.3)
            print("\nReturning to main menu....Hope to see you again\n")
            time.sleep(0.36)
    mycon.close()
    cur.close()
def goals_progress(username):
    print("\nIt's nice to see you.....Let's set up your goals for maintaining a healthy life")
    goal=input("\n\nEnter your goal that you want to achieve(like: Improve my core,Work on muscles etc.):")
    while True:
        c=0
        for i in range(len(goal)):
            c+=1
        if c>=100:
            print("\n Please enter only the main goal in 4-8 words")
            goal=input("Enter the goal in less than few words(like: Improve my core,Work on muscles etc.):")
        else:
            break
    C_weight=input("\nEnter your current weight in kgs:")
    while True:
        if C_weight.isdigit():
            if int(C_weight)<200:
                C_weight=int(C_weight)
                break
            else:
                C_weight=input("\nEnter your correct current weight in kgs:")
        else:
            C_weight=input("\nEnter your correct current weight in kgs:")
    T_weight=input("\nEnter your target weight in kgs:")
    while True:
        if T_weight.isdigit():
            if int(T_weight)<110:
                T_weight=int(T_weight)
                break
            else:
                T_weight=input("\nEnter the correct target weight in kgs:")
        else:
            T_weight=input("\nEnter the correct target weight in kgs:")
    Running=input("\nEnter the distance that you run usually(in km):")
    while True:
        if Running.isdigit():
            Running=int(Running)
            break
        elif Running in "":
            Running=0
            break
        else:
            Running=input("\nEnter the distance correctly that you run usually(in km):")
    Weight_lift=input("\nEnter the weight that you lift usually(in kg):")
    while True:
        if Weight_lift.isdigit():
            Weight_lift=int(Weight_lift)
            break
        elif Weight_lift in "":
            Weight_lift=0
            break
        else:
            Weight_lift=input("\nEnter the correct weight that you lift usually(in kg):")
    timing=input("\nEnter the duration approximately that you give to running and weigh_lift combined:")
    while True:
        if timing.isdigit():
            timing=int(timing)
            break
        else:
            timing=input("\nPlease enter the duration correctly that you give to running and weigh_lift combined:")
    Exertion= input("\nEnter the rate of Percieved Exertion by you: ")
    while True:
        if Exertion.isdigit():
            if int(Exertion)>=1 and int(Exertion)<=10:
                Exertion=int(Exertion)
                break
            elif Exertion in "":
                Exertion=1
                break
            else:
                print('\nConditions:')
                print('\n1. Exertion must be from 1 to 10')
                print('\n2. If exertion is 1 that means you felt easy to perform the running and weight lifting')
                print('\n3. If exertion is 10 that means you felt hard to perform the running and weight lifting')
                Exertion= input("\n Enter the correct rate of Perceived Exertion by you as per the conditions:")
        else:
            Exertion=input("Please enter the digits correctly")
    Endurance=""
    while True:
        if Running>=10 and Weight_lift>=25 and Exertion>=8 and timing>=4:
            Endurance="You are perfoming excellent"
        elif Running<=10 and Running>=5 and Weight_lift>=15 and Weight_lift<25 and Exertion>=4 and Exertion<=7 and timing>=3:
            Endurance="You are doing great..Start pushing yourself more"
        elif Running<=4 and Running>=1 and Weight_lift>=7 and Weight_lift<=14 and Exertion>=2 and Exertion<=6 and timing>=1.4:
            Endurance="Start boosting up your Running distance"
        elif Running<1 and Weight_lift<7 and Exertion<=3 and timing<=1:
            Endurance="You are much behind to your desired goal"
        elif Running==0 and Weight_lift>=15 and Exertion>=6.5 and timing>=2:
            Endurance="Start Running for half-hour,increase performance"
        elif Weight_lift<=5 and Running>=8 and Exertion>=5 and timing>=1.2:
            Endurance="Nice performance.Keep it up"
        else:
            Endurance="You need to improve"
        break
    return(goal,C_weight,T_weight,Running,Weight_lift,Endurance)

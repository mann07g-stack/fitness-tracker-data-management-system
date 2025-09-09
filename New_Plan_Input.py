import mysql.connector as con
def sub_table(new,plan_name,money_paid):
    mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
    cur=mycon.cursor()
    if plan_name=='Cardio Blast':
        no_months=money_paid//9.99
        qry=f'create table {new}_plan_details(Username varchar(30),Plan_name varchar(20),Description varchar(100),Duration_min_session int,Time_Period_month int,Excersises varchar(500), foreign key(Username) references userid(Username))'
        qry1="insert into {0}_plan_details values('{1}','{2}','Improve cardiovascular health and burn calories',30,{3},'Jumping Jacks,High Knees,Burpees,Running,Jump Rope')".format(new,new,plan_name,no_months)
        cur.execute(qry)
        cur.execute(qry1)
        mycon.commit()
        mycon.close()
        cur.close()
        
    elif plan_name=='Strength Builder':
        no_months=money_paid//12.99
        qry=f'create table {new}_plan_details(Username varchar(30),Plan_name varchar(20),Description varchar(100),Duration_min_session int,Time_Period_month int,Excersises varchar(500), foreign key(Username) references userid(Username))'
        qry1="insert into {0}_plan_details values('{1}','{2}','Build muscle strength and endurance',30,{3},'Squats,Push-ups,Lunges,Dumbbell Rows,Plank')".format(new,new,plan_name,no_months)
        cur.execute(qry)
        cur.execute(qry1)
        mycon.commit()
        mycon.close()
        cur.close()
        
    elif plan_name=='Flexibility Flow':
        no_months=money_paid//7.99
        qry=f'create table {new}_plan_details(Username varchar(30),Plan_name varchar(20),Description varchar(100),Duration_min_session int,Time_Period_month int,Excersises varchar(500), foreign key(Username) references userid(Username))'
        qry1="insert into {0}_plan_details values('{1}','{2}','Improve flexibility, mobility, and relaxation through stretching',30,{3},'Cat-Cow Stretch,Forward Fold,Standing Quad Stretch,Childs Pose,SeatedSpinalTwist')".format(new,new,plan_name,no_months)
        cur.execute(qry)
        cur.execute(qry1)
        mycon.commit()
        mycon.close()
        cur.close()
        
    elif plan_name=='Core Crusher':
        no_months=money_paid//10.99
        qry=f'create table {new}_plan_details(Username varchar(30),Plan_name varchar(20),Description varchar(100),Duration_min_session int,Time_Period_month int,Excersises varchar(500), foreign key(Username) references userid(Username))'
        qry1="insert into {0}_plan_details values('{1}','{2}','Improve stability, posture, and overall core strength',30,{3},'Bicycle Crunches,Plank with shouldertaps,Russian Twists,Leg Raises,Superman Pose')".format(new,new,plan_name,no_months)
        cur.execute(qry)
        cur.execute(qry1)
        mycon.commit()
        mycon.close()
        cur.close()
        
    elif plan_name=='TotalBodyTune-Up':
        no_months=money_paid//14.99
        qry=f'create table {new}_plan_details(Username varchar(30),Plan_name varchar(20),Description varchar(100),Duration_min_session int,Time_Period_month int,Excersises varchar(500), foreign key(Username) references userid(Username))'
        qry1="insert into {0}_plan_details values('{1}','{2}','Full-body workout, enhancing strength and endurance',30,{3},'Jump Squats,Push-Ups,Bent-Over Rows,Mountain Climbers,Dumbbell Lunges')".format(new,new,plan_name,no_months)
        cur.execute(qry)
        cur.execute(qry1)
        mycon.commit()
        mycon.close()
        cur.close()
        
    else:
        print()
    


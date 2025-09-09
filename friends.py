import time
import mysql.connector as con
def user_follow_following_new_user_insertion(username):
    mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
    cur=mycon.cursor()
    qry=f"select FullName from userid where Username='{username}'"
    cur.execute(qry)
    rs=cur.fetchall()
    for i in rs:
        if i[0]!="":
            name=rs[0][0]
            qry1=f"insert into friend_connection values('{username}','{name}','','','','')"
            cur.execute(qry1)
            mycon.commit()
            cur.close()
            mycon.close()
    else:
        print()
def follow_following(username):
    while True:
        print("\n\n⇛⇛⇛⇛1.If you want to see your followers and following.")
        print("\n⇛⇛⇛⇛2.If you want to check the daily activity details of your friend whom you follow.")
        print("\n⇛⇛⇛⇛3.If you want to find your friend on FITNESS TRACKER.")
        print("\n⇛⇛⇛⇛4. If you want to remove someone you follow.")
        print("\n⇛⇛⇛⇛5.If u want to return to the main menu.")
        n=input("\nEnter your choice from the following:")
        mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
        cur=mycon.cursor()
        qr1="update friend_connection set Follow=Trim(Both ',' From Follow)"
        qr2="update friend_connection set Follower=Trim(Both ',' From Follower)"
        qr3="update friend_connection set C_Followers=Trim(Both ',' From C_Followers)"
        qr4="update friend_connection set C_Following=Trim(Both ',' From C_Following)"
        cur.execute(qr1)
        cur.execute(qr2)
        cur.execute(qr3)
        cur.execute(qr4)
        mycon.commit()
        cur.close()
        mycon.close()
        if n in '1':
            mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
            cur=mycon.cursor()
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
                qry2=f"select Follower from friend_connection where username='{username}'"
                cur.execute(qry2)
                sa=cur.fetchall()
                if sa[0][0]in '':
                    print("\n\nThere aren't any new friend requests.")
                else:
                    new_follower=sa[0][0].split(',')
                    print("\nHere are new friend requests of your friends.")
                    print("\nFull_Name\tUsername")
                    w=[]
                    if '' in new_follower:
                        new_follower.remove('')
                    for m in new_follower:
                        qry3=f"select FullName from friend_connection where username='{m}'"
                        cur.execute(qry3)
                        na=cur.fetchall()
                        w.append(na[0][0])
                    for h in range(len(w)):
                        print(w[h],'\t',new_follower[h])
                    print('\n')
                    ask=input("\nDo you want to accept any of the requests(Yes/No):")
                    if ask in 'yesYes':
                        while True:
                            print("\n\n)))---1. If you want to accept all the requests.")
                            print("\n)))---2. If you want to accept specific requests and delete the rest.")
                            u=input("\nEnter the number alongside with the task that you want to proceed with:")
                            if u in '1':
                                qry4=f"update friend_connection set C_Followers = concat(C_Followers, ',', Follower), C_Following=concat(C_Following,',',Follower),Follower='' WHERE Username = '{username}'"
                                cur.execute(qry4)
                                mycon.commit()
                                for i in new_follower:
                                    qry5=f"update friend_connection set C_Followers=concat(C_Followers,',{username}'),C_Following=concat(C_Following,',{username}'),Follow=replace(Follow,'{username}','') where username='{i}'"
                                    cur.execute(qry5)
                                    mycon.commit()
                                print("\nAll the requests have been accepted by you")
                                break
                            elif u in '2':
                                time.sleep(0.3)
                                print("\nFull_Name\tUsername")
                                for h in range(len(w)):
                                    print(w[h],'\t',new_follower[h])
                                kl=input("Enter all the correct usernames separated by commas in order to accept those requests:")
                                kl=kl.split(',')
                                ku=[]
                                for ab in new_follower:
                                    for op in kl:
                                        if ab==op:
                                            qry6=f"update friend_connection set C_Followers = concat(C_Followers,',{op}'), C_Following=concat(C_Following,',{op}'),Follower=replace(Follower,'{op}','') WHERE Username = '{username}'"
                                            cur.execute(qry6)
                                            ku.append(ab)
                                            mycon.commit()
                                        else:
                                            pass
                                for we in ku:
                                    qry7=f"update friend_connection set C_Followers=concat(C_Followers,',{username}'),C_Following=concat(C_Following,',{username}'),Follow=replace(Follow,'{username}','') where username='{we}'"
                                    cur.execute(qry7)
                                    mycon.commit()
                                print("\n\nAll the requests that you asked for are accepted")
                                break
                            else:
                                print("\nPlease enter a valid choice of the following.")
            else:
                print("\nThere aren't any followers or following of your profile.\n")
                time.sleep(1)
                qry2=f"select Follower from friend_connection where username='{username}'"
                cur.execute(qry2)
                sa=cur.fetchall()
                if sa[0][0] in '':
                    print("\n\nThere aren't any new friend requests too.")
                else:
                    new_follower=sa[0][0].split(',')
                    print("\nHere are new friend requests of your friends.")
                    print("\nFull_Name\tUsername")
                    w=[]
                    if '' in new_follower:
                        new_follower.remove('')
                    for m in new_follower:
                        qry3=f"select FullName from friend_connection where username='{m}'"
                        cur.execute(qry3)
                        na=cur.fetchall()
                        w.append(na[0][0])
                    for h in range(len(w)):
                        print(w[h],'\t',new_follower[h])
                    print('\n')
                    ask=input("\nDo you want to accept any of the requests(Yes/No):")
                    if ask in 'yesYes':
                        while True:
                            print("\n\n)))---1. If you want to accept all the requests.")
                            print("\n)))---2. If you want to accept specific requests and delete the rest.")
                            u=input("\nEnter the number alongside with the task that you want to proceed with:")
                            if u in '1':
                                qry4=f"update friend_connection set C_Followers = concat(C_Followers, ',', Follower), C_Following=concat(C_Following,',',Follower),Follower='' WHERE Username = '{username}'"
                                cur.execute(qry4)
                                mycon.commit()
                                for i in new_follower:
                                    qry5=f"update friend_connection set C_Followers=concat(C_Followers,',{username}'),C_Following=concat(C_Following,',{username}'),Follow=replace(Follow,'{username}','') where username='{i}'"
                                    cur.execute(qry5)
                                    mycon.commit()
                                print("\nAll the requests have been accepted by you")
                                break
                            elif u in '2':
                                time.sleep(0.3)
                                print("\nFull_Name\tUsername")
                                for h in range(len(w)):
                                    print(w[h],'\t',new_follower[h])
                                kl=input("Enter all the correct usernames separated by commas in order to accept those requests:")
                                kl=kl.split(',')
                                ku=[]
                                for ab in new_follower:
                                    for op in kl:
                                        if ab==op:
                                            qry6=f"update friend_connection set C_Followers = concat(C_Followers,',{op}'), C_Following=concat(C_Following,',{op}'),Follower=replace(Follower,'{op}','') WHERE Username = '{username}'"
                                            cur.execute(qry6)
                                            ku.append(ab)
                                            mycon.commit()
                                        else:
                                            pass
                                for we in ku:
                                    qry7=f"update friend_connection set C_Followers=concat(C_Followers,',{username}'),C_Following=concat(C_Following,',{username}'),Follow=replace(Follow,'{username}','') where username='{we}'"
                                    cur.execute(qry7)
                                    mycon.commit()
                                print("\n\nAll the requests that you asked for are accepted")
                                break
                            else:
                                print("\nPlease enter a valid choice of the following.")
            cur.close()
            mycon.close()
    
        elif n in '2':
            mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
            cur=mycon.cursor()
            qry13=f"select C_Followers from friend_connection where username='{username}'"
            cur.execute(qry13)
            hh=cur.fetchall()
            if hh[0][0]not in '':
                print("\n Here is the list of your followers.\n")
                time.sleep(1)
                hh=hh[0][0].split(',')
                gg=[]
                for i in hh:
                    qry14=f"select FullName from friend_connection where username='{i}'"
                    cur.execute(qry14)
                    a=cur.fetchall()
                    gg.append(a[0][0])
                print("\nFullName\t\tUsername")
                for l in range(len(hh)):
                    print(gg[l],'\t',hh[l])
                time.sleep(1.2)
                name2=input("\nEnter the Fullname or the username of your friend whose activity you want to see:").strip()
                p=""
                for q in range(len(name2)):
                    if name2[q]==" ":
                        p=name2[0].upper()+name2[1:q+1]+name2[q+1].upper()+name2[q+2:]
                        p=name2
                        name2=""
                        break
                    else:
                        name2=name2
                if p=="" and name2!="" and name2 in hh:
                    qry15=f"select userid.Username, userid.FullName,{name2}_plan_details.*,{name2}_daily_activity.* from userid left join {name2}_plan_details on userid.Username={name2}_plan_details.Username left join {name2}_daily_activity on userid.Username={name2}_daily_activity.Username where userid.Username='{name2}'"
                    cur.execute(qry15)
                    rs=cur.fetchall()
                    for i in range(18):
                        b=rs[0][i]
                        if i==0:
                            print("\n Username of friend is:",b)
                            time.sleep(0.25)
                        elif i==1:
                            print("\n Name of friend:  ",b)
                            time.sleep(0.25)
                        elif i==3:
                            print("\n Plan name chosen by him/her : ",b)
                        elif i==4:
                            print("\n Description of the plan: ",b)
                        elif i==5:
                            print("\n Duration of per session class: ",b)
                        elif i==6:
                            print("\n Total number of months of the lasting of the plan:",b)
                        elif i==7:
                            print("\n Additional excersises that are needed to be performed by him/her are: ",b)
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
                    time.sleep(1)
                elif p!="" and p in gg and name2=="":
                    v=gg.index(p)
                    name2=hh[v]
                    qry15=f"select userid.Username, userid.FullName,{name2}_plan_details.*,{name2}_daily_activity.* from userid left join {name2}_plan_details on userid.Username={name2}_plan_details.Username left join {name2}_daily_activity on userid.Username={name2}_daily_activity.Username where userid.Username='{name2}'"
                    cur.execute(qry15)
                    rs=cur.fetchall()
                    for i in range(18):
                        b=rs[0][i]
                        if i==0:
                            print("\n Username of friend is:",b)
                            time.sleep(0.25)
                        elif i==1:
                            print("\n Name of friend:  ",b)
                            time.sleep(0.25)
                        elif i==3:
                            print("\n Plan name chosen by him/her : ",b)
                        elif i==4:
                            print("\n Description of the plan: ",b)
                        elif i==5:
                            print("\n Duration of per session class: ",b)
                        elif i==6:
                            print("\n Total number of months of the lasting of the plan:",b)
                        elif i==7:
                            print("\n Additional excersises that are needed to be performed by him/her are: ",b)
                            time.sleep(0.5)
                        else:
                            break
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
                    time.sleep(1)
                else:
                    print("\nYou may have entered a wrong username or name that is not in your followers.Please try again later.")
            else:
                time.sleep(1)
                print("\n\nIt seems like you don't have any mutual friends.\n")
            mycon.close()
            cur.close()
        elif n in '3':
            name1=input("\nEnter either username of your friend or complete Fullname to search:").strip()
            mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
            cur=mycon.cursor()
            qry8="select Username,FullName from friend_connection"
            cur.execute(qry8)
            jb=cur.fetchall()
            p=""
            for q in range(len(name1)):
                if name1[q]==" ":
                    p=name1[0].upper()+name1[1:q+1]+name1[q+1].upper()+name1[q+2:]
                    name1=p
                else:
                    name1=name1
            l=[]
            m=[]
            ccc=0
            for rt in range(len(jb)):
                l.append(jb[rt][0])
            for yr in range(len(jb)):
                m.append(jb[yr][1])
            for ab in l:
                if name1==ab:
                    f=input("\nDo you want to send him/her friend request(Yes/No):")
                    ccc+=1
                    if f in 'Yesyes':
                        qry9=f"update friend_connection set Follower=concat(Follower,',{username}') where Username='{name1}'"
                        cur.execute(qry9)
                        mycon.commit()
                        qry10=f"update friend_connection set Follow=concat(Follow,',{name1}') where Username='{username}'"
                        cur.execute(qry10)
                        mycon.commit()
                        print(f"\n\nYou have send a friend request to {name1} successfully\n")
                        break
                    else:
                        print("\n You chose not to send request to your friend...Returning back......")
                        time.sleep(1)
                        break
            if p in m:
                ccc+=1
                index=m.index(p)
                name1=l[index]
                f=input("\nDo you want to send him/her friend request(Yes/No):")
                if f in 'Yesyes':
                    qry11=f"update friend_connection set Follower=concat(Follower,',{username}') where Username='{name1}'"
                    cur.execute(qry11)
                    mycon.commit()
                    qry12=f"update friend_connection set Follow=concat(Follow,',{name1}') where Username='{username}'"
                    cur.execute(qry12)
                    mycon.commit()
                    print(f"\n\nYou have send a friend request to {name1} successfully\n")
                        
                else:
                    print("\n You chose not to send request to your friend...Returning back......")
                    time.sleep(1)
            if ccc==0:
                time.sleep(1)
                print("\n The username or name you searched for might not be on FITNESS TRACKER\n")
                time.sleep(1)
            cur.close()
            mycon.close()
        elif n in '4':
            print("Here is the list of your followers.")
            mycon=con.connect(host='localhost',user='root',passwd='manngupta',database='fitness_tracker')
            cur=mycon.cursor()
            qry13=f"select C_Followers from friend_connection where username='{username}'"
            cur.execute(qry13)
            hh=cur.fetchall()
            if hh[0][0]not in '':
                hh=hh[0][0].split(',')
                if hh[0][0] in "":
                    time.sleep(1)
                    print("\n\nIt seems like you don't have any friend to delete.\n")
                else:
                    gg=[]
                    for i in hh:
                        qry14=f"select FullName from friend_connection where username='{i}'"
                        cur.execute(qry14)
                        a=cur.fetchall()
                        gg.append(a[0][0])
                    print("\nFullName\tUsername")
                    for l in range(len(hh)):
                        print(gg[l],'\t',hh[l])
                    time.sleep(1.2)
                    name2=input("\nEnter the Fullname or the username of your friend whom you want to delete in your friend list:").strip()
                    p=""
                    for q in range(len(name2)):
                        if name2[q]==" ":
                            p=name2[0].upper()+name2[1:q+1]+name2[q+1].upper()+name2[q+2:]
                            p=name2
                            name2=""
                            break
                        else:
                            name2=name2
                    if p in "" and name2 not in"" and name2 in hh:
                        qry17=f"update friend_connection set C_Followers=replace(C_Followers,'{name2}',''),C_Following=replace(C_Following,'{name2}','') where username='{username}'"
                        cur.execute(qry17)
                        mycon.commit()
                        qry18=f"update friend_connection set C_Followers=replace(C_Followers,'{username}',''),C_Following=replace(C_Following,'{username}','') where username='{name2}'"
                        cur.execute(qry18)
                        mycon.commit()
                        print("\nYour request of removing your friend has been successfull...Please check your updated friend list\n")
                        time.sleep(1)
                    elif p!="" and name2 == "" and p in gg:
                        v=gg.index(p)
                        name2=hh[v]
                        qry17=f"update friend_connection set C_Followers=replace(C_Followers,'{name2}',''),C_Following=replace(C_Following,'{name2}','') where username='{username}'"
                        cur.execute(qry17)
                        mycon.commit()
                        qry18=f"update friend_connection set C_Followers=replace(C_Followers,'{username}',''),C_Following=replace(C_Following,'{username}','') where username='{name2}'"
                        cur.execute(qry18)
                        mycon.commit()
                        print("\nYour request of removing your friend has been successfull...Please check your updated friend list\n")
                        time.sleep(1)
                    else:
                        print("\nYou might have chosen a wrong username or name of your friend..Please try again later")
            else:
                print("\nIt seems like you don't have any friends.\n")
        elif n in '5':
            print("\n\n\t\t\t\t\t\tGetting back to the main menu....")
            time.sleep(1.1)
            break
        else:
            print("\nPLease enter a valid choice from the following:\n")

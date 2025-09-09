import time
def payment():
    print("\nThis is a very secured payment method....And all the details are erased once the payment is finished.")
    time.sleep(0.4)
    print("\nPlease click enter to continue with the payment.")
    a=input("Press Enter :")
    while True:
        if a=="":
            break
        else:
            a=input("Please enter in order to continue with the payment")
    card_no=int(input("\nEnter your debit/credit card number:"))
    while True:
        if card_no<=100000000000000 or card_no>=999999999999999:
            card_no=int(input("Please enter correct card Number(15-digit):"))
        else:
            break
    exp_date=input("\nEnter card's Expiry date (In the form: MM/YY):")
    while True:
        if len(exp_date)==5 and exp_date[0].isdigit() and exp_date[1].isdigit() and exp_date[3].isdigit() and exp_date[4].isdigit() and exp_date[0] in '01':
            break
        else:
            exp_date=input("Please Enter the expiry date (In the form: MM/YY):")
    cvv=int(input("\nEnter the CVV of the card:"))
    while True:
        if cvv>=1000 and cvv<=9999:
            break
        else:
            cvv=int(input("Please Enter the correct CVV of the card(4-digit):"))
    a=input("\nPress Enter(Don't refresh or close the page):")
    while True:
        if a=="":
            break
        else:
            a=input("Please enter to continue:")
    time.sleep(0.4)
    print("\n\t\t\t\t\t\tLoading...............Please Wait........")
    time.sleep(2)
    print("\n\t\t\t\t\tThank You.The payment has been confirmed")
def schedule():
    print("\nMorning (6:00 AM - 8:00 AM):")
    print("\n •6:00 AM - 6:30 AM: Cardio Blast")
    print("\t\t•Jumping Jacks: 3 sets of 30 seconds")
    print("\t\t•High Knees: 3 sets of 30 seconds")
    print("\t\t•Burpees: 3 sets of 10 reps")
    print("\t\t•Running in Place: 3 sets of 1 minute")
    print("\t\t•Jump Rope: 3 sets of 1 minute")
    print("\n •6:30 AM - 7:00 AM: Strength Builder")
    print("\t\t•Squats: 3 sets of 10 reps")
    print("\t\t•Push-ups: 3 sets of 10 reps")
    print("\t\t•Lunges: 3 sets of 12 reps (each leg)")
    print("\t\t•Dumbbell Rows: 3 sets of 10 reps (each arm)")
    print("\t\t•Plank: 3 sets of 30 seconds")
    print("\n •7:00 AM - 7:30 AM: Flexibility Flow")
    print("\t\t•Cat-Cow Stretch: 3 sets of 30 seconds")
    print("\t\t•Forward Fold: 3 sets of 1 minute")
    print("\t\t•Standing Quad Stretch: 3 sets of 30 seconds (each leg)")
    print("\t\t•Child's Pose: 3 sets of 1 minute")
    print("\t\t•Seated Spinal Twist: 3 sets of 30 seconds (each side)")
    time.sleep(1.2)
    print("\n •7:30 AM - 8:00 AM: Breakfast & Rest")
    print("\nMid-Morning (10:00 AM - 12:00 PM):")
    print("\n •10:00 AM - 10:30 AM: Core Crusher")
    print("\t\t•Bicycle Crunches: 3 sets of 15 reps (each side)")
    print("\t\t•Plank with Shoulder Taps: 3 sets of 30 seconds")
    print("\t\t•Russian Twists: 3 sets of 20 reps")
    print("\t\t•Leg Raises: 3 sets of 12 reps")
    print("\t\t•Superman Pose: 3 sets of 30 seconds")
    print("\n •10:30 AM - 12:00 PM: Work/Study")
    time.sleep(1)
    print("\nLunch Break (12:00 PM - 1:00 PM):")
    print("\n •12:00 PM - 12:30 PM: Healthy Lunch & Rest")
    print("\nAfternoon (2:00 PM - 4:00 PM):")
    print("\n •2:00 PM - 3:00 PM: Total Body Tune-Up")
    print("\t\t•Jump Squats: 3 sets of 15 reps")
    print("\t\t•Push-ups: 3 sets of 12 reps")
    print("\t\t•Bent-over Rows: 3 sets of 12 reps")
    print("\t\t•Mountain Climbers: 3 sets of 1 minute")
    print("\t\t•Dumbbell Lunges: 3 sets of 12 reps (each leg)")
    print("\n •3:00 PM - 4:00 PM: Rest & Recovery")
    time.sleep(1)
    print("\nEvening (6:00 PM - 8:00 PM):")
    print("\n •6:00 PM - 7:00 PM: Outdoor Activity (e.g., Jogging, Cycling, or Swimming)")
    print("\n •7:00 PM - 8:00 PM: Dinner & Relaxation")
    print("\nNight (9:00 PM - 10:00 PM):")
    print("\n •9:00 PM - 9:30 PM: Flexibility Flow (Optional)")
    print("\t\t•Cat-Cow Stretch: 3 sets of 30 seconds")
    print("\t\t•Forward Fold: 3 sets of 1 minute")
    print("\t\t•Standing Quad Stretch: 3 sets of 30 seconds (each leg)")
    print("\t\t•Child's Pose: 3 sets of 1 minute")
    print("\t\t•Seated Spinal Twist: 3 sets of 30 seconds (each side)")
    print("\n •9:30 PM - 10:00 PM: Wind Down & Prepare for Bed")
def workout_plan():
    while True:
        print("\nNOTE: You must have to select one plan and pay for it in order to continue.")
        print("\n------->Our different plans as follows:")
        print("\t1. Cardio Blast")
        print("\t2. Strength Builder")
        print("\t3. Flexibility Flow")
        print("\t4. Core Crusher")
        print("\t5. Total Body Tune-Up")
        print("\t6. If you have chosen the plan and payment has been made")
        n=int(input("Enter your choice(1-6) which plan you want to see:"))
        if n==1:
            print("\n\n\t\t\t\t\t\t\tCARDIO BLAST")
            print("\n•Description: This plan focuses on improving cardiovascular health and burning calories through high-intensity cardio exercises.")
            print("\n•Duration: 30 minutes per session")
            print("\n•Exercises:")
            print("\t•Jumping Jacks: 3 sets of 30 seconds")
            print("\t•High Knees: 3 sets of 30 seconds")
            print("\t•Burpees: 3 sets of 10 reps")
            print("\t•Running in Place: 3 sets of 1 minute")
            print("\t•Jump Rope: 3 sets of 1 minute")
            print("\n•Subscription Price: $9.99/month")
            choice=input("\nDO You want to go with this Plan[Y--(Yes)/N--(No)]:")
            if choice in 'YyYESyesYes':
                time_period=int(input("\nEnter the number of months for which you want to opt this plan:"))
                while True:
                    if time_period>0:
                        break
                    else:
                        time_period=int(input("Please Enter a correct number of months:"))
                print("\nTo continue please make the payment.")
                payment()
                g=9.99*time_period
                print(f"\n\n\t\t\t\tMESSAGE: ${g} has been credited/debited from your account number XXXX XXXXXX XXXXX\n\n")
                time.sleep(3)
                print("\nThe schedule for the respective classes is given below:")
                schedule()
                f="Cardio Blast"
                break
            else:
                continue
        elif n==2:
            print("\n\n\t\t\t\t\t\t\tSTRENGTH BUILDER")
            print("\n•Description: This plan aims to build muscle strength and endurance through resistance training exercises targeting major muscle groups.")
            print("\n•Duration: 45 minutes per session")
            print("\n•Exercises:")
            print("\t•Squats: 3 sets of 10 reps")
            print("\t•Push-ups: 3 sets of 10 reps")
            print("\t•Lunges: 3 sets of 12 reps (each leg)")
            print("\t•Dumbbell Rows: 3 sets of 10 reps (each arm)")
            print("\t•Plank: 3 sets of 30 seconds")
            print("\n•Subscription Price: $12.99/month")
            choice=input("\nDO You want to go with this Plan[Y--(Yes)/N--(No)]:")
            if choice in 'YyYESyesYes':
                time_period=int(input("\nEnter the number of months for which you want to opt this plan:"))
                while True:
                    if time_period>0:
                        break
                    else:
                        time_period=int(input("Please Enter a correct number of months:"))
                print("\nTo continue please make the payment.")
                payment()
                g=12.99*time_period
                print(f"\n\n\t\t\t\tMESSAGE: ${g} has been credited/debited from your account number XXXX XXXXXX XXXXX\n\n")
                time.sleep(3)
                print("\nThe schedule for the respective classes is given below:")
                schedule()
                f="Strength Builder"
                break
            else:
                continue
        elif n==3:
            print("\n\n\t\t\t\t\t\t\tFLEXIBILITY FLOW")
            print("\n•Description: This plan focuses on improving flexibility, mobility, and relaxation through stretching and yoga-inspired movements.")
            print("\n•Duration: 20 minutes per session")
            print("\n•Exercises:")
            print("\t•Cat-Cow Stretch: 3 sets of 30 seconds")
            print("\t•Forward Fold: 3 sets of 1 minute")
            print("\t•Standing Quad Stretch: 3 sets of 30 seconds (each leg)")
            print("\t•Child's Pose: 3 sets of 1 minute")
            print("\t•Seated Spinal Twist: 3 sets of 30 seconds (each side)")
            print("\n•Subscription Price: $7.99/month")
            choice=input("\nDO You want to go with this Plan[Y--(Yes)/N--(No)]:")
            if choice in 'YyYESyesYes':
                time_period=int(input("\nEnter the number of months for which you want to opt this plan:"))
                while True:
                    if time_period>0:
                        break
                    else:
                        time_period=int(input("Please Enter a correct number of months:"))
                print("\nTo continue please make the payment.")
                payment()
                g=7.99*time_period
                print(f"\n\n\t\t\t\tMESSAGE: ${g} has been credited/debited from your account number XXXX XXXXXX XXXXX\n\n")
                time.sleep(3)
                print("\nThe schedule for the respective classes is given below:")
                schedule()
                f="Flexibility Flow"
                break
            else:
                continue
        elif n==4:
            print("\n\n\t\t\t\t\t\t\tCORE CRUSHER")
            print("\n•Description: This plan targets the core muscles to improve stability, posture, and overall core strength.")
            print("\n•Duration: 25 minutes per session")
            print("\n•Exercises:")
            print("\t•Bicycle Crunches: 3 sets of 15 reps (each side)")
            print("\t•Plank with Shoulder Taps: 3 sets of 30 seconds")
            print("\t•Russian Twists: 3 sets of 20 reps")
            print("\t•Leg Raises: 3 sets of 12 reps")
            print("\t•Superman Pose: 3 sets of 30 seconds")
            print("\n•Subscription Price: $10.99/month")
            choice=input("\nDO You want to go with this Plan[Y--(Yes)/N--(No)]:")
            if choice in 'YyYESyesYes':
                time_period=int(input("\nEnter the number of months for which you want to opt this plan:"))
                while True:
                    if time_period>0:
                        break
                    else:
                        time_period=int(input("Please Enter a correct number of months:"))
                print("\nTo continue please make the payment.")
                payment()
                g=10.99*time_period
                print(f"\n\n\t\t\t\tMESSAGE: ${g} has been credited/debited from your account number XXXX XXXXXX XXXXX\n\n")
                time.sleep(3)
                print("\nThe schedule for the respective classes is given below:")
                schedule()
                f="Core Crusher"
                break
            else:
                continue
        elif n==5:
            print("\n\n\t\t\t\t\t\t\tTOTAL BODY TUNE--UP")
            print("\n•Description: This comprehensive plan engages multiple muscle groups to provide a full-body workout, enhancing strength and endurance.")
            print("\n•Duration: 60 minutes per session")
            print("\n•Exercises:")
            print("\t•Jump Squats: 3 sets of 15 reps")
            print("\t•Push-ups: 3 sets of 12 reps")
            print("\t•Bent-over Rows: 3 sets of 12 reps")
            print("\t•Mountain Climbers: 3 sets of 1 minute")
            print("\t•Dumbbell Lunges: 3 sets of 12 reps (each leg)")
            print("\n•Subscription Price: $14.99/month")
            choice=input("\nDO You want to go with this Plan[Y--(Yes)/N--(No)]:")
            if choice in 'YyYESyesYes':
                time_period=int(input("\nEnter the number of months for which you want to opt this plan:"))
                while True:
                    if time_period>0:
                        break
                    else:
                        time_period=int(input("Please Enter a correct number of months:"))
                print("\nTo continue please make the payment.")
                payment()
                g=14.99*time_period
                print(f"\n\n\t\t\t\tMESSAGE: ${g} has been credited/debited from your account number XXXX XXXXXX XXXXX\n\n")
                time.sleep(3)
                print("\nThe schedule for the respective classes is given below:")
                schedule()
                f="TotalBodyTune-Up"
                break
            else:
                continue
        else:
            print("Please select atleast one plan.")
    return(f,g)


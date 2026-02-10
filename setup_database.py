import mysql.connector

def setup():
    # Connect to MySQL server
    # NOTE: You must update these credentials to match your local MySQL setup
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'manngupta' 
    }

    try:
        # Connect to MySQL server (no database selected yet)
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()
        
        # Create Database
        cursor.execute("CREATE DATABASE IF NOT EXISTS fitness_tracker")
        print("Database 'fitness_tracker' ensured.")
        
        # Select Database
        cursor.execute("USE fitness_tracker")
        
        # 1. Create userid table
        # Structure inferred from: insert into userid values (FullName, Email, Phone, Username, Password, DOB)
        # and admin_control.py usage
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS userid (
            FullName VARCHAR(100),
            Email VARCHAR(100),
            Mobile_no BIGINT,
            Username VARCHAR(50) PRIMARY KEY,
            Login_password VARCHAR(50),
            DOB DATE
        )
        """)
        print("Table 'userid' ensured.")

        # 2. Create friend_connection table
        # Structure inferred from friends.py
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS friend_connection (
            Username VARCHAR(50),
            FullName VARCHAR(100),
            Follow TEXT,
            Follower TEXT,
            C_Followers TEXT,
            C_Following TEXT,
            FOREIGN KEY (Username) REFERENCES userid(Username) ON DELETE CASCADE
        )
        """)
        print("Table 'friend_connection' ensured.")

        # 3. Create events_and_programs table
        # Structure inferred from admin_control.py
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS events_and_programs (
            EventName VARCHAR(100),
            StartDate DATE,
            EndDate DATE,
            TimeDuration VARCHAR(50),
            Description TEXT
        )
        """)
        print("Table 'events_and_programs' ensured.")
        
        cnx.commit()
        cursor.close()
        cnx.close()
        print("\nSUCCESS: Database setup complete!")
        print("You can now run 'python main.py'")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        print("\nTROUBLESHOOTING:")
        print("1. Make sure your MySQL server is running.")
        print("2. Check if the user/password in this script matches your MySQL credentials.")

if __name__ == "__main__":
    setup()

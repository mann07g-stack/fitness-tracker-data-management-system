# Fitness Tracker Data Management System

A comprehensive Python-based application for tracking personal fitness activities, managing workout plans, and social interactions, built with a MySQL backend. This project features dual interfaces for both **Users** (Customers) and **Admins**.

## 🚀 Features

### For Users
*   **Daily Activity Logging**: Record daily workouts including duration, intensity, calories burnt, and categories (Cardio, Strength, etc.).
*   **Goal Setting**: Set and track personalized fitness goals based on BMI and body measurements.
*   **Workout Plans**: Choose from pre-defined plans like "Cardio Blast", "Strength Builder", and "Flexibility Flow".
*   **Social Connectivity**: Follow friends, send friend requests, and view their progress.
*   **Data Management**: View detailed reports of your activities and update or delete your records.

### For Admins
*   **User Management**: View user details and manage accounts.
*   **Plan Management**: Create and schedule new fitness events.
*   **System Oversight**: Full control over the database records.

## 🛠️ Prerequisites

Before running the application, ensure you have the following installed:

*   **Python 3.8+**
*   **MySQL Server**

## 📦 Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/mann07g-stack/fitness-tracker-data-management-system.git
    cd fitness-tracker-data-management-system
    ```

2.  **Set Up Virtual Environment**
    It is recommended to use a virtual environment to manage dependencies.
    
    *   **Windows:**
        ```powershell
        python -m venv venv
        .\venv\Scripts\activate
        ```
    *   **macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## 🗄️ Database Setup

The application interacts heavily with a MySQL database.

1.  Start your MySQL Server.
2.  **Important**: The current codebase uses default credentials. You may need to update them to match your local setup.
    *   Open `Introduction_of_Program.py`, `main.py`, and other module files.
    *   Locate the database connection lines:
        ```python
        con.connect(host='localhost', user='root', passwd='YOUR_PASSWORD', database='fitness_tracker')
        ```
    *   Update `user` and `passwd` to match your MySQL credentials.
    *   Ensure a database named `fitness_tracker` exists or allow the program to create tables as needed (the program contains `create table` logic).

## 🏃 Usage

To start the application, run the main script:

```bash
python main.py
```

Follow the on-screen prompts to:
1.  **Login** or **Sign Up**.
2.  Navigate the main menu to log activities, check plans, or manage settings.

## 📂 Project Structure

*   `main.py`: The entry point of the application.
*   `Introduction_of_Program.py`: Handles user authentication (Login/Signup).
*   `Activity_each_day.py`: Module for logging and viewing daily activities.
*   `Plan.py` & `New_Plan_Input.py`: Manages fitness plans and subscriptions.
*   `friends.py`: Social features (Follow/Unfollow logic).
*   `admin_control.py`: Administrative functions.
*   `goal_setting.py`: Logic for calculating BMI and setting goals.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## 📄 License

This project is open-source and available under the standard MIT License.
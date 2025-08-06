# 🏦 Vault - The Commitment Marketplace

## 📜 Description

**Vault** is a command-line application built on a powerful idea: turning intentions into action through real-world consequences. It's a commitment marketplace where you stake your own money on achieving your personal and professional goals.

-   **Set a Goal**: Define a task you want to accomplish.
-   **Stake Your Cash**: Put your own money on the line.
-   **Appoint a Witness**: Assign a trusted friend to verify the outcome.
-   **Succeed or Donate**: If you succeed, you get your money back. If you fail, the stake is automatically moved to your donation total, intended for a charity of your witness's choosing.

It’s not just a to-do list; it’s a psychological tool designed to create powerful accountability.

---

## ⚠️ Important: Early Prototype Notice

This program is a **very early prototype** created for fun and demonstration purposes. It is **not the final vision** for the Vault application and currently has known limitations and bugs.

Think of this as a proof-of-concept for the core logic. It will be upgraded and updated soon!

---

## ⚙️ Requirements

-   Python **3.8+**
-   A running **MySQL Server** instance
-   Python Packages:
    -   `mysql-connector-python`
    -   `bcrypt`
    -   `pyfiglet`

> 💡 Install required packages using:
> ```bash
> pip install mysql-connector-python bcrypt pyfiglet
> ```

---

## 📂 Configuration & Setup

There is no configuration file to edit. The application is designed to set itself up automatically.

1.  **MySQL Server**: Ensure your MySQL server is running before you start the application.
2.  **Database Credentials**: When you run the script for the first time, you will be prompted to enter your MySQL credentials (host, user, and password).
3.  **Automatic Setup**: The script will automatically:
    -   Create a database named `VaultPrototype` if it doesn't exist.
    -   Create the necessary tables (`User`, `Sessions`).

---

## 🛠️ How It Works

1.  **Connects to Database**: The app first establishes a connection to your MySQL server.
2.  **User Authentication**: You are prompted to either **Register** a new account or **Login** to an existing one. Passwords are securely hashed using `bcrypt`.
3.  **Main Menu**: Once logged in, you can see your current balance and total amount donated from failed commitments.
4.  **Create a Commitment**: Define your task, the amount to stake, the deadline, your witness, and the charity to donate to upon failure. The staked amount is immediately deducted from your balance.
5.  **Automatic Consequence Engine**: Every time you return to the main menu, the app automatically checks for any pending commitments that have passed their deadline.
6.  **Failure Processing**: If a deadline has passed, the commitment is marked as `failed`, and the staked funds are moved to your total donation tracker.

---

## ▶️ How To Run

1.  Make sure your **MySQL Server is running**.
2.  Open your terminal or command prompt.
3.  Navigate to the project directory.
4.  Run the main application script:

```bash
python app.py
````

5.  Follow the on-screen prompts:
      - Enter your database credentials first.
      - Choose to **Login** or **Register**.
      - Use the main menu to navigate the application.

-----

## ⛔ Important Notes

  - This is a **command-line only** application.
  - The "witness" and "charity" are currently just text fields for tracking. There is no notification or integration system.
  - The application is intended for **local testing and demonstration only**.
  - Always double-check your inputs, as there is minimal input validation.

-----

## 🧠 Pro Tips

  - For testing, you can set deadlines for just a few minutes into the future to see the automatic failure processing work. (Note: The check is by `date`, not `time`, so it will process after midnight).
  - Use a dedicated MySQL user with limited privileges for better security.
  - Keep the terminal window visible to see real-time status updates.

-----

## 🧰 Troubleshooting

| Problem                                    | Solution                                                                                                                              |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| ❓ Can't connect to database               | Double-check that your MySQL server is running and that your host, user, and password credentials are correct.                        |
| ❌ `Commands out of sync` or other DB errors | The latest version uses a connection pool and atomic transactions to prevent this, but if it occurs, restarting the app is a safe bet. |
| 📨 Data not updating                       | The main user dashboard (balance, donations) refreshes every time the main menu is displayed.                                         |

-----

## 👨‍💻 Developer  
Created by Evan William (2025)  
Version: 0.1.0 (Beta Prototype)



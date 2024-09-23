## UserManager CLI
### Description
**Console application for user management based on Linux system
uses the Curses library to create a text interface and works with sudo via subprocess to add, lock, unlock and remove users on the system**

![image](https://github.com/user-attachments/assets/23ba35ee-c197-43fa-bf6a-b4ca1a0bf356)

### Requirements:
   Python 3.x
   Linux
   sudo rights
### Installation
   1) git clone https://github.com/AralAskarov/UserManagerCli.git
   2) Make sure you have Python version 3.x installed. To check, use the command:
      python3 --version
   3) The program requires the curses and subprocess library, which is usually already built into Python on most Linux systems.
### Starting the program
   1) Open a terminal.
   2) Go to the directory where the program script is located.
   3) Run the script:
      python3 user_management.py
   4) At startup you will be prompted to enter your sudo password. This is necessary to perform administrative tasks.
## Features
The program works through curses and supports the functions described below.
   ### Navigation
    [↑] и [↓] — moving through the list of users.
    [←] и [→] — switching between pages if the user list is more than 4 people.
   ### Adding a new user
    1) Press the N key to add a new user.
    2) Enter the name of the new user and confirm creation:
       - If the user already exists, you will receive a message about this.
       - If the correct name is entered, the user will be created using the useradd command.
   ### Deleting a user
    1) Press Backspace to delete the selected user.
    2) Confirm the action by entering y. The user will be deleted
   ### Blocking a user
    1) Press L key to lock.
    2) Confirm the action by entering y. The user will be locked via the command usermod -L
   ### Unblocking a user
    1) Press U key to unlock.
    2) Confirm the action by entering y. The user will be unblocked via the usermod -U command.
   ### Status messages
    The program provides feedback on the screen on the completion of actions. Below is a list of possible messages:

    "user del successfully" - the user was successfully deleted.
    "deletion canceled" — user deletion has been cancelled.
    "created successfully" - the user was successfully created.
    "creation canceled" — user creation has been cancelled.
    "locked successfully" - the user has been successfully blocked.
    "blocking canceled" — user blocking has been cancelled.
    "unlocked successfully" - the user has been successfully unlocked.
    "unlocking canceled" — user unlocking has been cancelled.
    "exist already" - an attempt to create a user with a name that already exists.
    "user already locked" - the selected user is already blocked.
    "user not locked"—the selected user is not blocked.
  ### Shutdown
    To exit the program, press the Q key. When you exit, the program will run sudo -k to reset superuser privileges.
  ### Notes and Limitations
    Users "aral" and "aral-111" cannot be deleted or blocked. This is done so that I don't accidentally delete myself :)

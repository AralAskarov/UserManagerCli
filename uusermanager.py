import curses
from curses import wrapper
import pexpect
import math
import subprocess
import time

command = 'awk -F: \'$3 >= 1000 && $1 != "nobody" { print $1 }\' /etc/passwd'
process = pexpect.spawn(command)
process.expect(pexpect.EOF)
output = process.before.decode('utf-8')
users = output.splitlines()
print(users)
blocked_users = []

#for i in users:
    
 #   command = f'sudo -S passwd -S {i}'
  #  process = pexpect.spawn(command,timeout=5)
   # process.expect(pexpect.EOF)
   # output = process.before.decode('utf-8')
  #  status = output.splitlines()
   # print(status)
    #first_line = status[0]
    #parts = first_line.split()
    #status_flag = parts[1]
    #if status_flag == 'L':
        #blocked_users.append(i)

    
print(len(users))
print(float(len(users)/4))
print(math.ceil(float(len(users)/4)))
def main(stdscr):
    isSudo = False
    pages = math.ceil(float(len(users) / 4))
    current_arrow = 6
    current_page = 1
    curses.curs_set(0)
    while isSudo == False:
        curses.echo()
        stdscr.addstr(1, 0, "write your sudo password: ")
        stdscr.refresh()
        sudo = stdscr.getstr().decode("utf-8")
        result = subprocess.call('echo {} | sudo -S {}'.format(f'{sudo}', f"sudo -S -v"), shell=True)
        #stdscr.addstr(2,0, str(result))
        stdscr.clear()
        curses.noecho()
        if result == 0:
            isSudo = True
        else:
            sudo = ""
            stdscr.addstr(4,0, "UNCORRECT")
            while True:
                stdscr.clear()
                stdscr.addstr(2,0, "Wrond Password")
                stdscr.addstr(8,0, "Press R to retype password")
                key = stdscr.getch()
                if key == ord("r"):
                    stdscr.clear()
                    break
                
       
    for i in users:    
        command = f'sudo -S passwd -S {i}'
        process = pexpect.spawn(command,timeout=5)                              
        process.expect(pexpect.EOF)
        output = process.before.decode('utf-8')
        status = output.splitlines()
        print(status)
        first_line = status[0]
        parts = first_line.split()
        status_flag = parts[1]
        if status_flag == 'L':
            blocked_users.append(i)
  


    while isSudo:
        stdscr.clear()
        stdscr.addstr(0, 0,'--------------------------------------------')
        stdscr.addstr(1, 0, '           User Management')
        stdscr.addstr(2, 0,'--------------------------------------------')
        stdscr.addstr(4, 0, f'page {current_page} of {pages}')
        for i, user in enumerate(users[(current_page*4)-4:current_page*4]):
            status_user = ""
            for us in blocked_users:
                if us == user:
                    status_user = "BLOCKED"
        
        
            if i+6 != current_arrow:
                stdscr.addstr(i + 6, 0, f"  {i+(current_page*4)-4+1} {user}     {status_user}")
            else:
                stdscr.addstr(i + 6, 0, f"> {i+(current_page*4)-4+1} {user} {status_user}", curses.A_REVERSE)
        
        stdscr.addstr(11,0, "[↑ ↓] navigate")
        stdscr.addstr(12,0, "[← →] page")
        stdscr.addstr(13,0, "[N] new user")
        stdscr.addstr(14,0, "[Q] quit")
        stdscr.addstr(15,0, "[Backspace] delete user")

        key = stdscr.getch()
        if key == curses.KEY_UP:
            current_arrow = max(6, current_arrow - 1)
        elif key == curses.KEY_DOWN:
            if current_arrow <= 8:
                current_arrow = min(len(users) + 5, current_arrow+1)
        elif key == curses.KEY_RIGHT:
            if current_page < pages:
                current_arrow = 6
                current_page = current_page + 1
        elif key == curses.KEY_LEFT:
            if current_page > 1:
                current_arrow = 6
                current_page = current_page - 1
        elif key == ord('n'):
            curses.echo()
            stdscr.addstr(18, 0, "write username: ")
            new_user = stdscr.getstr().decode("utf-8")
            users.append(new_user)
        #command_add = 'echo PASSWORD | sudo -S useradd -m -p "" {new_user}'
            #process = pexpect.spawn(command_add)
            #process.expect(pexpect.EOF)
            subprocess.call(f"sudo useradd -m -p pass {new_user}", shell=True)
            if len(users) % 4 == 1:
                pages = pages + 1
            curses.noecho()
        elif key == curses.KEY_BACKSPACE:
        #while True:
                #stdscr.addstr(22, 0, f"Current Arrow Value: :{users[current_arrow-6]}")
                #stdscr.refresh()
                
            if users[(current_arrow-6)+ (current_page*4)-4]=="aral" or users[(current_arrow-6)+(current_page*4)-4]=="aral-111":
                pass
            else:
                subprocess.call(f"sudo userdel -r {users[(current_arrow-6)+(current_page*4)-4]}", shell=True) 
                users.remove(users[(current_arrow-6)+(current_page*4)-4])
                current_arrow = current_arrow-1
                if len(users)%4 == 0:
                    pages = pages - 1
                    current_page = current_page - 1
                    current_arrow = 6
        elif key == ord('q'):
            #дописать килл судо
            break


    stdscr.refresh()   
wrapper(main)

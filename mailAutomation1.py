#=====================================================================================================================================================================================

import os
import time
import psutil
import urllib.request
import smtplib
import schedule
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def is_Connected():
    try:
        urllib.request.urlopen("https://www.google.com/", timeout=1)
        return True

    except urllib.request.URLError as err:
        return False

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def MailSender(filename, time):
    EmailList = ["pranavibaraskar2003@gmail.com","baraskar28tejaswini@gmail.com","pranavibaraskar95@gmail.com","pralavphakatkar007@gmail.com","baraskarpranavi78@gmail.com","baraskar28baraskar@gmail.com"]
    try:
        for mails in EmailList:
            fromaddr = "pranavibaraskar2411@gmail.com"
            toaddr = mails

            msg = MIMEMultipart()

            msg['From'] = fromaddr
            msg['To'] = toaddr


            body = """
            Hello %s
            WELCOME TO OUR AUTOMATED MAIL SENDER APPLICATION
            Please find attached Documents which contains log of running process
            Log file is created at : %s

            THIS MAIL IS AUTO GENERATED MAIL

            ThankYou & Regards,
            Pranavi G Baraskar
            Marvellous Infosystems
            """ %(toaddr, time)

            Subject = """
            Marvellous Infosystem Process Log Genereted at : %s
            """ %(time)

            msg['Subject'] = Subject

            msg.attach(MIMEText(body,'plain'))

            attachment = open(filename, "rb")

            p = MIMEBase('application','octet-stream')

            p.set_payload((attachment).read())

            encoders.encode_base64(p)

            p.add_header('Content-Disposition',"attachment; filename = %s" % filename)

            msg.attach(p)

            s = smtplib.SMTP('smtp.gmail.com',587)

            s.starttls()

            s.login(fromaddr,"yihxgzgnedizegcq")

            text = msg.as_string()

            s.sendmail(fromaddr, toaddr, text)

            s.quit()

            print("Log file sent through mail")

    except Exception as E:
                print("Unable to send main.",E)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def ProcessLog(log_dir = 'Marvellous'):
    listprocess = []

    #creating folder on same file path
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "-" * 80

    log_path = os.path.join(log_dir,"MarvellousLog%s.log" %(time.ctime()))

    f = open(log_path,'w')

    f.write(separator + "\n")
    f.write("Marvellous Infosystem Process Logger : "+ time.ctime() + "\n")
    f.write(separator + "\n")
    f.write("\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs = ['pid','name','username'])
            vms = proc.memory_info().vms / (1024 * 1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo)
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    for element in listprocess:
        f.write("%s\n" %element)

    print("Log file is Successfully generated at location %s " %(log_path))

    connected = is_Connected()

    if connected:
        startTime = time.time()
        MailSender(log_path, time.ctime())
        endTime = time.time()

        print("Took %s seconds to send mail" % (endTime - startTime))

    else:
        print("There is no internet connection")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    print("Application name : " +argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used record of running processess")
        exit()

    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Application AbsoultePath_of_Directory")
        exit()

    try:
        schedule.every(int(argv[1])).minutes.do(ProcessLog)

        while True:
            schedule.run_pending()
            time.sleep(1)

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input ", E)

if __name__ == "__main__":
    main()

#=====================================================================================================================================================================================
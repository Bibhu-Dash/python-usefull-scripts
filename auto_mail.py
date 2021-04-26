###this code will work if you will install smtp server on the host machine.. that you can get it from your company/organization
import os
import subprocess
import datetime
import time
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEImage import MIMEImage

####User defined module##### for this below modules separate code written
import get_test_case
import target_and_Build_ID
import gpu_snapshot_count
import kgsl_logs
#######################################

def trigger():
    MAILS = r'\\server\location\mails.txt'
    fp = open(MAILS,'r')
    mails = fp.read()
    fp.close()
    mails = mails.rstrip()   ### remove extra space,nelines from right side of string
    mail_ids = mails.split('\n')  ### create a list of mail ids...
    
    #mail_ids = ['bibhu2.dash']
    for mail in mail_ids:
        send_mail(mail)

def send_mail(mail_id):
    strFrom = 'GFX_STABILITY'  ## this is will show in mail from this name mail came
    strTo = mail_id + '@outlook.com'
    msgRoot = MIMEMultipart('related')
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo
    print(msgRoot['To'])
    strCc = 'SomeOne@outlook.com'
    msgRoot['Cc'] = strCc
    
    TC = get_test_case.test_case_name()
    target = target_and_Build_ID.get_Target()
    Build_Info = target_and_Build_ID.Build_ID()
    snapshots = gpu_snapshot_count.GPU_SNAPSHOTS()
    kgsl_snip = kgsl_logs.kgsl_snippet()
    
    hostname = subprocess.check_output('hostname',shell = True)
    hostname = hostname.rstrip()
    msgRoot['Subject'] = hostname + ': ' + target + '--> Stability Completed'
    
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)
    
    mail_content = '''
    TEST CASE:   {}
    ======================================
    {}
    "GPU Snapshots":  {}
    
    KGSL snippet:
    +++++++++++++++++++++++++++++++++++++++
    {}
    +++++++++++++++++++++++++++++++++++++++
    '''
    
    msgText = MIMEText(mail_content.format(TC, target, Build_Info, snapshots, kgsl_snip))
    #msgText = MIMEText('This is a plain test text message.')
    msgAlternative.attach(msgText)
    
    smtp = smtplib.SMTP()
    smtp.connect('smtphost.something.com')
    smtp.sendmail(strFrom, [strTo]+[strCc], msgRoot.as_string())
    smtp.quit()

#if __name__ == '__main__':
#   main()

trigger()

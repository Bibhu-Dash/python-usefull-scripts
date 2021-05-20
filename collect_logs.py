
import subprocess
import time
import os
import sys
import shutil

KMSG = 'start "kmsg_log" cmd /c "adb shell logcat -b kernel 2>&1 | tee '+ time.strftime("%Y%m%d-%H.%M.%S")+'_kmsg.txt'
KMSG_KILL = 'taskkill /IM cmd.exe /FI "WINDOWTITLE eq kmsg_log"'
LCAT = 'start "logcat_log" cmd /c "adb shell logcat -v threadtime 2>&1 | tee '+ time.strftime("%Y%m%d-%H.%M.%S")+'_logcat.txt'
LCAT_KILL = 'taskkill /IM cmd.exe /FI "WINDOWTITLE eq logcat_log"'

CLR_LCAT = 'adb logcat -c'
CLR_KMSG = 'adb shell logcat -b kernel -c'

def main():
    clear_logs()
    print('Please enter time to collect logs:')
    print('           ---> 1 . FC = 72000 sec')
    print('           ---> 2 . CS = 144000 sec')
    print('           ---> 3 . Enter Specific time collect logs in seconds')
    x = input('Please enter 1 or 2 or 3 ---> ')
    if x == 1:
        collect_log_for_time = 72000
        print('Collecting logs for {} secs'.format(collect_log_for_time))
    elif x == 2:
        collect_log_for_time = 144000
        print('Collecting logs for {} secs'.format(collect_log_for_time))
    elif x == 3:
        collect_log_for_time = input('Enter your time in seconds')
        print('Collecting logs for {} secs'.format(collect_log_for_time))
    else:
        print('Please enter a valid input 1 or 2 or 3')
        sys.exit()
    
    t0 = time.time()    ### this will get the current time
    t = 0
    collect_logs()
    while(t < collect_log_for_time):
        t1 = time.time()
        t = t1 - t0
    kill_logs()
    time.sleep(1)

def clear_logs():
    subprocess.call(CLR_LCAT)
    subprocess.call(CLR_KMSG)

def collect_logs():
    #Enable developer option and increase log buffer
    subprocess.call('adb shell setting put global development_settings_enabled 1')
    subprocess.call('adb shell logcat -G 16M')
    #Start logcat and kmsg logging
    subprocess.Popen(KMSG, stdin=None, stderr=None, shell=True)
    subprocess.Popen(LCAT, stdin=None, stderr=None, shell=True)
    
def kill_logs():
    subprocess.call(KMSG_KILL)
    subprocess.call(LCAT_KILL)

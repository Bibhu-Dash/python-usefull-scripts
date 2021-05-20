import os
import subprocess
import sys
import shutil

path = sys.argv[1]

os.chdir(path)

files = os.listdir()
l=len(files)
print(files)
print('Number of files = {}'.format(l))

for i in range(l):
	os.system('mkdir {}'.format(i))
	shutil.move('{}'.format(files[i]),'{}'.format(i))



#files_count.py <path>
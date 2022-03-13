import os
import platform
import datetime
import subprocess

res01 = os.popen("git add --all")

print(res01.read())

platForm = platform.system()
dateTime = datetime.datetime.now()
command = f'git commit -m "{dateTime}-{platForm}-"{"first_backup"}'

# res02 = os.popen(command)
# res = res02.read()

p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

res = p.stdout.read()

print(res)

res03 = os.popen("git push")

print(res03.read())

# git log --pretty=format:"%h - %an, %ar : %s"


# 此处仅仅用于build exe程序用， S2 环境已经损坏
# res04 = os.popen("git reset --hard")
# print(res04)
#
# res05 = os.popen("git pull")
# print(res05)

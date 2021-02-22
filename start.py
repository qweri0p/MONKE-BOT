import os
import platform
done=False
system = platform.system()
while not done:
    if system==("Windows"):
        os.system("python MONKBOT.py")
    else:
        os.system("python3 MONKBOT.PY")
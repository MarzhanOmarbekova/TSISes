# 3 Write a Python program to drop microseconds from datetime.

from datetime import  *
today = datetime.now()
print(today.strftime("%Y-%m-%d %H:%M:%S"))
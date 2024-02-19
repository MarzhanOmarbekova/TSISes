# 2 Write a Python program to print yesterday, today, tomorrow.

from datetime import  *
today = datetime.now()
yesterday = today - timedelta(days=1)
print(yesterday)
tomorrow = today + timedelta(days=1)
print(tomorrow)
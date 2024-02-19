# 1 Write a Python program to subtract five days from current date.
from datetime import  *
today = datetime.now()
days_5_from_2day = today - timedelta(days=5)
print(days_5_from_2day)
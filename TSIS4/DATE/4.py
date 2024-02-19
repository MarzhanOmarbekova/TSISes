# 4 Write a Python program to calculate two date difference in seconds.

from datetime import  *
today = datetime.now()
yesterday = today - timedelta(days = 1)
diff = today - yesterday 
print(diff.total_seconds())
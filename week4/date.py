from datetime import datetime, timedelta

'''x = datetime.today()
new = x - timedelta(days=5)
print(new.strftime("%d"))'''

'''
today = datetime.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print( yesterday.strftime("%Y-%m-%d"))
print(today.strftime("%Y-%m-%d"))
print(tomorrow.strftime("%Y-%m-%d"))'''

'''
x = datetime.now()
without_microseconds = x.replace(microsecond=0)
print(x)
print(without_microseconds)'''
'''
x = datetime(2024, 2, 15, 12, 0, 0) 
y = datetime(2024, 2, 21, 15, 30, 0)
diff = abs((y - x).total_seconds())
print(diff)'''

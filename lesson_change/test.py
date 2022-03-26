from datetime import datetime
from time import time

now = datetime.now()
timenow = now.strftime("%H:%M")
print(timenow)
if "08:00" > timenow:
    print("true")
else: 
    print("false")
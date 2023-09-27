# Version 3
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

def get_language():
    pass

class TimeC():
    def __init__(self, label):
        self.current_time = current_time
        self.label = label
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)



import time

वेळ = int(time.strftime('%H'))

if वेळ > 23:
    print("hoo")
else:
    print("nahi")


from datetime import datetime

# Assuming the current time is 2:18:57
current_time = datetime.now().time()

# Set the target time for comparison
target_time = datetime.strptime("15:00:00", "%H:%M:%S").time()

if current_time >= target_time:
    print("Good Afternoon")
else:
    print("Hello")

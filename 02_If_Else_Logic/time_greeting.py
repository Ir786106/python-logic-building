import datetime

now=datetime.datetime.now()
hour=now.hour

username="M. Irfan Waseem"

print("Current time:", now.strftime("%Y-%m-%d %H:%M:%S"))
if 5<= hour <12:
    print(f"Good Morning {username}!")
elif 12<= hour <5:
    print(f"Good Afternoon {username}!")
elif 5<= hour <9:
    print(f"Good Evening {username}!")
else:
    print(f"Good Night {username}!")
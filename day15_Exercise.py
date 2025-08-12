import time

current_time = time.strftime("%H:%M:%S")
print(current_time)

curr_Hour = int(time.strftime("%H"))

if curr_Hour < 12:
    print("Good Morning Sir.")
elif curr_Hour < 17:
    print("Good Afternoon Sir.")
else:
    print("Good Evening Sir")

# print(time.localtime())
now = time.localtime()
print(time.strftime("%Y-%m-%d %H:%M:%S", now))


print("Current time:", time.ctime())

start = time.time()
time.sleep(2)
end = time.time()

print("Slept for", end - start, "seconds")

import time


t = time.localtime()
formated_time = time.strftime("%Y-%m-%d %H:%H:%S", t)
print(formated_time)

# print(4)
# time.sleep(2)
# print("This is printed after 2 seconds.")


# def whileloop():
#     i = 0
#     while i < 20000:
#         print(i)
#         i += 1


# def forloop():
#     for i in range(20000):
#         print(i)


# start_time = time.time()  # give time in seconds since 1970
# whileloop()
# t1 = time.time() - start_time
# start_time2 = time.time()  # give time in seconds since 1970
# forloop()
# t2 = time.time() - start_time2

# print(f"While Loop : {t1}s")
# print(f"For Loop : {t2}s")

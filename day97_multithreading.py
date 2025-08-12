import threading
import time

# Multithreading in Python
# Multithreading is a technique in programming that allows multiple threads of execution to run concurrently within a single process. In Python, we can use the threading module to implement multithreading. In this tutorial, we will take a closer look at the threading module and its various functions and how they can be used in Python.


def func1(s):
    print(f"Sleeping for {s} seconds.")
    time.sleep(s)


def func2(s):
    print(f"Sleeping for {s} seconds.")
    time.sleep(s)


def func3(s):
    print(f"Sleeping for {s} seconds.")
    time.sleep(s)


# Normal Coding

# time1 = time.perf_counter()
# func1(4)
# func2(2)
# func3(1)
# time2 = time.perf_counter()
# print(f"Time taken to execute all functions : {time2-time1}")

# Same Codde Using Threads

time1 = time.perf_counter()
t1 = threading.Thread(target=func1, args=[4])
t2 = threading.Thread(target=func2, args=[2])
t3 = threading.Thread(target=func3, args=[1])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
time2 = time.perf_counter()
print(f"Time taken to execute all functions Using Threads : {time2-time1}")

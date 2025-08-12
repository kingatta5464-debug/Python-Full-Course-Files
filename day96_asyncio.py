import time
import asyncio

# 🧠 Simple Explanation of asyncio in Python
# Let’s imagine you are doing your homework and waiting for your pizza delivery at the same time.

# In normal (blocking) Python: You do your homework, but stop doing it until the pizza arrives.

# In asyncio (non-blocking): You do your homework while waiting for the pizza. Once the pizza arrives, you quickly get it, then continue your work.

# So, asyncio lets your program do many things at once, especially things that take time, like:

# Downloading from the internet

# Reading files

# Talking to a database

# Waiting for user input


# 🧠 What is asyncio?
# asyncio helps you run multiple tasks at the same time in Python, especially when tasks involve waiting (like downloading stuff, waiting for messages, etc).

# for example


def cooking():
    print("Started Cooking.")
    time.sleep(3)
    print("Cooking done.")


def Washing():
    print("Started Washing.")
    time.sleep(2)
    print("Washing done.")


def main():
    cooking()
    Washing()


main()

# This upper program waits for cooking to finish before washing dishes.
# total time = 3 + 2 = 5 seconds

print("\nWITH ASYNCIO FUNCTION\n")


# In this lower program both cooking and washing execute simultaneously which will decrease the execution time of program
async def cooking():
    print("Started Cooking.")
    await asyncio.sleep(3)
    print("Cooking done.")


async def Washing():
    print("Started Washing.")
    await asyncio.sleep(2)
    print("Washing done.")


async def main():
    await asyncio.gather(cooking(), Washing())


asyncio.run(main())


# An Other Example


async def order_pizza():
    print("📞 Orderd a Pizza...")
    await asyncio.sleep(4)
    print("🍕 Pizza delivered!")


async def watch_youtube():
    for i in range(5):
        print(f"📺 Watching YouTube video {i+1}")
        await asyncio.sleep(1)


async def main():
    await asyncio.gather(order_pizza(), watch_youtube())


asyncio.run(main())

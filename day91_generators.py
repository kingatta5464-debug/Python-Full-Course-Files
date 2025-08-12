# Generators in Python are a simple and powerful way to create iterators. Instead of returning all values at once (like a list), generators yield values one at a time using the yield keyword. This makes them memory-efficient, especially for large data sets.

# 🔧 Key Concepts:
# ✅ Normal Function vs Generator Function:
# Normal function uses return → returns value once, then terminates.

# Generator function uses yield → pauses the function and remembers where it left off, so it can resume later.


def my_generator():
    for i in range(5):
        yield i


gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))


# ✅ Why Use Generators?
# Feature	Benefit
# yield	Saves memory (doesn’t store all values)
# Lazy evaluation	Computes values only when needed
# Infinite sequences	Can generate values forever without crashing

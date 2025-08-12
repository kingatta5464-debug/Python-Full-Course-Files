import os

for i in range(0, 100):
    os.rename(f"OsModule/day{i+1}.png", f"OsModule/day{i+1}.txt")

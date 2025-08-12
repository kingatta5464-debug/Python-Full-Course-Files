import os

os.mkdir("OsModule")
for i in range(0, 100):
    os.mkdir(f"OsModule/day{i+1}.png")

for i in range(0, 10):
    os.mkdir(f"OsModule/tutorial{i+1}.txt")

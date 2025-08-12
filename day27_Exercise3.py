que = [
    "Pakistan Independence Year?",
    "Founder Of Pakistan?",
    "Total Provinces Of Pakistan?",
    "Pakistan's Largest Province?",
]

ans = ["1947", "Quaid-e-Azam", "4", "Balochistan"]

options = [
    ["1946", "1947", "1948", "1949"],
    ["Quaid-e-Azam", "Allama Iqbal", "Faiz Ahmad", "Fatimah Jinnah"],
    ["3", "2", "1", "4"],
    ["Balochistan", "Punjab", "Sindh", "Sarhad"],
]

ind = 0
Earning = 0

for i in que:
    print(i)
    coptions = 1
    for j in options[ind]:
        print(coptions, ".", j)
        coptions += 1
    x = int(input("Select An Option : "))
    while x > 4 or x < 1:
        print("Choose Only from 1-4")
        x = int(input("Select An Option Again : "))
    cans = options[ind][x - 1]
    if cans == ans[ind]:
        print("Correct! You Earned 2000 Rs.")
        Earning += 2000
    else:
        print("Wrong Answer")
    ind += 1


print("Your Total Earning Is : ", Earning)

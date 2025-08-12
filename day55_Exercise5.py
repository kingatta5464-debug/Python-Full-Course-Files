import random


def name(x):
    if x == "s":
        return "Sanke"
    elif x == "w":
        return "Water"
    else:
        return "Gun"


print("\nSNAKE WATER GUN GAME\n")
total_rounds = int(input("How Many Rounds From 1-10 You Wanna Play? \n"))
while total_rounds > 10 or total_rounds < 1:
    print("Your Rounds Are Not In Rage!")
    total_rounds = int(input("Please Select Again Only From 1-10 : \n"))
x = 1
computer_scores = 0
user_scores = 0
while x <= total_rounds:
    choices = ["s", "w", "g"]
    comp_selection = random.choice(choices)
    comp_selection = comp_selection.lower()
    my_choice = input("S. Snake\nW. Water\nG. Gun\nSelect S, W or G\n")
    my_choice = my_choice.lower()
    while my_choice != "s" and my_choice != "w" and my_choice != "g":
        my_choice = input("Select again only from S, W and G : \n")
    print("User Choose : ", name(my_choice))
    print("Computer Choose : ", name(comp_selection))
    if comp_selection == my_choice:
        print("Draw")
    elif comp_selection == "s" and my_choice == "w":
        print("Computer Won")
        computer_scores += 1
    elif comp_selection == "w" and my_choice == "g":
        print("Computer won")
        computer_scores += 1
    elif comp_selection == "w" and my_choice == "g":
        print("Computer won")
        computer_scores += 1
    else:
        print("User won")
        user_scores += 1
    x += 1

print("FINAL RESULTS")
print("Computer Total Scores : ", computer_scores)
print("User Total Scores : ", user_scores)
if user_scores > computer_scores:
    print("🎉 User win!")
elif user_scores < computer_scores:
    print("Computer Won The Game\n😞 You lose.")
else:
    print("😐 It's a draw.")

import random

pilihan = ["gunting", "batu", "kertas"]
bot = random.choice(pilihan)

user = input("your choice: ").lower()

if user not in pilihan:
    print("invalid input")
    exit()

if user == bot:
    result = "draw"
elif user == "batu" and bot == "kertas":
    result = "lose"
elif user == "gunting" and bot == "batu":
    result = "lose"
elif user == "kertas" and bot == "gunting":
    result = "lose"
else:
    result = "win"

print("user:", user)
print("bot :", bot)
print("result:", result)

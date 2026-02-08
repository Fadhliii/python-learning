import random
#TODO:choose one of word from this list
hewan = [
    "harimau",
    "gajah",
    "singa",
    "jerapah",
    "kucing",
    "anjing",
    "kelinci",
    "burung kolibri",
    "hiu"
]
#bot input
bot = random.choice(hewan)
print(bot)
#user input\
#word length
length = len(bot) #c:to counnt length of choosen list
#placeholder
placeholder = ""
for hewans in range(length):
    placeholder += "_ | "
print(placeholder)


# gameover = False
# display = ""
# while not gameover:
#     user = input("input hewan :").lower()
#     for i in bot:
#         if i == user:
#             display += i
#         else:
#             display += " _ " 
#     print(display)
    
#     # continue

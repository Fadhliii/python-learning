import random

pilihan = ["batu", "gunting", "kertas"]

print("🔥=== GAME SUIT  ===🔥")
print("Pilih: batu ✊ | gunting ✌️ | kertas ✋")
outgame = "Ketik 'exit' kalau udah bosen main\n"

while True:
    user = input("Pilihan : ").lower().strip()
    bot = random.choice(pilihan).lower()
    print("┌" + "─" * 20 + "┐")
    print("|"f"User pilih : {user}")
    print("|"f"Bot pilih : {bot}")
    print("└" + "─" * 20 + "┘")
    # user exit 
    if user == "exit":
        print("\nMakasih udah main bareng! 👋✨ Sampai ketemu lagi ya~")
        break
    #user invalid input
    if user not in pilihan:
        print("Inputnya salah tuh. ulangi lagi ya TQ")
        continue
    #user in match
    #input user
    if user == bot:
        print("wah seri nih matchnya 🔥")
    elif (user == "gunting" and bot == "kertas") or \
        (user == "batu" and bot == "gunting") or \
        (user == "kertas" and bot == "batu"):
        print("🏆🏆 yeay menang !🏆🏆")
    else:
        print(" 💔💔 kurang bentung, coba lagi deh 💔💔 ")        
        
    print(outgame)
    
    
print()
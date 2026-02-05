import random
import string

letters = list(string.ascii_lowercase)
n_letters = int(input("choose jumlah letter : \n"))

numbers = list(string.digits)
n_numbers = int(input("choose jumlah nomor  : "))

symbols = list(string.punctuation)
n_symbols = int(input("choose jumlah simbol : "))

pw = ""
for char in range(0, n_letters):
    pw += random.choice(letters)
    
for char in range(0, n_numbers):
    pw += random.choice(numbers)
    
for char in range(0, n_symbols):
    pw += random.choice(symbols)
    
print(pw)
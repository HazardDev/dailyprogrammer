

letters = "abcdefghijklmnopqrstuvwxyz"

limit = 26
strnow = "a"
for letter in range(limit):
    if letter == 0: continue
    print(strnow)
    strnow = strnow[:(len(strnow)//2)+1] + letters[letter] + strnow[(len(strnow)//2)::-1]

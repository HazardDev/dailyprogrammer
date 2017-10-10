letters = "abcdefghijklmnopqrstuvwxyz"
for letter in range(26):
    strnow = strnow + letters[letter] + strnow
open("output.txt", "w").write(strnow)

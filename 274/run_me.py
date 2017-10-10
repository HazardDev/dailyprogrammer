declaration = open("declaration.txt", "r").read().split(" ")
cipher = open("cipher.txt", "r").read().split(", ")

decipher = ""
for i in cipher:
    decipher = decipher + declaration[int(i) - 1][0]

open("output.txt", "w").write(decipher)



nums = input()
an_ar = nums.split(" ")

print(an_ar)

def compare(a, b):
    return int(a + b) > int(b + a) #Returns true if a concat b is larger than b concat a

swap = 0

for i in range(len(an_ar) - 1):
    for x in range(len(an_ar) - 1):
        if not compare(an_ar[x], an_ar[x+1]):
            swap += 1
            temp = an_ar[x]
            an_ar[x] = an_ar[x+1]
            an_ar[x+1] = temp

print("".join(an_ar))
an_ar.reverse()
print("".join(an_ar))
print(swap)
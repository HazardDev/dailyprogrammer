
# def xormult(a, b):
#     print(a, b)
#     a = str(bin(a))[2:]
#     b = str(bin(b))[2:]
#     print(a, b)
#     values = []
#     for i in range(len(a)):
#         build = ""
#         for x in range(len(b)):
#             build = str(int(a[i]) * int(b[x])) + build
#         values.append(build)



#     return values

def xormult(a, b):
    a = str(bin(a))[2:]
    b = str(bin(b))[2:]
    return int(a) * int(b)



val = xormult(14, 13)

print(val)
import random
from itertools import permutations

def cyclic_perm(a):
    n = len(a)
    b = [[a[i - j] for i in range(n)] for j in range(n)]
    return b

CHNAMES = ['Smash Or Pass', 'Scrisoare de amor', 'Date-ul ideal',
           'Desen', 'Red flags', 'Cantece']
namelist = open("nume.txt", 'r', encoding = "utf-8").read()
namelist = namelist.split('\n')
listlen = len(namelist)
challenges = 6;

#print(namelist)

if listlen % 2 != 0:
    print("bad input")
    exit()

listbase = namelist[:(listlen//2)]
list_cycle = namelist[(listlen//2):listlen]
#print(list_cycle)

perms = list(cyclic_perm(list_cycle))
revperms = list(cyclic_perm(list_cycle[::-1]))
perms = perms + revperms

permslen = len(perms)
#(perms)
pairs = [[[listbase[i], perms[k % permslen][i]] for i in range(listlen // 2)] for k in range(challenges)]
print(pairs)

out = open("perechi.txt", "w", encoding = "utf-8")

for i in range(challenges):
    out.write("Challenge " + CHNAMES[i] + ":\n")
    for k in range(listlen // 2):
        out.write(str(pairs[i][k][0]) + " - " + str(pairs[i][k][1]) + "\n")
    out.write("\n")
out.close()

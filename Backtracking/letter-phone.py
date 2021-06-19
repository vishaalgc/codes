
# 234
# 2 -> abc
# 3 -> def
# 4 -> ghi

# Possible combinations
# adg     b       c
# adh
# adi
# aeg
# aeh
# aei
# afg
# afh
# afi


def recur(targetLength,A,lt,results):
    print(A,lt)
    if len(lt) == targetLength:
        results.append(''.join(lt))
    else:
        for j in range(len(A)):
            item = A[j]
            for k in range(len(item)):
                insideItem = item[k]
                lt.append(insideItem)
                del item[k]
                recur(targetLength,A[j+1:],lt,results)
                del lt[-1]
                item.insert(k,insideItem)

st = "22"
mp = {}
mp[1] = []
mp[2] = ['a','b','c']
mp[3] = ['d','e','f']
mp[4] = ['g','h','i']
mp[5] = ['j','k','l']
mp[6] = ['m','n','o']
mp[7] = ['p','q','r','s']
mp[8] = ['t','u','v']
mp[9] = ['w','x','y','z']

A = []
for i in st:
    i = int(i)
    A.append(list(mp[i]))

lt = []
results = []
k = len(st)
recur(k,A,lt,results)
print(results)


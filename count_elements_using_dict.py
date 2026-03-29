arr = [1,2,1,3,2,1]
freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1        #freq[num] = 1, Create a new key = num and assign value = 1
print(freq)

s='banana'
f={}
for ch in s:
    if ch in f:
        f[ch] +=1
    else:
        f[ch]=1
print(f)
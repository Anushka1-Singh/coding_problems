s1=input("enter first string : ")
s2=input("enter first string : ")
if len(s1)!=len(s2):
    print("not an anagram")
else:
    freq={}
    # count characters of first string
    for ch in s1:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    # substract using second string
    for ch in s2:
        if ch in freq:
            freq[ch]-=1
        else:
            print("not an anagram")
            break
    else:
        # final check
        all_zero=True
        for key in freq:
            if freq[key]!=0:
                all_zero=False
                break
        if all_zero:
            print("anagram")
        else:
            print("not anagram")

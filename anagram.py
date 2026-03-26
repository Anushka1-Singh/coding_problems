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

# OR 
def are_anagram(str1,str2):
    # remove spaces and convert to lower case
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()
    
    # must have equal lengths to be anagrams
    if len(str1) != len(str2):
        return False
    # compare character frequency counts
    return sorted(str1)==sorted(str2)
# test cases
test_pairs =[
    ('listen','silent'),
    ('hello','world'),
    ('astronomer','moon starer'),
    ('abc','ab'),
    ('dormitory','dirty room',)
]
for sh1,sh2 in test_pairs:
    result=are_anagram(sh1,sh2)
    print(f'"{s1}"&"{s2}" -> {" anagram" if result else" not an anagram"}')

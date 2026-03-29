sentence = "  she  is  a  girl  "
if sentence == "":
    print("empty sentence")
else:
    count = 0
    for i in range(len(sentence)):
        # condition 1: current character must not be a space
        # condition 2: either it is the first character
        #              OR the previous character was a space
        # if both are true → a new word is starting → count it
        if sentence[i] != " " and (i == 0 or sentence[i-1] == " "):#A new word begins the moment you see a non-space character after a space character
            count += 1                                             #i == 0 is a safety check — it says "if we are at the very first character, don't look behind, just count it as a word start directly"
    print("number of words:", count)
#**Visualising the condition on `"  she  is  a  girl  "`:**
#i=0  → ' '  → space        → condition 1 fails → skip
#i=1  → ' '  → space        → condition 1 fails → skip
#i=2  → 's'  → not space ✓  → prev=' ' ✓        → NEW WORD → count=1
#i=3  → 'h'  → not space ✓  → prev='s' ✗        → skip
#i=4  → 'e'  → not space ✓  → prev='h' ✗        → skip
#i=5  → ' '  → space        → condition 1 fails → skip
#i=6  → ' '  → space        → condition 1 fails → skip
#i=7  → 'i'  → not space ✓  → prev=' ' ✓        → NEW WORD → count=2
#i=8  → 's'  → not space ✓  → prev='i' ✗        → skip
#i=9  → ' '  → space        → condition 1 fails → skip
#i=10 → ' '  → space        → condition 1 fails → skip
#i=11 → 'a'  → not space ✓  → prev=' ' ✓        → NEW WORD → count=3
#i=12 → ' '  → space        → condition 1 fails → skip
#i=13 → ' '  → space        → condition 1 fails → skip
#i=14 → 'g'  → not space ✓  → prev=' ' ✓        → NEW WORD → count=4
#i=15 → 'i'  → not space ✓  → prev='g' ✗        → skip
#i=16 → 'r'  → not space ✓  → prev='i' ✗        → skip
#i=17 → 'l'  → not space ✓  → prev='r' ✗        → skip
#i=18 → ' '  → space        → condition 1 fails → skip
#i=19 → ' '  → space        → condition 1 fails → skip
#Output: number of words: 4  ✓
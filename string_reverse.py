#adding the new character in front, not at the end.
#So each new character pushes previous characters to the right → creating a reversed string.
s='rohit'
reversed_s=''
for char in s:
    reversed_s=char+reversed_s  
print(reversed_s)

def reverse_string(s):
    reversed_s = ''
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s
test_cases = [
    "rohit",        # normal
    "",             # empty
    "a",            # single char
    "ab",           # two chars
    "madam",        # palindrome
    "hello world",  # spaces
    "a@b#c!",       # special chars
    "12345",        # numbers
    "ab12#c",       # mixed
    "AbC"           # case sensitivity
]
for test in test_cases:
    result = reverse_string(test)
    print(f"Input: '{test}' -> Output: '{result}'")

# reversed built in method which returns the reverse string
s1 = 'rohit'
reversed_s1 =reversed(s1)   #give you characters in reverse… but only when you ask for them one by one”
print(reversed_s1)          # reversed_s1 : An iterator is an object that produces items one at a time, on demand, instead of storing them all at once.

s2 = "rohit"
for char in reversed(s2):
    print(char, end='')     # end= After printing this, append this string instead of going to next line


# while loop
s3='rohit'
reversed_s3=''
i=len(s3)-1
while i>=0:
    reversed_s3 += s3[i]
    i -= 1
print(reversed_s3,'using while loop')

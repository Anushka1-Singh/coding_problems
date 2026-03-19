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
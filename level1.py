def solution(x):
    # Your code here
    if not isinstance(x, str):
        raise TypeError
    plain_alphabet = "abcdefghijklmnopqrstuvwxyz"
    code_alphabet =  "zyxwvutsrqponmlkjihgfedcba"
    res = ""
    for char in x:
        if char not in plain_alphabet:
            res += char
        else:
            i = code_alphabet.index(char)
            res += plain_alphabet[i]
    return res

sol1 = solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
sol2 = solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
print(sol1, sol2)
# done

def repeated(s):
    chars = {}
    for char in s:
        chars.update({char: chars[char] + 1 if char in chars else 1})
    return chars

print(f'Частота букв{repeated("beep beep boop beer")}')

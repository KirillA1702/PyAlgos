# done

def sub_strings(arr):

    cnt = []
    leng = len(arr)
    for i in range(leng):
        for j in range(i + 1, leng + 1):
            cnt.append(hash(arr[i:j]))

    return len(set(cnt) - {hash(arr)})


arr = 'Python'
print(f'В строке "{arr}" {sub_strings(arr)} подстрок')

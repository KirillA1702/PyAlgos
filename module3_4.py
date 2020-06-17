# done

import random

array = []
x = 50
while x != 0:
    gen_numb = random.randint(0, 50)
    array.append(gen_numb)
    x -= 1

def repeated(numb):
    result = dict((numb.count(i), i) for i in list(numb))
    return result[max(result.keys())]

print(repeated(array))

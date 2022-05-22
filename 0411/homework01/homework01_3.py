# homework01_3.py

def test(i, j):
    return i*j

i = 3
j = 2
k = test(i, j)
if(k > 5): print('>5\n')
else: print('<=5\n')

cont = 0
num = 7
for i in range (1, 10, 2):
    print('I=%d J=%d' %(i, num))
    print('I=%d J=%d' %(i, num-1))
    print('I=%d J=%d' %(i, num-2))
    num += 2
n = 1 
rodada = cont_g = cont_i = cont_e = 0 
while n == 1:
    gi, gg = map(int, input().split())
    if gi > gg: 
        cont_i += 1
    elif gg > gi:
        cont_g += 1
    elif gi == gg:
        cont_e += 1
    print('Novo grenal (1-sim 2-nao)')
    n = int(input())
    rodada += 1
    
print('%d grenais' %rodada)
print('Inter:%d' %cont_i)
print('Gremio:%d' %cont_g)
print('Empates:%d' %cont_e)
if cont_i == cont_g:
    print('Nao houve vencedor')
elif cont_g > cont_i: 
    print('Gremio venceu mais')
else:
    print('Inter venceu mais')
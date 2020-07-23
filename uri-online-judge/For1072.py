n = int(input())

cont_in = cont_out = 0
cont = 0

while cont < n:
    
    valor = int(input())
    if 10 <= valor <= 20:
        cont_in += 1
    else:
        cont_out += 1
    
    cont += 1

print('%d IN' %cont_in)
print('%d OUT' %cont_out)


quantidade_dias = int(input())
ano = quantidade_dias // 365
meses = quantidade_dias % 365
meses_final = meses // 30
dias = meses % 30

print('%d ano(s)' %ano)
print('%d mes(es)' %meses_final)
print('%d dia(s)' %dias)

a = int(input("Informe o diâmetro da Flange:"))



print("Espessura da Flange:")
if a <= 50:
    print(2)
if a > 50 and a <= 100:
    print(3)
if a > 100 and a <= 150:
    print(4)
if a > 150 and a <= 200:
    print(5)
if a > 200:
    print(6)
    
    
    
print("Diâmetro do Pescoço:")
print(a/2)

print("Altura do Pescoço:")
print(a*2)

print("Posição dos Furos:")
print(a*85/100)



print("Quantidade de Furos:")
if a <= 50:
    print(0)
if a > 50 and a <= 100:
    print(2)
if a > 100 and a <= 150:
    print(4)
if a > 150 and a <= 200:
    print(6)
if a > 200:
    print(8)
    
    
    
print("Diâmetro do Furo")
if a <= 50:
    print(0)
if a > 50 and a <= 100:
    print(4)
if a > 100 and a <= 150:
    print(6)
if a > 150 and a <= 200:
    print(8)
if a > 200:
    print(10)
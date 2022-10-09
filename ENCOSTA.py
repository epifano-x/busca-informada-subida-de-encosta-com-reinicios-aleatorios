import random

valoraleatorio = random.randint(0,200)/10
x = valoraleatorio
f = -x**8 + 77*x**7 - 2451*x**6 + 41817*x**5 - 414849*x**4 + 2429223*x**3 - 8130689*x**2 + 14117683*x - 9699690
print('____________________________________________')
print('valor  inicial de x sorteado',x)
print('____________________________________________')
i = 1 
contador = 0
for x in range(100000):
    x = valoraleatorio
    v1 = -x**8 + 77*x**7 - 2451*x**6 + 41817*x**5 - 414849*x**4 + 2429223*x**3 - 8130689*x**2 + 14117683*x - 9699690
    x = valoraleatorio-0.1
    v2 = -x**8 + 77*x**7 - 2451*x**6 + 41817*x**5 - 414849*x**4 + 2429223*x**3 - 8130689*x**2 + 14117683*x - 9699690
    x = valoraleatorio+0.1
    v3 = -x**8 + 77*x**7 - 2451*x**6 + 41817*x**5 - 414849*x**4 + 2429223*x**3 - 8130689*x**2 + 14117683*x - 9699690
    print('____________________________________________')
    print('reinicio de numero ->',contador)
    print('____________________________________________')
    print ('valor de v1 ->',v1)
    print ('valor de v2 ->',v2)
    print ('valor de v3 ->',v3)
    print('____________________________________________')
    if v2 > v1:
        valoraleatorio = valoraleatorio-0.1
        contador = contador+1
    elif v3 > v1:
        valoraleatorio = valoraleatorio+0.1
        contador = contador+1
    else:
        print('____________________________________________')
        print('ENCONTROU')
        break

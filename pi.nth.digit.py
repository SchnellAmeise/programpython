import math
while True:
    nth_pi = int(input("Até qual digito de PI você quer? "))
    if nth_pi <= 100:
        print("PI = {:.{}f}".format(math.pi, nth_pi))
    else:
        print("Número muito grande, tente outra vez.")
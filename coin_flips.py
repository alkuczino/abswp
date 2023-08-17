import random

def throw():
    throws = [random.randint(0,1) for _ in range(100)]
    orly=0
    reszki=0
    szostki=0
    for toss in throws:
        if toss == 0:
            reszki += 1
            orly = 0
        else:
            orly += 1
            reszki = 0
        if reszki == 6 or orly == 6:
            szostki += 1
    return szostki

if __name__ == '__main__':
    
    result = sum(throw() for _ in range(10000))
    precentage = result / 10000    
    print('Na 10000 prób 100 rzutów każda, było ' + str(result) + ' serii po 6 orłów lub reszek')
    print('Na 100 rzutów monetą występuje średnio ' + str(precentage) + ' serii po 6 orłów lub reszek')
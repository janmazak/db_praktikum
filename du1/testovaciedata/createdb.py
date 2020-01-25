import random
import datetime
import sys


POCET_PIJANOV = 20
POCET_ALKOHOLOV = 12
POCET_KRCIEM = 10
POCET_NAVSTEV = 10

lubi = []
pijani = []
alkoholy = []
cenyAlkoholov = {}
krcmy = []
navstevy = []

nextid = 1

random.seed()


def prepare_default():
    for i in range(1, POCET_PIJANOV+1):
        pijani.append('default_p' + str(i).zfill(2))
    for i in range(1, POCET_ALKOHOLOV+1):
        a = 'default_a' + str(i).zfill(2)
        alkoholy.append(a)
        cenyAlkoholov[a] = random.randint(1, 5)
    for i in range(1, POCET_KRCIEM+1):
        krcmy.append(('default_k' + str(i).zfill(2), sorted(random.sample(alkoholy, POCET_ALKOHOLOV // 2))))
    
    for i in range(POCET_PIJANOV):
        lubene = sorted(random.sample(alkoholy, len(alkoholy) // 2))
        for alkohol in lubene:
            lubi.append((pijani[i], alkohol))

    for i in range(POCET_PIJANOV):
        pijan = pijani[i]
        if i == 8: # drzgros
            krcma, alkoholykrcmy = krcmy[0]
            najlacnejsiAlkohol = alkoholykrcmy[0]
            for a in alkoholykrcmy:
                if cenyAlkoholov[a] < cenyAlkoholov[najlacnejsiAlkohol]:
                    najlacnejsiAlkohol = a
            for k in range(i):
                od = random.randint(1, 100) + datetime.datetime.now().microsecond/1000000.0
                navstevy.append((None, pijan, krcma, najlacnejsiAlkohol, random.randint(1, 100), od))            
        else:
            for j in range(POCET_KRCIEM):
                krcma, alkoholykrcmy = krcmy[j]
                for k in range(i):
                    vypite = sorted(random.sample(alkoholykrcmy, len(alkoholykrcmy) // 2))
                    od = random.randint(1, 100) + datetime.datetime.now().microsecond/1000000.0
                    for l in range(len(vypite)):
                        navstevy.append((None, pijan, krcma, vypite[l], random.randint(1, 100), od))

def prepare_a():
    newpijani = ['a_p1', 'a_p2']
    pijani.extend(newpijani)
    krcma, alkoholykrcmy = krcmy[0]
    for k in range(50):
        vypite = sorted(random.sample(alkoholykrcmy, len(alkoholykrcmy) // 2))
        od = random.randint(1, 100) + datetime.datetime.now().microsecond/1000000.0
        for l in range(len(vypite)):
            navstevy.append((None, 'a_p1', krcma, vypite[l], random.randint(1, 100), od))
    for alkohol in alkoholy:        
        for (krcma, alkoholykrcmy) in krcmy:
            if alkohol in alkoholykrcmy:
                od = random.randint(1, 100) + datetime.datetime.now().microsecond/1000000.0
                navstevy.append((None, 'a_p2', krcma, alkohol, random.randint(1, 10), od))
                break


def prepare_b():
    pijani.extend(['b_p1'])
    mnozstvo = 1
    od = 1
    for alkohol in alkoholy:        
        for (krcma, alkoholykrcmy) in krcmy:
            if alkohol in alkoholykrcmy:
                navstevy.append((None, 'b_p1', krcma, alkoholy[0], mnozstvo, od))
                mnozstvo += random.randint(0, 1)
                od += 1
    for i in range(5):
        pijan = 'b_p00' + str(i)
        pijani.append(pijan)
        krcma, alkoholykrcmy = krcmy[random.randint(0, len(krcmy)-1)]
        navstevy.append((None, pijan, krcma, alkoholykrcmy[random.randint(0, len(alkoholykrcmy)-1)], 47, 47))


def prepare_c():
    for (pijan, alkohol) in lubi:
        if pijan != 'default_p' + str(POCET_PIJANOV):
            continue
        for (krcma, alkoholykrcmy) in krcmy:
            if alkohol in alkoholykrcmy:
                od = random.randint(1, 100) + datetime.datetime.now().microsecond/1000000.0
                navstevy.append((None, pijan, krcma, alkohol, random.randint(101, 200), od))
    singlefail = False
    for (pijan, alkohol) in lubi:
        if pijan != 'default_p' + str(POCET_PIJANOV-1):
            continue        
        for (krcma, alkoholykrcmy) in krcmy:
            if alkohol in alkoholykrcmy:
                od = random.randint(1, 100) + datetime.datetime.now().microsecond/1000000.0
                if not singlefail:       
                    maxmnozstvo = -1
                    for (ident, p, k, a, m, od) in navstevy:
                        if a == alkohol and k == krcma:
                            if m > maxmnozstvo:
                                maxmnozstvo = m
                    mnozstvo = maxmnozstvo
                    singlefail = True
                else:
                    mnozstvo = random.randint(101, 200)
                navstevy.append((None, pijan, krcma, alkohol, mnozstvo, od))


def prepare_d():
    alkohol = list(cenyAlkoholov.keys())[0]
    krcmy.append(("d_k1", [alkohol]))
    navstevy.append((None, "d_p1", "d_k1", None, None, 5))


def print_db():
    for i in range(len(lubi)):
        print("lubi(" + lubi[i][0] + ", " + lubi[i][1] + ").")
    for i in range(len(krcmy)):
        krcma, alkoholykrcmy = krcmy[i]
        for j in range(len(alkoholykrcmy)):
            print("capuje(" + krcma + ", " + alkoholykrcmy[j] + ", " + str(cenyAlkoholov[alkoholykrcmy[j]]) + ").")
    navstivil = []
    vypil = []
    for (ident, p, k, a, m, od) in navstevy:
        if ident is None:
            global nextid
            ident = nextid
            nextid += 1
        navstivil.append("navstivil(" + str(ident) + ", " + p + ", " + k + ", " + str(od) + ").")
        if a != None:
            vypil.append("vypil(" + str(ident) + ", " + a + ", " + str(m) + ").")
    for s in navstivil:
        print(s)
    print("\n")
    for s in vypil:
        print(s)


prepare_default()
prepare_a()
prepare_b()
prepare_c()
prepare_d()

print_db()

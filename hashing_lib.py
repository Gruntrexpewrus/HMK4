# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 13:47:09 2019

@author: leona
"""

import sympy as s
m = s.nextprime(958505838)

import random

def randomizr(m): 
    vec = []
    for i in range(20):
        vec.append(random.randrange(m))
    return vec

vector1 = [238420765, 848925297, 784711979, 497093051, 95554829, 514988376, 892218180, 442524537, 607757090, 700296439, 596878981, 371686624, 439536567, 181541896, 635998009, 830467436, 782561980, 212875567, 392765566, 534916217]
vector2 = [667252919, 294923376, 857674523, 455499217, 487102145, 176035026, 223282253, 610577513, 707981282, 103967431, 812769808, 806736283, 479599574, 228782634, 441223920, 850329407, 434609601, 799716331, 671844433, 589053973]
vector3 = [399089958, 398452767, 51973215, 420884573, 883431994, 46306089, 445136725, 73819833, 460047188, 550915479, 840195322, 53305110, 523616283, 679027420, 164041420, 323692409, 850889656, 267436729, 530084757, 555947052]
vector4 = [360456327, 260340259, 556014589, 88632059, 675905187, 154700660, 558289546, 13412832, 496149736, 145965229, 410734023, 701177977, 523295721, 354015393, 31246611, 203541478, 811770871, 697524858, 38643469, 625709998]
vector5 = [198449539, 858931647, 111900049, 793153272, 72035689, 915892416, 386067109, 432145732, 786680161, 197524167, 560256363, 582699524, 801304152, 922568252, 471275982, 287382050, 691678402, 792317068, 475674805, 696631435]
vector6 = [897728679, 185242023, 563247529, 957415683, 275736323, 813059754, 874316063, 81158502, 858981714, 704621876, 782484058, 274547650, 73468298, 285239415, 467534053, 240265981, 85451921, 379450467, 815001741, 153710564]
vector7 = [667091761, 594599526, 417139662, 901299857, 576375979, 19784631, 532685751, 112057141, 475564085, 676246707, 478433915, 854391781, 953972748, 130700365, 732046487, 341923245, 95697728, 164619653, 90474761, 622232906]

def simple_dot(x,y):
    A = 0
    for i in range(20):
        #print(x[i])
        A = A +((x[i])*y[i])%m
    return(A%m)
    
def Hash1(x): 
    vec = []
    for i in x:
        vec.append(ord(i))
    return (simple_dot(vec,vector1))

def Hash2(x): 
    vec = []
    for i in x:
        vec.append(ord(i))
    return (simple_dot(vec,vector2))

def Hash3(x): 
    vec = []
    for i in x:
        vec.append(ord(i))
    return (simple_dot(vec,vector3))

def Hash4(x): 
    vec = []
    for i in x:
        vec.append(ord(i))
    return (simple_dot(vec,vector4))

def Hash5(x): 
    vec = []
    for i in x:
        vec.append(ord(i))
    return (simple_dot(vec,vector5))

def Hash6(x): 
    vec = []
    for i in x:
        vec.append(ord(i))
    return (simple_dot(vec,vector6))

def Hash7(x): 
    vec = []
    for i in x:
        vec.append(ord(i))
    return (simple_dot(vec,vector7))

import time
def BloomFilter(passwords1, passwords2):
    start = time.time()
    filtr = [0]*m #here m the module
    probably = 0
    ppos = []
    #first i put in my filter all the password from passwords1, signing with a 1 the components where there is something
    with open(passwords1) as infile:
        for line in infile:
            item = line.replace('\n','')
            filtr[Hash1(item)] = 1
            filtr[Hash2(item)] = 1
            filtr[Hash3(item)] = 1
            filtr[Hash4(item)] = 1
            filtr[Hash5(item)] = 1
            filtr[Hash6(item)] = 1
            filtr[Hash7(item)] = 1
    #now that every password from df passwords1 is inside, we have to put the new ones and count homw many are probably duplicates
    with open(passwords2) as infile:
        for line in infile:
            item = line.replace('\n','')
            if filtr[Hash1(item)] == 1:
                if filtr[Hash2(item)] == 1:
                    if filtr[Hash3(item)] == 1:
                        if filtr[Hash4(item)] == 1:
                            if filtr[Hash5(item)] == 1:
                                if filtr[Hash6(item)] == 1:
                                    if filtr[Hash7(item)] == 1:
                                        probably = probably + 1
                                        #we created the ppso list to end the bonus part quickly without rerun the code
                                        ppos.append(item)
    end = time.time()
    #for the probability of false positive we build the model from the passwords1 size and i false positive rate we wanted, so it's 1%
    print('Number of hash function used: ', 7)
    print('Number of duplicates detected: ', probably)
    print('Probability of false positives: ', 0.01)
    print('Execution time: ', end-start)
    return ppos


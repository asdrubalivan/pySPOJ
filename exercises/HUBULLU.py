# -*- coding: utf-8 -*-
'''
Created on 30/10/2012

@author: asdrubal
@todo: Aplicar función a iterable... (Multiplicar todos los valores de una lista)
'''
from collections import namedtuple
import sys

TestCase = namedtuple('TestCase', 'number pieces player')

class BadRange(Exception):
    pass

def getInput():
    try:
        N = int(input())
    except EOFError:
        return
    else:
#        if not 1 <= N <= 2000000000:
#            raise BadRange
        cases = []
        for i in range(1, N + 1):
            try:
                number = int(input())
            except EOFError:
                break
            try:
                pieces, player = [int(x) for x in input().split()]
            except EOFError:
                pass
            else:
                if not 0 <= player <= 1:
                    raise BadRange
                cases.append(TestCase(number, pieces, player))
    return tuple(cases)

def winner(case):
    if case.player == 0:
        print("Airbone wins.")
    elif case.player == 1:
        print ("Pagfloyd wins.")
        

if __name__ == '__main__':
    cases = getInput()
    for case in cases:
        winner(case)


    
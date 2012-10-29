'''
Created on 29/10/2012

@author: asdrubal
@see: Resolution of problem NY10A (code 8612) in python 3
@twitter: @asdrubalivan
'''
import itertools
import re


class BadRange(Exception):
    pass
def permutationsGame():
    return [''.join(cadena) for cadena in itertools.product('TH', repeat=3)]
def findEveryOverlapMatch(string, valueToFind):
    regex = "(?=%s)" % (valueToFind)
    return [match for match in re.findall(regex, string)]
def findAll(string):
    values = permutationsGame()
    return {value:len(findEveryOverlapMatch(string, value)) for value in values}
def getInput():
    '''
        Due to requisites at the online judge some operations
        may look redundant
    '''
    p = int(input())
    if not 1 <= p <= 1000:
        raise BadRange
    dictionary_input = {}
    for val in range(1, p + 1):
        case = int(input())
        string = input()
        dictionary_input[case] = string.upper()
    return dictionary_input
def output(dictionary):
    for key in sorted(dictionary.keys()):
        print(key,end=" ")
        printResults(dictionary[key])
def printResults(string):
    dictionary = findAll(string)
    for key in sorted(dictionary.keys(), reverse=True):
        print (dictionary[key], end=" ")
    print()
    
if __name__=="__main__":
    dictionary_output = getInput()
    output(dictionary_output)
    

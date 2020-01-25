import subprocess
import sys


def createTestableFile():
    with open('du1.pl', 'r') as inputfile:
        with open('du1-testable.pl', 'w') as outputfile:
            outputfile.write(
"""
:- consult('query.pl').
:- consult('subtotal.pl').
:- consult('pijani-test.pl').

""")
            outputfile.write(inputfile.read())


def processOutput(lines):
    solution = []
    for line in lines:
        if line.startswith('['):
            solution.append(line)
    return solution


def areDifferent(x, y):
    return sorted(x) != sorted(y)


def check(task):
    p = subprocess.Popen("swipl --quiet -s du1-testable.pl < test-" + task + ".pl", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, )
    stdout, stderr = p.communicate()
    solutionToTest = sorted(processOutput(stdout.decode('utf-8').split('\n')))
    with open('correctSolution-' + task + '.txt', 'r') as inputfile:
        correctSolution = sorted(processOutput([line.rstrip() for line in inputfile.readlines()]))
    
    if areDifferent(solutionToTest, correctSolution):
        print("\n\n******* wrong solution for " + task + ":\n")
        print("----- tested solution:")
        print(solutionToTest)
        print("----- correct solution:")
        print(correctSolution)
    else:
        print("\n\ncorrect solution for " + task + "\n")
        

def check_all(tasklist):    
    createTestableFile()
    for task in tasklist:
        check(task)
    print("\n\nEnd of test.")
    

if len(sys.argv) > 1:
    tasklist = [sys.argv[1]]
else:
    tasklist = ['a', 'b', 'c', 'd']
check_all(tasklist)

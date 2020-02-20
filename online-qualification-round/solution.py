import random

def scoresSorter(val):
    return val[1]

def libSorter(val):
    N = int(val[0][0])
    T = int(val[0][1])
    M = int(val[0][2])

    fitness = N * M / T

    return fitness

def readFile(filename):
    fp = open(filename)
    line = fp.readline().rstrip().split(' ')
    B = int(line[0])
    L = int(line[1])
    D = int(line[2])
    scores = fp.readline().rstrip().split(' ')
    scores = list(map(int, scores))

    libraries = []
    for i in range(0,L):
        lib = fp.readline().rstrip().split(' ')
        lib.append(i)
        books = fp.readline().rstrip().split(' ')
        books = list(map(int, books))
        
        booksScore = []
        for j in range(0, len(books)):
            booksScore.append([books[j], scores[books[j]]])

        booksScore.sort(key = scoresSorter, reverse = True )

        libraries.append([lib, booksScore])

    libraries.sort(key = libSorter, reverse = True)

    fp.close()
    return B, L, D, scores, libraries

def writeFile(filename, result):
    fout = filename[:-3] + '.out'
    fp = open(fout, "w")

    fp.write(str(len(result)) + '\n')

    for i in range(0, len(result)):
        fp.write(' '.join(map(str,result[i][0])) + '\n')
        fp.write(' '.join(map(str,result[i][1])) + '\n')

    fp.close()

def solve(B, L, D, scores, libraries):
    result = []

    for i in range(0, L):
        booksInLib = int(libraries[i][0][0])
        libID = [libraries[i][0][3], booksInLib]
        books = []
        for j in range(0, booksInLib):
            books.append(libraries[i][1][j][0])

        result.append([libID, books])

    return result


def run(file):
    B, L, D, scores, libraries = readFile("Input/"+file)

    result = solve(B, L, D, scores, libraries)

    writeFile("Output/" + file, result)

files = 'a_example.in  b_read_on.in  c_incunabula.in  d_tough_choices.in  e_so_many_books.in  f_libraries_of_the_world.in'.split('  ')

for f in files:
    print(f)
    run(f)
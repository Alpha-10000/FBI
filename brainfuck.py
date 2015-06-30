import sys
import getch
    
def findBrackets(bf, brackets):
    char = bf.read(1)
    while char != '':
        if char == '[':
            brackets[0].append(bf.tell())
            brackets[1].append(-1)
        if char == ']':
            for i in xrange(len(brackets[0]) - 1 , -1, -1):
                if brackets[1][i] == -1:
                    brackets[1][i] = bf.tell()
                    break
        char = bf.read(1)
    
                
def evaluate(bf, cells, ptr, brackets):
    char = bf.read(1)
    i = 0
    while char != '':
        if char == '>':
            ptr += 1

        elif char == '<':
            ptr -= 1

        elif char == '+':
            cells[ptr] += 1

        elif char == '-':
            cells[ptr] -= 1  

        elif char == '.':
            sys.stdout.write(chr(cells[ptr]))

        elif char == ',':
            getch.getch() 

        elif char == '[':            
            while brackets[0][i] != bf.tell():
                i += 1
            if cells[ptr] == 0:
                x = brackets[1][i]
                bf.seek(x, 0)

        elif char == ']':
            if cells[ptr] != 0:
                x = brackets[0][i]
                bf.seek(x, 0)
        else:
            char = bf.read(1)
            continue

        char = bf.read(1)

if __name__ == '__main__':
    bf = open(sys.argv[1], "r")
    
    cells = [0 for x in range(30000)]
    ptr = 0
    brackets = [[],[]]
    
    findBrackets(bf, brackets)
    bf.seek(0,0)
    
    evaluate(bf, cells, ptr, brackets)

    bf.close()

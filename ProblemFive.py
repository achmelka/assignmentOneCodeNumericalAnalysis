import math

MAX_ITERATIONS = 50
TOLERANCE = .0001


def main():
    biSectionMethod('a')
    biSectionMethod('b')
    biSectionMethod('c')
    biSectionMethod('d')
    print("")
    print("")
    fixedPointMethod('a')
    fixedPointMethod('b')
    fixedPointMethod('c')
    print("")
    print("")
    newtonsMethod('a')
    newtonsMethod('b')
    newtonsMethod('c')
    newtonsMethod('d')
    print("")
    print("")
    secantMethod('a')
    secantMethod('b')
    secantMethod('c')
    secantMethod('d')


def biSectionMethod(equation):
    print("----------------------------------------------------------------------")
    print("|                            Bisection Method                        |")
    print("----------------------------------------------------------------------")
    if equation == 'a':
        print("|-------------------------------Function A---------------------------|")
        #print("    a     |    b    |   (b-a)/2  |   f(a)  |   f(b)   |  f((b-a)/2) ")
        a = -1.0
        b = 1.0
        i = 1
        while i <= MAX_ITERATIONS:  #to only go through 50 iterations
            midpoint = (a+b)/2
            aValue = equationA(a)
            bValue = equationA(b)
            midpointValue = equationA(midpoint)
            print("ITR: "+str(i)+" | a:   "+str(a)+" | b:   "+str(b)+"   | midpoint:  "+str(midpoint)+"  | f(midpoint):  "+str(midpointValue)+" ")
            i = i + 1
            if midpointValue == 0 or (b-a)/2 <= TOLERANCE:
                #print("YEETBisection")
                return
            else:
                if midpointValue > 0:
                    b = midpoint
                elif midpointValue < 0:
                    a = midpoint

    elif equation == 'b':
        print("|-------------------------------Function B---------------------------|")
        #print("|    a     |    b    |   (b-a)/2  |   f(a)  |   f(b)   |  f((b-a)/2) |")
        a = 0.0
        b = 2.0
        i = 1
        while i <= MAX_ITERATIONS:  # to only go through 50 iterations
            midpoint = (b+a)/2
            aValue = equationB(a)
            bValue = equationB(b)
            midpointValue = equationB(midpoint)
            print("ITR: "+str(i)+" | a:   "+str(a)+" | b:   "+str(b)+"   | midpoint:  "+str(midpoint)+"  | f(midpoint):  "+str(midpointValue)+" ")
            i = i + 1
            if midpointValue == 0 or (b-a)/2 <= TOLERANCE:
                return
            else:
                if midpointValue > 0:
                    b = midpoint
                elif midpointValue < 0:
                    a = midpoint

    elif equation == 'c':
        print("|-------------------------------Function C---------------------------|")
        #print("|    a     |    b    |   (b-a)/2  |   f(a)  |   f(b)   |  f((b-a)/2) |")
        a = -2.0
        b = 2.0
        i = 1
        while i <= MAX_ITERATIONS: #to only go through 50 iterations
            midpoint = (b+a)/2
            aValue = equationC(a)
            bValue = equationC(b)
            midpointValue = equationC(midpoint)
            print("ITR: "+str(i)+" | a:   "+str(a)+" | b:   "+str(b)+"   | midpoint:  "+str(midpoint)+"  | f(midpoint):  "+str(midpointValue)+" ")
            i = i + 1
            if midpointValue == 0 or (b-a)/2 <= TOLERANCE:
                return
            else:
                if midpointValue > 0:
                    b = midpoint
                elif midpointValue < 0:
                    a = midpoint

    elif equation == 'd':
        print("|-------------------------------Function D---------------------------|")
        #print("|    a     |    b    |   (b-a)/2  |   f(a)  |   f(b)   |  f((b-a)/2) |")
        a = -2.0
        b = 2.0
        i = 1
        while i <= MAX_ITERATIONS:  # to only go through 50 iterations
            midpoint = (b+a) / 2
            aValue = equationD(a)
            bValue = equationD(b)
            midpointValue = equationD(midpoint)
            print("ITR: "+str(i)+" | a:   "+str(a)+" | b:   "+str(b)+"   | midpoint:  "+str(midpoint)+"  | f(midpoint):  "+str(midpointValue)+" ")
            i = i + 1
            if midpointValue == 0 or (b-a)/2 <= TOLERANCE:
                return
            else:
                if midpointValue > 0:
                    b = midpoint
                elif midpointValue < 0:
                    a = midpoint


def fixedPointMethod(equation):
        print("----------------------------------------------------------------------")
        print("|                          Fixed Point Method                        |")
        print("----------------------------------------------------------------------")
        if equation == 'a':
            x0 = 1# thats not right im just setting up the algorithm
            print("|-------------------------------Function A---------------------------|")
            for i in range(1, MAX_ITERATIONS):
                x1 = equationAgx(x0)
                print("ITR: "+str(i)+" | x1: "+str(x1)+"")
                if i == MAX_ITERATIONS:
                    print("WILL NOT CONVERGE")
                    return
                if abs(equationA(x1)) < TOLERANCE:
                    #print("AYYE M8")
                    return
                i = i+1
                x0 = x1

        if equation == 'b':
            x0 = 1# thats not right im just setting up the algorithm
            print("|-------------------------------Function B---------------------------|")
            for i in range(1, MAX_ITERATIONS):
                x1 = equationBgx(x0)
                print("ITR: "+str(i)+" | x1: "+str(x1)+"")
                if i == MAX_ITERATIONS:
                    print("WILL NOT CONVERGE")
                    return
                if abs(equationB(x1)) < TOLERANCE:
                    #print("AYYE M8")
                    return
                i = i+1
                x0 = x1

        if equation == 'c':
            x0 = 0# thats not right im just setting up the algorithm
            print("|-------------------------------Function C---------------------------|")
            for i in range(1, MAX_ITERATIONS):
                x1 = equationCgx(x0)
                print("ITR: "+str(i)+" | x1: "+str(x1)+"")
                if i == MAX_ITERATIONS:
                    print("WILL NOT CONVERGE")
                    return
                if abs(equationC(x1)) < TOLERANCE:
                    #print("AYYE M8")
                    return
                i = i+1
                x0 = x1



def newtonsMethod(equation):
    print("----------------------------------------------------------------------")
    print("|                            Newton's Method                         |")
    print("----------------------------------------------------------------------")
    i = 1.0
    x0 = 1.0
    x1 = 0.0
    if equation == 'a':
        print("|-------------------------------Function A---------------------------|")
        for i in range(MAX_ITERATIONS):
            y = equationA(x0)
            yprime = equationAPrime(x0)
            #maybe needs more code, but also possibly not
            x1 = x0 - (y/yprime)
            print("ITR: " + str(i) + " | x0: " + str(x0) + " | x1: " + str(x1) + " | abs(x1-x0:)" + str(abs(x1 - x0)) + " ")
            if(abs(x1-x0) <= TOLERANCE):
                #print("YEETNewton")
                return
            else:
                x0 = x1
                i = i + 1
        if i == 50:
            print("Max Iterations reached")
            return

    if equation == 'b':
        print("|-------------------------------Function B---------------------------|")
        for i in range(MAX_ITERATIONS):
            y = equationB(x0)
            yprime = equationBPrime(x0)
            #maybe needs more code, but also possibly not
            x1 = x0 - (y/yprime)
            print("ITR: " + str(i) + " | x0: " + str(x0) + " | x1: " + str(x1) + " | abs(x1-x0:)" + str(abs(x1 - x0)) + " ")
            if(abs(x1-x0) <= TOLERANCE):
                #print("YEETNewton")
                return
            else:
                x0 = x1
                i = i + 1
        if i == 50:
            print("Max Iterations reached")
            return

    if equation == 'c':
        print("|-------------------------------Function C---------------------------|")
        for i in range(MAX_ITERATIONS):
            y = equationC(x0)
            yprime = equationCPrime(x0)
            #maybe needs more code, but also possibly not
            x1 = x0 - (y/yprime)
            print("ITR: " + str(i) + " | x0: " + str(x0) + " | x1: " + str(x1) + " | abs(x1-x0:)" + str(abs(x1 - x0)) + " ")
            if(abs(x1-x0) <= TOLERANCE):
                #print("YEETNewton")
                return
            else:
                x0 = x1
                i = i + 1
        if i == 50:
            print("Max Iterations reached")
            return

    if equation == 'd':
        print("|-------------------------------Function D---------------------------|")
        for i in range(MAX_ITERATIONS):
            y = equationD(x0)
            yprime = equationDPrime(x0)
            #maybe needs more code, but also possibly not
            x1 = x0 - (y/yprime)
            print("ITR: " + str(i) + " | x0: " + str(x0) + " | x1: " + str(x1) + " | abs(x1-x0:)" + str(abs(x1 - x0)) + " ")
            if(abs(x1-x0) <= TOLERANCE):
                #print("YEETNewton")
                return
            else:
                x0 = x1
                i = i + 1
        if i == 50:
            print("Max Iterations reached")
            return


def secantMethod(equation):
    print("----------------------------------------------------------------------")
    print("|                            Secant Method                           |")
    print("----------------------------------------------------------------------")
    if equation == 'a':
        print("|---------------------------Equation A-------------------------------|")
        x1 = -1.0
        x2 = 1.0
        for i in range(1, MAX_ITERATIONS):
            value1 = equationA(x1)
            value2 = equationA(x2)
            if value1 == value2:
                print("ERROR")
                return
            x3 = x2 - value2 * (x2 - x1) / (value2 - value1)
            print("ITER: "+str(i)+ " | x1: "+str(x1)+" | x2: "+str(x2)+" | x3: "+str(x3))
            if abs(x3) < TOLERANCE or abs(x3-x2) < TOLERANCE:
                return
            x1 = x2
            x2 = x3
            if i == MAX_ITERATIONS:
                print("WILL NOT CONVERGE!")
                return

    if equation == 'b':
        print("|---------------------------Equation B-------------------------------|")
        x1 = -1.0
        x2 = 1.0
        for i in range(1, MAX_ITERATIONS):
            value1 = equationB(x1)
            value2 = equationB(x2)
            if value1 == value2:
                print("ERROR")
                return
            x3 = x2 - value2 * (x2 - x1) / (value2 - value1)
            print("ITER: "+str(i)+ " | x1: "+str(x1)+" | x2: "+str(x2)+" | x3: "+str(x3))
            if abs(x3) < TOLERANCE or abs(x3-x2) < TOLERANCE:
                return
            x1 = x2
            x2 = x3
            if i == MAX_ITERATIONS:
                print("WILL NOT CONVERGE!")
                return

    if equation == 'c':
        print("|---------------------------Equation C-------------------------------|")
        x1 = -1.0
        x2 = 1.0
        for i in range(1, MAX_ITERATIONS):
            value1 = equationC(x1)
            value2 = equationC(x2)
            if value1 == value2:
                print("ERROR")
                return
            x3 = x2 - value2 * (x2 - x1) / (value2 - value1)
            print("ITER: "+str(i)+ " | x1: "+str(x1)+" | x2: "+str(x2)+" | x3: "+str(x3))
            if abs(x3) < TOLERANCE or abs(x3-x2) < TOLERANCE:
                return
            x1 = x2
            x2 = x3
            if i == MAX_ITERATIONS:
                print("WILL NOT CONVERGE!")
                return

    if equation == 'd':
        print("|---------------------------Equation D-------------------------------|")
        x1 = -1.0
        x2 = 1.0
        for i in range(1, MAX_ITERATIONS):
            value1 = equationD(x1)
            value2 = equationD(x2)
            if value1 == value2:
                print("ERROR")
                return
            x3 = x2 - value2 * (x2 - x1) / (value2 - value1)
            print("ITER: "+str(i)+ " | x1: "+str(x1)+" | x2: "+str(x2)+" | x3: "+str(x3))
            if abs(x3) < TOLERANCE or abs(x3-x2) < TOLERANCE:
                return
            x1 = x2
            x2 = x3
            if i == MAX_ITERATIONS:
                print("WILL NOT CONVERGE!")
                return


def equationA(number):
    return (3 * math.pow(number, 3)) - (2 * math.pow(number, 2)) + (5 * number) - (2 * math.exp(number))+1


def equationB(number):
    return (math.pow(number, 4)) + (3 * math.pow(number, 2)) - 2


def equationC(number):
    return (3 * number) - (math.pow(number, 2)) + (math.exp(number)) - 2

def equationD(number):
    return number - math.cos(number)

def equationAPrime(number):
    return (9 * math.pow(number, 2)) - (4 * number) - (2 * math.exp(number)) + 5

def equationBPrime(number):
    return (4 * math.pow(number, 4)) + (6 * number)

def equationCPrime(number):
    return (-2 * number) + math.exp(number) + 3

def equationDPrime(number):
    return math.sin(number) + 1

def equationAgx(number):
    return (-3 * math.pow(number, 3) + 2 * math.pow(number, 2) + 2 * math.exp(number) -1)/5

def equationBgx(number):
    return math.sqrt((2-number**4)/3)

def equationCgx(number):
    return (number**2 - math.exp(number) + 2)/3

def equationDgx(number):
    return 1

if __name__ == "__main__":
    main()
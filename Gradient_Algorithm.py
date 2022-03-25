import math
import Constants
import Functions

def square(args):
    return args[0]*args[0]

def derivative(function, args,arg_num=0):
    h = 0.000001
    args2 = args.copy()
    args2[arg_num] += h
    return (function(args2) - function(args))/h

def gradient(function, args):
    g = []
    for i in range(len(args)):
        g.append(derivative(function,args,i))
    return g



def gradient_func(function, start, min_max=Constants.MIN,\
                    learn_rate=0.001, max_iter=1_000, tol=0.0001):
    iters = 0
    for i in range(max_iter):
        #print(x)
        iters = i
        diff = gradient(function, start)
        diff = list(map(lambda a: a*learn_rate, diff))
        if all(map(lambda a: abs(a) < tol, diff)):
            break
        for i in range(len(start)):
            start[i] += (min_max == Constants.MAX)*diff[i]
            start[i] -= (min_max == Constants.MIN)*diff[i]

    return iters, start

## testowanie printy
start = Functions.randomData([[-2,2], [-2,2]], 2)
lowest = math.inf
it = math.inf
ar = start
for _ in range(100):
    iters, args = gradient_func(Functions.rosenbrock, start,
                                learn_rate=0.00003, tol=0.0000001, max_iter=10_000)
    fx = Functions.rosenbrock(args)
    if lowest > fx:
        lowest = fx
        it = iters
        ar = args
print(it, ar, lowest)

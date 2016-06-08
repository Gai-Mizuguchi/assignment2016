import sys
import random
import time
import numpy as np
import math

def read_instance(line):
    listline = line.strip().split()
    bias = (0, 1.)
    vector = [bias]
    for i in listline:
        if (i != listline[0]):
            component = i.split(":")
            alpha = int(component[0])
            beta = int(component[1])
            root = math.sqrt(beta*beta)
            vector.append((alpha, beta/root))
        Labelfv = (int(listline[0]), vector)

    return Labelfv

def read_data(filename):
    instancelist = []
    fv_max = 0
    for i in open(filename, "r"):
        instance = read_instance(i)
        instancelist.append(instance)
        
        for fv in instance[1]:
            if int(fv[0]) > int(fv_max):
                fv_max = fv[0]
    return instancelist, fv_max

def add_fv(fv):
    for comp in fv:
        weight[comp[0]] += comp[1]
    return

def sub_fv(fv):
    for comp in fv:
        weight[comp[0]] -= comp[1]

def add_tmp(fv, nupdates):
    for comp in fv:
        tmp_weight[comp[0]] += (comp[1]*nupdates)

def sub_tmp(fv, nupdates):
    for comp in fv:
        tmp_weight[comp[0]] -= (comp[1]*nupdates)

def mult_fv(fv, weight):
    lenweight = len(weight)
    output = 0
    for component in fv:
        if component[0] < lenweight:
            output += weight[component[0]] * component[1]
    return output

def averaged_weight(update):
    if not len(weight) == len(tmp_weight):
        print("Try Again!")
    if len(weight) == len(tmp_weight):
        for i in range(len(weight)):
            ave_weight[i] = weight[i] - (tmp_weight[i] / update)

def update_weight(instancelist, nupdates):
    random.shuffle(instancelist)
    for instance in instancelist:
        if mult_fv(instance[1], weight) * instance[0] <= 0.1:
            if instance[0] > 0:
                add_fv(instance[1])
                add_tmp(instance[1], nupdates)
            else:
                sub_fv(instance[1])
                sub_tmp(instance[1], nupdates)

            nupdates += 1
    return weight, tmp_weight, nupdates

def evaluate(instancelist, weight):
    correct = 0
    num_instance = 0
    for instance in instancelist:
        if mult_fv(instance[1], weight) * instance[0] > 0:
            correct += 1
        num_instance += 1
    return(correct, num_instance, float(correct)/num_instance)

if __name__=="__main__":
    start_time = time.time()
    (train_data, train_max_index) = read_data(sys.argv[1])
    weight = [int(0)] * (int(train_max_index)+1)
    tmp_weight = weight

    nupdates = 0
    
    for learning in range(int(sys.argv[3])):
        weight, tmp_weight, nupdates = update_weight(train_data, nupdates)

    ave_weight = [0]*(int(train_max_index)+1)
    averaged_weight(nupdates)
    (test_data, test_max_index) = read_data(sys.argv[2])
    result = evaluate(test_data, ave_weight)

    print("Correct: ", result[0])
    print("Tested: ", result[1])
    print("Accuracy: ", result[2])
    
    end_time = time.time()
    print(end_time - start_time)

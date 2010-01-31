'''
Created on Jan 30, 2010

@author: changwang
'''

import random

from edu.wmich.hopfield.MindofHomer import prune_input, state_factory, matrix_creator, state2string
from edu.wmich.hopfield.utils import matrixFormatter

def random_update(state, weight_matrix):
    sum = 0
    neuron = random.randint(0, 69)
    weights = weight_matrix[neuron]
    for i in range(70):
        sum += state[i] * weights[i]
    return (neuron, threshold_func(sum))
    
def threshold_func(input_sum):
    return 1 if input_sum > 0 else 0

def main():
    #stable_str = raw_input("Please type the stable string, which you want the system to converge at: ")
    #stable_str = prune_input(stable_str)
    stable_str = prune_input('changwang!')
#    print "'" + stable_str + "'"
    
    matrix = matrix_creator(state_factory(stable_str))
    
    #matrixFormatter(matrix)
    
#    print matrix
    
#    init_str = raw_input("Please type the initial string for the system: ")
#    init_str = prune_input(init_str)
    init_str = prune_input('wangchang')
#    print "'" + init_str + "'"
    init_state = state_factory(init_str)
#    print init_state
    #for i in range(100):
    update_str = ''
    while(update_str != stable_str):
        neuron, output = random_update(init_state, matrix)
        init_state[neuron] = output
    
        update_str = state2string(init_state)
        print update_str

if __name__ == '__main__':
    main()
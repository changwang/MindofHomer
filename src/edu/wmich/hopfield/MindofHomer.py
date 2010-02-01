'''
Created on Jan 30, 2010

@author: changwang
'''

import random

HEXDICT = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
    '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
    'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'
}

def dec2bin(decimal):
    """ Python < 2.6 doesn't provide bin(), so use this way to map integer and binary.
    Create hex of int, remove '0x'. now for each hex char,
    look up binary string, append in list and join at the end. """
    bstr = ''.join([HEXDICT[hstr] for hstr in hex(decimal)[2:]])
    return bstr[1:] if len(bstr) > 7 else bstr.rjust(7, '0') # make sure the return string is 7 bits.

def state_factory(input):
    """ According to the user input string, map that into a 70 items array,
    Each item represents a neuron in the system. """
    state_set = []
    for ch in input:
        bstr = dec2bin(ord(ch))
        for b in bstr:
            state_set.append(int(b))
    return state_set

def matrix_creator(stable_set):
    """ Using the given stable string, calculates the 70 x 70 weight matrix. """
    weight_matrix = []
    for idx_i, s_i in enumerate(stable_set):
        sub_matrix = []
        for idx_j, s_j in enumerate(stable_set):
            if idx_j == idx_i: # because there is no self affect, weight sets to 0.
                sub_matrix.append(0)
            else:
                sub_matrix.append((2 * s_i - 1)*(2 * s_j - 1))
        weight_matrix.append(sub_matrix)

    return weight_matrix

def prune_input(input):
    """ Prune the input string to 10 characters long. """
    return input.ljust(10, ' ') if len(input) < 10 else input[:10]

def state2string(state):
    """ Mapping the binary string into readable characters. """
    resulting = ''
    str_state = [str(b) for b in state]
    binary_string = ''.join(str_state)
    for i in range(len(state) / 7):
        ch = int(binary_string[i*7:(i+1)*7], 2) # binary -> decimal -> character
        if ch > 0 and ch < 10:
            ch = str(ch)
        else:
            ch = chr(ch)
        resulting += ch
    return resulting
        
def random_update(state, weight_matrix):
    """ Randomly pick up one neuron to be active. """
    sum = 0
    neuron = random.randint(0, 69) # index starts from 0, so 0 , ... , 69 
    weights = weight_matrix[neuron] # this is the weight array attached to above neuron
    for i in range(70):
        sum += state[i] * weights[i]
    return (neuron, _threshold_func(sum)) # I want it to return both neuron number & output

def _threshold_func(input_sum):
    """ In our prerequisites, threshold value is 0.
    So, if sum of input * weight is less than 0, it gives 0,
    otherwise it fires 1. """
    return 1 if input_sum > 0 else 0
        
def energy_func(state, weight_matrix):
    """ The energy function. In our system,
    we can see this function goes to its minimum local value. """
    energy = 0
    for i, s_i in enumerate(state):
        for j, s_j in enumerate(state):
            energy += s_i * s_j * weight_matrix[i][j]
    return - (0.5 * energy)
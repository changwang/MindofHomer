'''
Created on Jan 30, 2010

@author: changwang
'''

HEXDICT = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
    '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
    'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'
}

def dec2bin(decimal):
    ''' Python < 2.5 doesn't provide bin(), so use this way to map integer and binary.
    Create hex of int, remove '0x'. now for each hex char,
    look up binary string, append in list and join at the end. '''
    bstr = ''.join([HEXDICT[hstr] for hstr in hex(decimal)[2:]])
    if len(bstr) > 7:
        bstr = bstr[1:]
    return bstr.rjust(7, '0')

def stable_state_factory(stable_input):
    stable_state_set = []
    for i in range(len(stable_input)):
        bstr = dec2bin(ord(stable_input[i]))
        for b in range(7):
            stable_state_set.append(int(bstr[b]))
    return stable_state_set

#    return [[bstr] for bstr in [dec2bin(ord(c)) for c in [ch for ch in stable_input]]]

def matrix_creator(stable_set):
    weight_matrix = []
    for s_i in range(70):
        sub_matrix = []
        for index, s_j in enumerate(stable_set):
            if index == s_i:
                sub_matrix.append(0)
            else:
                sub_matrix.append((2 * stable_set[s_i] - 1)*(2 * s_j - 1))
        weight_matrix.append(sub_matrix)

    return weight_matrix
'''
Created on Jan 30, 2010

@author: changwang
'''

from edu.wmich.hopfield.MindofHomer import prune_input, state_factory, matrix_creator, state2string, energy_func, random_update

def main():
    """ Entry of my program, ask user to input two strings,
    first one is the stable string, the other one is the initial string. """
    
    stable_str = raw_input("Please type the stable string, which you want the system to converge to: ")
    stable_str = prune_input(stable_str)
    
    matrix = matrix_creator(state_factory(stable_str))
    
    init_str = raw_input("Please type the initial string for the system: ")
    init_str = prune_input(init_str)
    
    init_state = state_factory(init_str)
    
    state = init_state[:]

    update_str = ''
    step = 0
    while(update_str != stable_str):
        neuron, output = random_update(state, matrix)
        state[neuron] = output
        
        step += 1
        
        print "This is STEP '" + str(step) + "'"
        
        print "neuron " + str(neuron) + " is updating"
        
        print "The value of energy function is: " + str(energy_func(state, matrix))
    
        update_str = state2string(state)
        
        if update_str == stable_str:
            print "====== Come to Stable ======"
            print "'" + update_str + "'"
            print "============================"
        else:
            print "Current state interpreted to string is: '" + update_str + "'"
        print

if __name__ == '__main__':
    main()
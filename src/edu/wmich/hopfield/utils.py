'''
Created on Jan 31, 2010

@author: changwang
'''

def matrixFormatter(mat):
    """ utility function, in order to print the matrix
    with readable format. """
    
    for i in range(len(mat)):
        for j in mat[i]:
            print '%2d' % j,
        print
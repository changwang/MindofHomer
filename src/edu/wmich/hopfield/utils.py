'''
Created on Jan 31, 2010

@author: changwang
'''

def matrixFormatter(mat):
    for i in range(len(mat)):
        for j in mat[i]:
            print '%2d' % j,
        print
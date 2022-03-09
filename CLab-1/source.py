import numpy as np

########################################################
## Complete functions in skeleton codes below
## following instructions in each function.
## Do not modify existing function name or inputs.
## Do not test your codes here - use main.py instead.
## You may use any built-in functions from NumPy.
## You may define and call new functions as you see fit.
########################################################


def low_rank_approx(A, k):
    '''
    inputs: 
      - A: m-by-n matrix
      - k: positive integer, k<=m, k<=n
    returns:
      X: m-by-n matrix that is an as-close-as-possible approximation of A
         up to rank k
    '''
    #TODO: Fill your work here
    U, S, V_T = np.linalg.svd(A)
    print(U.shape)
    print(np.diag(S[:k]).shape)
    print(V_T[:k].shape)
    return U[:,:k]@np.diag(S[:k])@V_T[:k]
    """
    m,n = A.shape
    S_diag = np.zeros((m, n))
    np.fill_diagonal(S_diag,S)
    S_diag[:,n-(n-k):n]=0
    
    Ak = U * S_diag * V_T
    """
    #return Ak
    
    
    

def constrained_LLS(A, B):
    '''
    inputs:
      - A: n-by-n full rank matrix
      - B: n-by-n matrix
    returns:
      x: n-diemsional vector that minimises ||Ax||2 subject to ||Bx||2=1 
    '''
    #TODO: Fill your work here



### you can optionally write your own functions like below ###

# def my_func_name(input1, input2, ...):
#     do something
#     return ...
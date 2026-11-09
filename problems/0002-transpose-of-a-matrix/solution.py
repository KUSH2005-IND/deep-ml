def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here

    if not a:
        return []

    m=len(a) #no of rows
    n=len(a[0]) #no of cols

    trans=[[0 for _ in range(m)] for _ in range(n)] #empty transpose matrix (nxm)
    # #outer loop creates n rows, inner loop fills m zeroes in each row

    for i in range(m):
        for j in range(n):
            trans[j][i]=a[i][j] #transpose

    return trans
N = 5
C = [[0] * N for row in range(N)]

def matrix(A, B):
    global C
    for i in range(N):
        for j in range(N):
            sum = 0
            for k in range(N):
                sum += A[i][k] * B[k][j]
            C[i][j] = sum
        
def output_result(A, B):
    global C
    print("\nContent of Matrix A : \n")
    output_matrix(A)       
    print("\nContent of Matrix B : \n")
    output_matrix(B)
    print("\nContent of Matrix C : \n")
    output_matrix(C)
    
def output_matrix(m):
    for i in range(N):
        for j in range(N):
            print(" ", m[i][j], end = '')   
        print()
        
def main():
    global N
    
    A = [[0] * N for row in range(N)]
    B = [[0] * N for row in range(N)]
      
    for i in range(N):
        for j in range(N):
            A[i][j] = j + 1
            B[i][j] = -(j - 5)
    
    matrix(A, B)
    output_result(A, B)        
    
main()
 
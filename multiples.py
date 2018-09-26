#program to print multiples
def multiple(m,N): 
  
    # inserts all elements from n to  
    # (m * n)+1 incremented by n. 
    a = range(N, (m * N)+1, N) 
      
    print(a) 
  
# driver code  
N = int(input(""))
m=5
multiple(m, N) 

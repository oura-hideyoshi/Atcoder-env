n_test = int(input())

def calc_sum_NN(k, m):
    return k*m*(m+1) // 2

def calc_sum_N(k, m):
    return k*m

for _ in range(n_test):
    N, M = map(int, input().split())
    A = [0]
    B = [0]
    init_C = None
    
    for __ in range(N):
        x, y = map(int, input().split())
        if __ == 0:
            init_C = x
            
        if B[-1] > 0 and B[-1] + calc_sum_N(x, y) < 0:
            thresh_y = B[-1] % abs(x)
            A.append( A[-1] + calc_sum_NN(x, thresh_y) + B[-1] * thresh_y)
            B.append( B[-1] + calc_sum_N(x, thresh_y))
            
            A.append( A[-1] + calc_sum_NN(x, y - thresh_y) + B[-1] * (y - thresh_y))
            B.append( B[-1] + calc_sum_N(x, thresh_y))
        else:
            A.append( A[-1] + calc_sum_NN(x, y) + B[-1] * y)
            B.append( B[-1] + calc_sum_N(x, y))
    
    A.append(init_C)
    
    print(max(A))
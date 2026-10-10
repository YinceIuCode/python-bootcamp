"""
// Member 5 - Starting C++ point

int fibonacci(int n){
    vector<int> fib_table = {0, 1};
    
    for (int i = 0; i < n; ++i){
        int temp = fib_table[0] + fib_table[1];
        fib_table[0] = fib_table[1];
        fib_table[1] = temp;
    };
    
    return fib_table[0];
}

"""

def fibonacci(n : int):    
    from functools import reduce
    return reduce(lambda x, dummy: [x[1], x[0] + x[1]], range(n), [0, 1])[0]

for i in range(100):
    print(fibonacci(i), i)
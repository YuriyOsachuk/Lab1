def fibonacci(n):
    if n < 0:
        print("Incorrect input")
        return
    
    if n == 0:
        return 0
    elif n == 1:
        return 1

    x_n_2 = 0
    x_n_1 = 1

    for i in range(2, n + 1):
        x_n = x_n_1 + x_n_2
        x_n_2 = x_n_1
        x_n_1 = x_n
    
    return x_n_1

print(fibonacci(20))

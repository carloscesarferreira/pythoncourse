print("Consider two numbers n and k, with 0 <= k <= n, we want to calculate Binomial (n, k)")

while True:
    n = int(input("Enter n: "))
    k = int(input("Enter k: "))

    if n == k:
        p = 1
    else:
        p = n - k

    if k < 0 or n < 0 or n < k:
        print("The numbers you used are not valid.")
        choice = int(input("Enter 0 - Quit Program or 1 - Try Again: "))        
        if choice == 0:
            print("You quitted the the program")
            break
        elif choice != 1:
            print("Invalid choice. Please enter 0 - Quit Program or 1 - Try Again.")
    else:
        
        def binomial(n, k):
            
            def factorial_n(n):
                result = n
                for x in range(n, 1, -1):
                    result = result * (x - 1)
                return result
            
            def factorial_k(k):
                result = k
                for x in range(k, 1, -1):
                    result = result * (x - 1)
                return result
        
            def factorial_n_k(p):
                result = p
                for x in range(p, 1, -1):
                    result = result * (x - 1)
                return result
        
            return factorial_n(n) / (factorial_k(k) * factorial_n_k(p))
        
        result = binomial(n, k)
        print(f"Binomial({n},{k}) = {result}")
        break

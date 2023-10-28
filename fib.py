import rustlib
import timeit

def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def rust_code():
    return rustlib.fib(18)

if __name__ == "__main__":
    n = 18  
    print("""----------------------------------------------------------------------------- \n\n\n""")

    fib_time = timeit.timeit('Fibonacci(n)', globals=globals(), number=1000) * 1e6

    rust_time = timeit.timeit('rust_code()', globals=globals(), number=1000) * 1e6

    print(f"Python Fibonacci Function Time: {fib_time:.2f} microseconds")
    print(f"Rust InterOp called from Python Time: {rust_time:.2f} microseconds")


    print(""" \n\n\n-----------------------------------------------------------------------------""")




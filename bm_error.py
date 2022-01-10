def bisection(func, a, b, error_acceptable):

    def f(x):
        f = eval(func)
        return f

    error = abs(b-a)

    while error > error_acceptable:
        c = (b + a)/2

        if f(a) * f(b) >=  0:
            print("No root or Multiple root present, therefore bisection method will not work,")
            quit()
        elif f(c) * f(a) < 0:
            b = c
            error = abs(b - a)
        elif f(c) * f(b) < 0:
            a = c
            error = abs(b - a)
        else:
            print("Something went wrong!")
            quit()
        
    print(f"The error is {error}")
    print(f"The Lower boundry, a is {a} and the Upper boundry, b is {b}")

func = input("Enter the Function: ")
a = input("Enter the first root: ")
b = input("Enter the second root: ")
error_acceptable = input("Enter the acceptable error: ")
func = str(func)
a = float(a)
b = float(b)
error_acceptable = float(error_acceptable)

bisection(func, a, b, error_acceptable)
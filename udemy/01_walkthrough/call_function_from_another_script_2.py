#!/usr/bin/env python3

import call_function_from_another_script_1 as script1

def multiply(a,b):
    print(f"Product of {a} and {b} is {a*b}")
    return None

def main():
    x=20
    y=10
    script1.add(x,y)
    script1.subtract(x,y)
    multiply(x,y)
    return None

if __name__=="__main__":
    main()

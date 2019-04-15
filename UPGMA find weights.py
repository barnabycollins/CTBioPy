while True:
    a =   int(input("\n\n\n|a|     --> "))
    b =   int(input("|b|     --> "))
    dac = float(input("d(a, c) --> "))
    dbc = float(input("d(b, c) --> "))

    print((a*dac+b*dbc)/(a+b))

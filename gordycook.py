def F(J, Ka, Kc, A, B, C):
    assert type(J) is int and type(Ka) is int and type(Kc) is int, \
        "J, Ka, and Kc must be integers."
    try:
        A = float(A)
        B = float(B)
        C = float(C)
    except ValueError:
        raise ValueError("A, B, C must be numbers.")
    assert J <= 3 and Ka <= 3 and Kc <= 3, \
        "implemented only for J <= 3"
    if J == 0:
        return 0
    elif J == 1:
        if Ka == 1 and Kc == 0:
            return A + B
        elif Ka == 1 and Kc == 1:
            return A + C
        elif Ka == 0 and Kc == 1:
            return B + C
    elif J == 2:
        if Ka == 2 and Kc == 0:
            return 2*A + 2*B + 2*C + 2*((B - C)**2 + (A - C)*(A - B))**(1/2)
        elif Ka == 2 and Kc == 1:
            return 4*A + B + C
        elif Ka == 1 and Kc == 1:
            return A + 4*B + C
        elif Ka == 1 and Kc == 2:
            return A + B + 4*C
        elif Ka == 0 and Kc == 2:
            return 2*A + 2*B + 2*C - 2*((B - C)**2 + (A - C)*(A - B))**(1/2)
    elif J == 3:
        if Ka == 3 and Kc == 0:
            return 5*A + 5*B + 2*C + 2*(4*(A - B)**2 + (A - C)*(B - C))**(1/2)
        elif Ka == 3 and Kc == 1:
            return 5*A + 2*B + 5*C + 2*(4*(A - C)**2 - (A - B)*(B - C))**(1/2)
        elif Ka == 2 and Kc == 1:
            return 2*A + 5*B + 5*C + 2*(4*(B - C)**2 + (A - B)*(A - C))**(1/2)
        elif Ka == 2 and Kc == 2:
            return 4*A + 4*B + 4*C
        elif Ka == 1 and Kc == 2:
            return 5*A + 5*B + 2*C - 2*(4*(A - B)**2 + (A - C)*(B - C))**(1/2)
        elif Ka == 1 and Kc == 3:
            return 5*A + 2*B + 5*C - 2*(4*(A - C)**2 - (A - B)*(B - C))**(1/2)
        elif Ka == 0 and Kc == 3:
            return 2*A + 5*B + 5*C - 2*(4*(B - C)**2 + (A - B)*(A - C))**(1/2)
    assert False, \
        "combination of J, Ka, Kc not found"
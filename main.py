import cmath

a = float(input())
b = float(input())
c = float(input())

if a == b == c == 0:
    print("x ∈ C")

elif a == b == 0 and c != 0:
    print("x ∉ C")

elif a == 0:
    print(-b / c)

else:
    D = b * b - 4 * a * c

    x1 = (-b + cmath.sqrt(D)) / (2 * a)
    x2 = (-b - cmath.sqrt(D)) / (2 * a)

    print("x =", x1, ", ", x2)

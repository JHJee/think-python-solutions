from math import sqrt


def exercise_1():
    print("# exercise_1()")

    def compare(x, y):
        if x > y:
            return 1
        elif x == y:
            return 0
        else:
            return -1

    print(compare(4, 5))


def exercise_2():
    print("# exercise_2()")

    def hypotenuse(sa, sb):
        sa = sa ** 2
        sb = sb ** 2
        h = sqrt(sa + sb)
        return h

    hypotenuse(4, 10)


def exercise_3():
    print("# exercise_3()")
    pass


def exercise_4():
    print("# exercise_4()")
    pass


exercise_1()
exercise_2()
exercise_3()
exercise_4()


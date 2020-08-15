def exercise_1():
    print("# exercise_1()")
    # Traceback (most recent call last):
    #  File "c:\Users\Jihye\Desktop\TP-Chapter3.py", line 3, in <module>
    #    repeat_lyrics()
    # NameError: name 'repeat_lyrics' is not defined
    pass


def exercise_2():
    print("\n# exercise_2()")

    def repeat_lyrics():
        print_lyrics()
        print_lyrics()

    def print_lyrics():
        print("yes")
        print("I'm a lumberjack, and I'm okay.")
        print("I sleep all night and I work all day.")

    repeat_lyrics()


def exercise_3(str):
    print("\n# exercise_3()")
    print(" " * 65, str)


def exercise_4():
    print("\n# exercise_4()")

    def print_spam(str):
        print(str)

    def do_twice(f, str):
        f(str)
        f(str)

    def do_four(f, str):
        do_twice(f, str)
        do_twice(f, str)

    do_four(print_spam, "spam")


def exercise_5():
    print("\n# exercise_5()")
    print("+", "----", "+", "----", "+")
    print("|      |      |")
    print("|      |      |")
    print("|      |      |")
    print("|      |      |")
    print("+", "----", "+", "----", "+")
    print("|      |      |")
    print("|      |      |")
    print("|      |      |")
    print("|      |      |")
    print("+", "----", "+", "----", "+")


exercise_1()
exercise_2()
exercise_3("allen")
exercise_4()
exercise_5()


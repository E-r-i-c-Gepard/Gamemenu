def raten():
    a, b = 0, 101
    while True:
        c = (b - a) // 2 + a
        print(f"Ist die Zahl {c}?")
        answer = input("kleiner, größer oder richtig: ")
        if answer == "kleiner":
            b = c
        if answer == "größer":
            a = c
        if answer == "richtig":
            print("Juhuuuuuhuhuhuhuhuuuu!")
            break

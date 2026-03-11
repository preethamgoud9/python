count = 0

def func(value):
    global count
    if count == value:
        return
    else:
        print("preetham")
        count += 1
        func(value)

func(3)
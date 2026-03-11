def func(count):
    if count == 0:
        return
    else:
        count = count - 1
        print(count)
        func(count)

func(5)
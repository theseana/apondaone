from ussd import pages


def p_0_4():
    p = {
        '0': p_0 ,
    }
    print(pages.page_0_4)
    input_msg = input("replay: ")
    p[input_msg]()


def p_0_3():
    p = {
        '0': p_0 ,
    }
    print(pages.page_0_3)
    input_msg = input("replay: ")
    p[input_msg]()


def p_0_2():
    p = {
        '0': p_0 ,
    }
    print(pages.page_0_2)
    input_msg = input("replay: ")
    p[input_msg]()


def p_1_1():
    p = {
            '0': p_0_1 ,
        }
    print(pages.page_0_1_1)
    input_msg = input("replay: ")
    p[input_msg]()


def p_0_1():
    p = {
        '0': p_0 ,
        '1': p_1_1 ,
    }
    print(pages.page_0_1)
    input_msg = input("replay: ")
    p[input_msg]()


def p_0():
    p = {
        '0': quit ,
        '1': p_0_1,
        '2': p_0_2,
        '3': p_0_3,
        '4': p_0_4,
    }
    print(pages.page_0)
    input_msg = input("replay: ")
    p[input_msg]()


p_0()

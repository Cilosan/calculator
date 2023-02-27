class InvalidFormatException(Exception):
    """Raised when the input format isn't fitting"""
    pass


class InvalidOperatorException(Exception):
    """Raised when the operator format isn't fitting"""
    pass


# Checks if number is one digit and integer
def is_one_digit(v):
    v = float(v)
    output = - 10 < v < 10 and v.is_integer()
    return output


# Checks the laziness of a user
def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 in "+*-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
    print(msg)
    return


msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_list = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]

memory = 0

while True:

    try:
        # Checking input on correctness and calculating result
        print(msg_0)
        calc = input().split()
        if len(calc) != 3:
            raise InvalidFormatException
        x, op, y = calc
        x = memory if x == "M" else float(x)
        y = memory if y == "M" else float(y)
        if len(op) != 1 or op not in "+-/*":
            raise InvalidOperatorException
        check(x, y, op)

        if op == "+":
            result = float(x + y)
        elif op == "-":
            result = float(x - y)
        elif op == "*":
            result = float(x * y)
        elif op == "/":
            result = float(x / y)
        print(result)

        # Saving result in memory
        while True:
            print(msg_4)
            answer_memory = input()
            if is_one_digit(result):
                msg_index = 10
                while answer_memory != "n" and msg_index <= 12:
                    answer_memory = input(msg_list[msg_index] + "\n")
                    msg_index = msg_index + 1
            if answer_memory == "y":
                memory = result
            elif answer_memory != "n" and answer_memory != "y":
                continue
            break

        # Asking about continuing the calculations
        while True:
            print(msg_5)
            answer_continue = input()
            if answer_continue != "n" and answer_continue != "y":
                continue
            break
        if answer_continue == "y":
            continue

    except ValueError:
        print(msg_1)
        continue
    except InvalidOperatorException:
        print(msg_2)
        continue
    except ZeroDivisionError:
        print(msg_3)
        continue
    except InvalidFormatException:
        print("Your format should be 'x operator y'")
        continue

    break

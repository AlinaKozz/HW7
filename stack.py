def push(stack, n):
    global stack_list
    stack_list = stack[:] + [n]
    return stack_list


def pop(stack_list):
    last_num = stack_list[-1]
    stack = stack_list[:-1]
    print(last_num)
    return stack


def size(stack):
    return len(stack_list) - 1


def back(stack_list):
    return stack_list[-1]


def clear(stack_list, answer):
    if answer == 'y':
        stack_list = []
        return stack_list


def exit():
    print("Bye")

command = ""
stack_list = []

if __name__ == '__main__':

    while command != "exit":

        command = input("Enter the command: ")
        if command == 'push':
            input_number = input("Enter a number: ")
            push(stack=stack_list, n=input_number)
            print("Ok")
        elif command == 'pop':
            stack_list = pop(stack_list)
        elif command == 'size':
            stack_len = size(stack=stack_list)
            print(stack_len)
        elif command == 'back':
            print(stack_list[-1])
        elif command == 'clear':
            input_answer = input("Clear the list, yes or no [y/n]? ")
            stack_list = []
            print("Ok")
        else:
            print("Bye")
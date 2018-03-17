

class Stack:

    def __init__(self, *args):
        self.body = list(args)
        self.permitted_count = 100

    def push(self, new_item):
        if len(self.body) < self.permitted_count:
            self.body = self.body + [new_item]
            return self.body

    def pop(self):
        last_num = self.body[-1]
        self.body = self.body[:-1]
        return last_num

    def size(self):
        return len(self.body)

    def back(self):
        return self.body[-1]

    def clear(self, answer):
        if answer == 'y':
            self.body = []
            return self.body

    def show(self):
        print(self.body)


def exit():
    print("Bye")

command = ""

stack = Stack()

if __name__ == '__main__':

    while command != "exit":

        command = input("Enter the command: ")
        if command == 'push':
            input_number = input("Enter a number: ")
            stack.push(input_number)
            print("Ok")
        elif command == 'pop':
            last_num = stack.pop()
            print(last_num)
        elif command == 'show':
            stack.show()
        elif command == 'size':
            stack_len = stack.size()
            print(stack_len)
        elif command == 'back':
            print(stack.body[-1])
        elif command == 'clear':
            input_answer = input("Clear the list, yes or no [y/n]? ")
            stack.clear(input_answer)
            print("Ok")
        else:
            print("Bye")

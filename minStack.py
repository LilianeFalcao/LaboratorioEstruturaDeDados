from stack import Stack

main_stack = Stack()
min_stack = Stack()

def push_aux(data):
    main_stack.push(data)

    if min_stack.is_empty():
        min_stack.push(data)
    elif data < min_stack.peek():
        min_stack.push(data)
    else:
        min_stack.push(min_stack.peek())

def pop_aux():
    min_stack.pop()
    return main_stack.pop()

def get_min():
    if min_stack.is_empty():
        raise IndexError("Pilha vazia - não há mínimo")
    return min_stack.peek()

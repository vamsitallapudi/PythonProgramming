
def print_and_iterate(current):
    print("{}".format(current.data), end=" ")
    current = current.next
    return current
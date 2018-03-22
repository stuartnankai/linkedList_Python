class Node(object):

    def __init__(self, value, next_node=None, pre_node=None):
        self.value = value
        self.next_node = next_node
        self.pre_node = pre_node


class LinkedList(object):
    """
    push (insert value at back);
    pop (remove value at back);     Need to return the value which I removed
    shift (remove value at front);  Need to return the value which I removed
    unshift (insert value at front);

    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.current = None

    def push(self, new_value):
        self.length = self.length + 1
        if self.tail is not None:  # if list has node
            new_node = Node(new_value, None, self.tail)
            self.tail.next_node = new_node
        else:  # new list without node
            new_node = Node(new_value)
            self.head = new_node
        self.tail = new_node

    def pop(self):
        if self.length > 0:  # Not empty
            self.length = self.length - 1
            pop_value = self.tail.value
            self.tail = self.tail.pre_node  # The previous node will be the tail
            if self.tail is not None:
                self.tail.next_node = None
            else: 
                self.head = None
            return pop_value
        else:
            # raise Exception("Meaningful message indicating the source of the error")
            raise ValueError("Empty list, no element")

    def shift(self):
        if self.length > 0:
            self.length = self.length - 1
            shift_value = self.head.value
            self.head = self.head.next_node
            if self.head is not None:
                self.head.pre_node = None
            else:
                self.tail = None
            return shift_value
        else:
            # raise Exception("Meaningful message indicating the source of the error")
            raise ValueError("Empty list, no element")

    def unshift(self, new_value):
        self.length = self.length + 1
        if self.head is not None:
            new_node = Node(new_value, self.head, None)
            self.head.pre_node = new_node
        else:
            new_node = Node(new_value)
            self.tail = new_node
        self.head = new_node

    # def showList(self):
    #     node = self.head
    #     while node is not None:
    #         print(node.value)
    #         node = node.next_node

#
# if __name__ == '__main__':
#     new_list = LinkedList()
#     new_list.push(10)
#     new_list.push(20)
#     new_list.push(30)
#     new_list.push(40)
#     # new_list.unshift(30)
#     print("This is the length of list", new_list.length)
#     new_list.showList()
#     print("*" * 100)
#     new_list.pop()
#     new_list.pop()
#     # new_list.shift()
#     new_list.showList()
#     print("This is the length of list", new_list.length)

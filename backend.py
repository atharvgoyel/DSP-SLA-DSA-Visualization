#Array

def array_insert(array, value, index):
    if index < 0 or index > len(array):
        return False
    array.insert(index, value)
    return True

def array_delete(array, index):
    if index < 0 or index >= len(array):
        return None
    return array.pop(index)

def array_search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1

#stack

def stack_push(stack, value):
    stack.append(value)
    return True

def stack_pop(stack):
    if len(stack) == 0:
        return None
    return stack.pop()

#queue

def queue_enqueue(queue, value):
    queue.append(value)
    return True

def queue_dequeue(queue):
    if len(queue) == 0:
        return None
    return queue.pop(0)

#Single linkd

class SinglyNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = SinglyNode(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def delete(self, value):
        if self.head is None:
            return False
        if self.head.value == value:
            self.head = self.head.next
            return True
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def to_list(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next
        return values

#Doubly linked

class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = DoublyNode(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        new_node.previous = current

    def delete(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                if current.previous is not None:
                    current.previous.next = current.next
                else:
                    self.head = current.next
                if current.next is not None:
                    current.next.previous = current.previous
                return True
            current = current.next
        return False

    def to_list(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next
        return values

#search

def linear_search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1

def binary_search(array, value):
    low = 0
    high = len(array) - 1
    while low <= high:
        middle = (low + high) // 2
        if array[middle] == value:
            return middle
        elif array[middle] < value:
            low = middle + 1
        else:
            high = middle - 1
    return -1

#sort

def bubble_sort(array):
    result = array[:]
    for i in range(len(result) - 1):
        for j in range(len(result) - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result

def selection_sort(array):
    result = array[:]
    for i in range(len(result) - 1):
        smallest = i
        for j in range(i + 1, len(result)):
            if result[j] < result[smallest]:
                smallest = j
        result[i], result[smallest] = result[smallest], result[i]
    return result

#Def. Val.

def default_array():
    return [10, 20, 30, 40, 50]

def default_stack():
    return [10, 20, 30, 40]

def default_queue():
    return [10, 20, 30, 40]

def default_singly_linked_list():
    linked_list = SinglyLinkedList()
    linked_list.insert(10)
    linked_list.insert(20)
    linked_list.insert(30)
    return linked_list

def default_doubly_linked_list():
    linked_list = DoublyLinkedList()
    linked_list.insert(10)
    linked_list.insert(20)
    linked_list.insert(30)
    return linked_list

def default_searching_array():
    return [10, 20, 30, 40, 50, 60]

def default_sorting_array():
    return [50, 20, 40, 10, 30]

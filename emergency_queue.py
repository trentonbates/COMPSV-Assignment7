class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency

class MinHeap:
    def __init__(self):
        self.data = list()

    def heapify_up(self, index):
        ...

    def heapify_down(self, index):
        ...

    def insert(self, patient):
        ...

    def print_heap(self):
        ...

    def peek(self):
        ...

    def remove_min(self):
        ...

# Test your MinHeap class here including edge cases
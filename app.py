from flask import Flask, render_template
from collections import deque

app = Flask(__name__)

# Define the Node class for the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to append data to the linked list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Method to convert the linked list to a Python list
    def to_list(self):
        node = self.head
        nodes = []
        while node:
            nodes.append(node.data)
            node = node.next
        return nodes

@app.route('/')
def index():
    # List
    sample_list = [1, 2, 3, 4, 5]

    # Dictionary
    sample_dict = {'a': 1, 'b': 2, 'c': 3}

    # Set
    sample_set = {1, 2, 3, 4, 5}

    # Tuple
    sample_tuple = (1, 2, 3, 4, 5)

    # Stack (using deque)
    sample_stack = deque([1, 2, 3, 4, 5])
    sample_stack.append(6)  # Push
    sample_stack.pop()      # Pop

    # Queue (using deque)
    sample_queue = deque([1, 2, 3, 4, 5])
    sample_queue.append(6)   # Enqueue
    sample_queue.popleft()   # Dequeue

    # Linked List
    sample_linked_list = LinkedList()
    sample_linked_list.append(1)
    sample_linked_list.append(2)
    sample_linked_list.append(3)

    return render_template(
        'index.html',
        sample_list=sample_list,
        sample_dict=sample_dict,
        sample_set=sample_set,
        sample_tuple=sample_tuple,
        sample_stack=list(sample_stack),
        sample_queue=list(sample_queue),
        sample_linked_list=sample_linked_list.to_list()
    )

if __name__ == '__main__':
    app.run(debug=True)

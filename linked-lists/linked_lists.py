class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

# This class will only be used to hold a reference to the first node object in our list. We will provide a constructor method to hold this information in a variable called head.


class LinkedList:
    def __init__(self):
        self.head = None

    def append_node(self, data):
        node = ListNode(data)
        if self.head is None:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def print_node(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def search_list(self, key):
        cur = self.head
        while cur and cur.data != key:
            cur = cur.next
        # if key was not present in the list, L will have become null
        return cur

    # def insert_after(self, node, new_node):
    #     new_node.next = node.next
    #     node.next = new_node

    # def delete_after(self, node):
    #     node.next = node.next.next


test = LinkedList()
test.append_node('A')
test.append_node('B')
test.append_node('C')

test.print_node()
print(test.search_list('C').data)


# http://theteacher.info/index.php/fundamentals-of-cs/5-data-structures/topics/4463-creating-a-linked-list-in-python
# https://stackabuse.com/python-linked-lists/

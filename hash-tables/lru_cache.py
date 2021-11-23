# 12.3 implement an ISBN cache
# The International Standard Book Number(ISBN) is a unique commercial book identifier. It is a string of length 10. The firrst 9 characters are digits; the last character is a check character. The check character is the sum of the first 9 digits, mod 11, with 10 represented by 'X'. (Modern ISBNs use 13 digits, and the check digit is taken mod 10; this problem is concerned with 10-digit ISBNs)
# Create a cache for looking up prices of books identified by their ISBN. For the purpose of this exercise, treat ISBNs and prices as positive integers. you must implement lookup, insert, and erase methods. use the Least Recently Used(LRU) policy for cache eviction.
# https://leetcode.com/problems/lru-cache/

# element:
# The tiem complexity for each loopup is O(1) for the hash table loopup and O(1) for updaing the queue, i.e., O(1) overall.
import collections


class LruCache:
    def __init__(self, capacity):
        self._isbn_price_table = collections.OrderedDict()
        self.capacity = capacity

    def lookup(self, isbn):
        if isbn not in self._isbn_price_table:
            return -1
        price = self._isbn_price_table.pop(isbn)
        self._isbn_price_table[isbn] = price

    def insert(self, isbn, price):
        # We add the value for key only if key is not present- we don't update existing values.
        if isbn in self._isbn_price_table:
            price = self._isbn_price_table.pop(isbn)
        elif len(self._isbn_price_table) == self._capacity:
            self._isbn_price_table.popitem(last=False)
        self._isbn_price_table[isbn] = price

    def erase(self, isbn):
        return self._isbn_price_table.pop(isbn, None) is not None


# yt:
# https://www.youtube.com/watch?v=7ABFKPK2hD4
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}  # map key to node

        # left=LRU, right=most recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

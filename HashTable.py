class Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.length = 0

  def add(self, newNode):
    if self.head is None:
      self.head = newNode
      self.length = 1
      return

    node = self.head

    while node.next is not None:
      if node.key == newNode.key:
        node.value = newNode.value
        return
      node = node.next

    if node.key == newNode.key:
        node.value = newNode.value
        return
    node.next = newNode
    self.length += 1

  def pop(self):
    node = self.head
    self.head = node.next
    node.next = None
    self.length -= 1
    return node
    

class HashTable:
  def __init__(self):
    self.size = 8
    self.array = [LinkedList()]*self.size
    self.numItems = 0

  def get(self, key):
    pos = hash(key) % self.size
    node = self.array[pos].head
    
    while node is not None:
      if node.key == key:
        return node.value

      node = node.next

    return None

  def add(self, key, value):
    node = Node(key, value)
    pos = hash(key) % self.size
    self.array[pos].add(node)
    
    self.numItems += 1

    if self.numItems*2 > self.size:
      self.resize()

  def resize(self):
    self.size *= 2
    self.numItems = 0
    oldArray = self.array
    self.array = [LinkedList()]*self.size

    for ll in oldArray:
      if ll is None:
        continue

      while ll.head is not None:
        node = ll.pop()
        self.add(node.key, node.value)
  
  def has(self, key):
    pos = hash(key) % self.size
    ll = self.array[pos]
    if ll.length == 0:
      return False

    node = ll.head
    while node is not None:
      if node.key == key:
        return True
      node = node.next

    return False


    

ht = HashTable()

ht.add("key", "value")
print(ht.get("key"))
ht.add("key", "newValue")
print(ht.get("key"))
print(ht.has("key"))
print(ht.has("key1"))
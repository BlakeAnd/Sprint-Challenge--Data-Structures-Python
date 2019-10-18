class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    # TO BE COMPLETED
    # if self.head and self.head.next_node and self.head.next_node.next_node:
    #   print("ok")
    #   stable_point = self.head
    #   current = self.head.next_node
    #   print("stable", stable_point.value)
    #   while current:
    #     stable_point.next_node = current.next_node
    #     current.next_node = stable_point
    #     current = self.head.next_node
    # elif self.head and self.head.next_node:
    #   end = self.head.next_node
    #   end.next_node = self.head
    current = self.head
    arr = []
    while current:
      arr.append(current.value)
      current = current.next_node
    # print(arr)
    current = self.head
    counter = 1
    while current:
      current.value = arr[len(arr) - counter]
      counter += 1
      current = current.next_node
      
      
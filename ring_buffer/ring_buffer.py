class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item
    self.current += 1
    if self.current == self.capacity:
      self.current = 0

  def get(self):
    stop_point = self.capacity
    for i in range(0, self.capacity):
      if self.storage[i] == None:
        stop_point = i
    #     print("i", i)

    # print(self.storage[:stop_point])
    return self.storage[:stop_point]
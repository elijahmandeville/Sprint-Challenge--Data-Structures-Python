class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.oldest = 0

    def append(self, item):
        # We will have to add to the beginning but remove from the end as well if the cap is met.

        # if len(self.data) >= self.capacity:
        #     self.data.pop(0)
        #     self.data.insert(len(self.data), item)
        # else:
        #     self.data.insert(len(self.data), item)

        if len(self.data) < self.capacity:
            self.data.append(item)
        else:
            self.data[self.oldest] = item
        self.oldest = (self.oldest + 1) % self.capacity

    def get(self):

        return [item for item in self.data if item is not None]

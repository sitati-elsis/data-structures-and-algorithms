class Stack:
    def __init__(self):
        self.storage = ""

    def push(self, word):
        self.storage = self.storage + "-" + word

    def pop(self):
        word = self.storage[self.storage.rfind('-')+1:]
        self.storage = self.storage[:self.storage.rfind('-')]
        return word

    def size(self):
        return len(self.storage)

food = Stack()
food.push("ugali")
food.push("skuma")
food.push("nyama")
print(food.size())
print(food.storage)
last = food.pop()
print(last)
print(food.storage)
print(food.size())
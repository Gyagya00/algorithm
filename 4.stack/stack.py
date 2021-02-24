def push(arr, s):
    arr.append(s)
    return arr

def pop(arr):
    return arr.pop(-1)

arr = []
push(arr, 1)
push(arr, 2)
push(arr, 3)

print(pop(arr))
print(pop(arr))
print(pop(arr))



class Stack():
    stack = []

    def push(self, data):
        self.stack.append(data)
        return self.stack

    def pop(self):
        data = self.stack.pop()
        return data

s = Stack()
print(s.push('하이'))
print(s.push('안녕'))
print(s.push('봉쥬르'))

print(s.pop())
print(s.stack )
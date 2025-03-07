class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Runtime complexity - O(n)
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            last = self.head
            if last.next:
                last = last.next
            last.next = Node(value)

    # Runtime complexity - O(1)
    def prepend(self, value):
        firstNode = Node(value)
        firstNode.next = self.head
        self.head = firstNode

    # Runtime comlexity - O(n)
    def insert(self, value, index):
        if index == 0:
            firstNode = Node(value)
            firstNode.next = self.head
            self.head = firstNode
        else:
            if self.head is None:
                raise ValueError("Index out of bounds")
            else:
                last = self.head
                for i in range(index - 1):
                    if last.next is None:
                        raise ValueError("Index out of bounds")
                    last = last.next
                newNode = Node(value)
                newNode.next = last.next
                last.next = newNode

    # Runtime complexity - O(n)
    def __contains__(self, value):
        last = self.head
        while last is not None:
            if last.value == value:
                return True
            last = last.next
        return False

    # Runtime complexity - O(n)
    def __len__(self):
        count = 0
        last = self.head if self.head else None
        while last is not None:
            last = last.next
            count += 1
        return count

    # Runtime complexity - O(n)
    def delete(self, value):
        last = self.head
        if last is not None:
            if last.value == value:
                self.head = last.next
            else:
                while last.next:
                    if last.next.value == value:
                        last.next = last.next.next
                        break
                    last = last.next

    # Runtime complexity - O(n)
    def pop(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last = self.head
            for i in range(index - 1):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next
            if last.next is None:
                raise ValueError("Index out of bounds")
            else:
                last.next = last.next.next

    # Runtime complexity - O(n)
    def get(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last = self.head
            for i in range(index):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next
            return last.next

    # def __repr__(self):
    #     if self.head is None:
    #         return "[]"
    #     else:


if __name__ == "__main__":
    l1 = LinkedList()
    l1.append(1)
    l1.prepend(0)
    l1.insert(2, 2)
    l1.delete(1)
    l1.pop(0)
    print(l1)

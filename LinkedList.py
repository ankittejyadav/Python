class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Non Linked List")
            return

        itr = self.head
        llstr = ""

        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next

        print(llstr)

    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insertValues(self, dataList):
        self.head = None
        for data in dataList:
            self.insertAtBeginning(data)

    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def removeAtIndex(self, index):
        if index < 0 or index > self.getLength():
            raise Exception("Index OutofBounds")

        # remove head
        if index == 0:
            self.head = self.head.next
            return

        # remove index
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
            itr = itr.next
            count += 1

    def insertAtIndex(self, index, data):
        if index < 0 or index > self.getLength():
            raise Exception("idx error")
        if index == 0:
            self.insertAtBeginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
            count += 1


if __name__ == "__main__":
    ll = LinkedList()
    # ll.insertAtBeginning(10)
    # ll.insertAtBeginning(2)
    ll.insertAtEnd(50)
    ll.insertAtEnd(500)
    ll.insertValues([1, 2, 3, 5])
    ll.removeAtIndex(2)
    ll.insertAtIndex(1, 11)
    ll.print()

    print(ll.getLength())

class PriorityQueueNode:

    def __init__(self, value, pr):
        self.data = value
        self.priority = pr
        self.next = None


class PriorityQueue:

    def __init__(self):

        self.front = None

    def isEmpty(self):

        return True if self.front is None else False

    def push(self, value, priority):

        if self.isEmpty():

            self.front = PriorityQueueNode(value, priority)

            return 1

        else:

            if self.front.priority > priority:

                newNode = PriorityQueueNode(value, priority)
                newNode.next = self.front

                self.front = newNode

                return 1

            else:

                temp = self.front

                while temp.next:

                    if priority <= temp.next.priority:
                        break

                    temp = temp.next

                newNode = PriorityQueueNode(value, priority)
                newNode.next = temp.next
                temp.next = newNode

                return 1

    def traverse(self):

        if self.isEmpty():
            return "Queue is Empty!"
        else:
            s = []
            temp = self.front
            while temp:
                print(temp.data)
                temp = temp.next


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.push(100, 0)
    pq.push(110, 1)
    pq.push(120, 2)
    pq.push(130, 3)

    pq.traverse()

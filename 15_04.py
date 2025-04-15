


class Node2:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:


    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head is None:
            return "Lista jest pusta"

    def append(self,data):
        nowy_wezel = Node2(data)
        if self.head is None:
            self.head = nowy_wezel
            return
        last= self.head
        while last.next is not None:
            last = last.next
        nowy_wezel = Node2(data)
        last.next = nowy_wezel
        last.prev =last

    def display_forward(self):
        if self.head is None:
            return "Lista jest pusta"
        else:
            current = self.head
            while current:
                print(current.data, end="->")
                current = current.next
            print("None")

    def display_backward(self):
        if self.head is None:
            print("Lista jest pusta")
        else:
            # Używamy listy pomocniczej do zebrania elementów
            elements = []
            current = self.head
            while current:
                elements.append(current.data)
                current = current.next
            # Wyświetlamy w odwrotnej kolejności
            for data in reversed(elements):
                print(data, end="->")
            print("None")

    def delete(self):
        if self.head is None:
            print("Lista jest pusta")
            

                

        




lista = DoublyLinkedList()

lista.append(1)
lista.append(2)
lista.append(3)



lista.display_forward()
lista.display_backward()





class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    union_dict = {}
    output_list = LinkedList()

    head = llist_1.head
    while head:
        union_dict[head.value] = ""
        head = head.next

    head = llist_2.head
    while head:
        if not union_dict.get(head.value):
            union_dict[head.value] = ""
            head = head.next
    
    for value in union_dict.keys():
        output_list.append(Node(value))
    
    return output_list


def intersection(llist_1, llist_2):
    inter_dict_1 = {}
    output_list = LinkedList()

    head = llist_1.head
    while head:
        inter_dict_1[head.value] = ""
        head = head.next
    
    head = llist_2.head
    while head:
        if inter_dict_1.get(head.value) is not None:
            output_list.append(Node(head.value))
        head = head.next

    return output_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("union", union(linked_list_1, linked_list_2))
print("inter", intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("union", union(linked_list_3, linked_list_4))
print("inter", intersection(linked_list_3, linked_list_4))


# Test Case 3

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,"dog",4,35,6,65,6,4,3,23]
element_2 = [1,7,None,9,11,"dog",1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("union", union(linked_list_3, linked_list_4))
print("inter", intersection(linked_list_3, linked_list_4))

# Test Case 4

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3]
element_2 = [3]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("union", union(linked_list_3, linked_list_4))
print("inter", intersection(linked_list_3, linked_list_4))


# Test Case 5

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = [3, 4, 4, None]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("union", union(linked_list_3, linked_list_4))
print("inter", intersection(linked_list_3, linked_list_4))


# Test Case 6

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("union", union(linked_list_3, linked_list_4))
print("inter", intersection(linked_list_3, linked_list_4))
#!/usr/bin/env python
# coding: utf-8

# In[32]:


class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    
    def insert_at_front(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = new_node
            p = new_node
            
            
    def middle(self):
        fast = self.head
        slow = self.head
        if self.head == None:
            print("list is empty.")
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        print("Middle elements is {0}".format(slow.data))
        
        
    def reverse(self):
        Next = None
        prev = None
        curr = self.head
        while curr != None:
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next
        self.head = prev
        
        
    def insert_at_position(self):
        data = int(input("value to be insert"))
        new_node = Node(data)
        pos = int(input("postion for insertion"))
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            p = self.head
            for i in range(1,pos-1):
                p = p.next
            new_node.next = p.next
            p.next = new_node
            p = new_node
            
    
    def insert_into_sorted_list(self):
        data = int(input("value to be insert"))
        new_node = Node(data)
        temp = self.head
        p = self.head
        while temp != None and temp.data <= new_node.data :
            p = temp
            temp = temp.next
        new_node.next = temp
        p.next = new_node
        p = new_node
        
        
    def reverse_in_k_size_group(self,head,k):
        count = 0
        Next = None
        prev = None
        curr = head
        while curr != None and count < k:
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next
            count+=1
            
        if Next != None:
            head.next = self.reverse_in_k_size_group(Next,k)
        self.head = prev
        return prev
    
    
    def nth_node_from_last(self,n):
        if self.head == None:
            print("empty list")
        first = self.head
        for i in range(n):
            first = first.next
        second = self.head
        while first != None:
            first = first.next
            second = second.next
        print(second.data)
        
    
    def delete_from_start(self):
        if self.head == None:
            print("underflow list")
        p = self.head.next
        self.head.next = None
        self.head = p
        
    
    def delete_from_last(self):
        first = self.head
        if self.head == None:
            print("list is empty")
        while first.next.next != None:
            first = first.next
        first.next = None 
        
        
    def delete_any_position(self,pos):
        if self.head == None:
            print("underflow list")
        if pos == 1:
            p = self.head.next
            self.head.next = None
            self.head = p
        else:
            temp = self.head
            for i in range(1,pos-1):
                temp = temp.next
            temp.next = temp.next.next
            
        
         
    def traverse(self):
        p = self.head
        if self.head == None:
            print("list is empty")
        while p != None:
            print(p.data,end="->")
            p = p.next
        print("None")

            
list = LinkedList()

n = int(input("number of values insert into list"))
for i in range(n):
    list.insert_at_end(int(input()))
    
# list.middle()
# list.insert_at_position()
# list.reverse()
# list.insert_into_sorted_list()
# list.reverse_in_k_size_group(list.head,int(input("size of goup for rotation")))
# list.nth_node_from_last(int(input("pos of node from last")))
# list.delete_from_start()
# list.delete_from_last()
list.delete_any_position(int(input("enter position for deletion")))
list.traverse()     


# ## 

# In[ ]:





# In[ ]:





# In[ ]:





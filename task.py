#Implimentation of Link_list Data Structure
#Intialize the Node class of Link_list



class Node:
    def __init__(self,data):       #Node class have two perimeters 1st is Data and 2nd is pointer next 
        self.data=data                           
        self.next=None             #Intially next is None
    def display(self):             #Function to display data 
        print(self.data,end="\t")    
class Linklist:
    def __init__(self):
        self.head=None
    def addatStart(self):
        value=int(input("Enter the data:"))
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode          
    def addatEnd(self):
        value=int(input("Enter the data:"))
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode 
    def removeatstart(self):
        if self.head==None:
            print("The linklist is EMPTY!")
        else:
            self.head=self.head.next
    def removeatend(self):
        if self.head==None:
            print("The linklist is Empty!")
        else:
            temp=self.head
            preveious=None
            while temp.next!=None:
                preveious=temp
                temp=temp.next
            preveious.next=None    
    def size(self):
        if self.head==None:
            print("The linklist is Empty!")
        else:
            pointer=self.head
            size=0
            while pointer.next!=None:
                size=size+1
                pointer=pointer.next
            return (size+1)
    def sum(self):
        if self.head==None:
            print("The linklist is Empty!")
        else:
            pointer=self.head
            sum_data=0
            while pointer.next!=None:
                sum_data=sum_data+pointer.data
                pointer=pointer.next
            sum_data=sum_data+pointer.data
            return sum_data 
    def Average(self):
        if self.head==None:
            print("The Linklist is Empty!")
        else:
            sum_data=self.sum()
            size=self.size()
            average=sum_data/size
            print("Average of Linklist is:",int(average))
    def maximum(self):
        if self.head==None:
            print("The Linklist is Empty!")
        else:
            pointer=self.head
            maximum_number=pointer.data
            while pointer.next!=None:
                if maximum_number<pointer.data:
                    maximum_number=pointer.data
                pointer=pointer.next 
            if pointer.data >maximum_number:
                print("The maximum number of linklist is:",pointer.data)
            else:    
                print("Mximum number is:",maximum_number) 
    def minimum(self):
        if self.head==None:
            print("The Linklist is Empty!")
        else:
            pointer=self.head
            minimum_number=pointer.data
            while pointer.next!=None:
                if minimum_number>pointer.data:
                    minimum_number=pointer.data
                pointer=pointer.next 
            if pointer.data <minimum_number:
                print("The minimum number is:",pointer.data)
            else:    
                print("Minimum number is:",minimum_number)
    def middle_element(self):   #This function by counting the size and then iterate util it achieve
        if self.head==None:
            print("The linklist is Empty!")
        else:
            pointer=self.head
            size=(self.size())
            mid_number=size/2
            count=1
            while count!=mid_number:
                count+=1
                pointer=pointer.next
            return pointer.data
    def middle_element_pointer(self):     #This Function is by using two pointers.
        if self.head==None:
            print("The Linklist is Empty!")
        else:
            first_pointer=self.head
            second_pointer=self.head
            while first_pointer!=None:
                second_pointer=second_pointer.next
                first_pointer=first_pointer.next.next
            return second_pointer.data                                                                                                        
    def display(self):
        if self.head==None:
            print("The Linklist is Empty")
        else:
            temp=self.head
            while temp!=None:
                temp.display()
                temp=temp.next
            print("\t")   

L1=Linklist()
L1.addatStart()
L1.addatStart()
L1.addatStart()
L1.addatEnd()
L1.addatEnd()
L1.addatEnd()
L1.display()
print(L1.middle_element())   
print(L1.middle_element_pointer())                                 
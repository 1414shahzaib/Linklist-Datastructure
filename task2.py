class Numbers:
    def __init__(self,data):
        self.data=data
        self.next=None
    def display(self):
        print(self.data,end="\t")
class Linklist:
    def __init__(self):
        self.head=None
    def addAtstart(self):
        value=int(input("Enter the data:"))
        newnode=Numbers(value)
        if self.head==None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def removefromstart(self):
        if self.head==None:
            print("The linklist is Empty")
        else:
            self.head=self.head.next
    def displayNumbers(self):
        if self.head==None:
            print("The Linklist is Empty")
        else:
            temp=self.head
            while temp!=None:
                temp.display()
                temp=temp.next
            print("\t")

L1=Linklist()            
L1.addAtstart()
L1.addAtstart()
L1.displayNumbers()
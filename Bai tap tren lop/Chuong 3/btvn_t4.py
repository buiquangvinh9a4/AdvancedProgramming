class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.len = 0
    
    def insert(self, data):   # chèn data vào đầu danh sách
        newNode = ListNode(data)
        newNode.next = self.head
        self.head = newNode
        self.len += 1
                
    def printList(self):     # In danh sách
        curNode = self.head
        while curNode is not None:
            print(curNode.data)
            curNode = curNode.next
    
    def len(self):          # In số lượng các nút danh sách
        return self.len
    
    def checkList(self, x):          # Kiểm tra danh sách có nút nào chứa giá trị x không
        curNode = self.head
        while curNode is not None and curNode.data != x:
            curNode = curNode.next
        return curNode is not None

    def addList(self, L, x):
        if L.checkList(x) == False:
            L.insert(x)
    
    def deleteNode(self, x):        # xóa giá trị x khỏi danh sách nếu danh sách chứa x
        predNode = None
        curNode = self.head
        while curNode is not None and curNode.data != x:
            predNode = curNode
            curNode = curNode.next
        if curNode is not None:
            if curNode is self.head:
                head = curNode.next
            else:
                predNode.next = curNode.next
        
            

L = List()
L.insert(2)
L.insert(3)
L.insert(4)
L.printList()
L.addList(L, 5)
L.printList()

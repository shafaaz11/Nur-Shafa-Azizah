class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def is_empty(self):
        return self.front is None
    
    def enqueue(self, data):
        new_node = Node(data)
        
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
    def dequeue(self):
        if self.is_empty():
            return None
        
        temp = self.front
        self.front = temp.next
        
        if self.front is None:
            self.rear = None
        return temp.data
    
    def display(self):
        if self.is_empty():
            print("TIDAK ADA PESANAN")
            return
        
        current_node = self.front
        while current_node:
            print(current_node.data)
            current_node = current_node.next
            
def main():
    queue = Queue()
    
    while True:
                
        print('''
⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅
⫸ SELAMAT DATANG DI RESTORAN TONYCHOPPER ⫷
⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅''')
        print('''
SILAHKAN PILIH MENU :
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
⫕⫖ 1) Tambah Data Antrian       ⫕⫖
⫕⫖ 2) Hapus Data Antrian        ⫕⫖
⫕⫖ 3) Tampilkan Data Antrian    ⫕⫖
⫕⫖ 4) Keluar Dari Antrian       ⫕⫖
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■''')
        choice = input("PILIH MENU : ")
        

        
        if choice == '1':    
            print('''
-------------------------------                  
Silahkan Masukan Pesanan !
-------------------------------
    ''')
            item = input("Pembeli Memesan: ")
            queue.enqueue(item)
        
        elif choice == '2':
            item = queue.dequeue()
            if item is None:
                print("ANTRIAN KOSONG")
            else:
                print(f'''
----------------------------------------
Pesanan {item} telah siap !
{item} Terhapus Dari Antrian
----------------------------------------
''')
                
        elif choice == '3':
            print('''
-----------------------------------
Menampilkan Pesanan Dalam Antrian !
----------------------------------- 
''')
            queue.display()
            
        elif choice == '4':
            print("ANDA KELUAR DARI PEMESANAN !")
            break
        else:
            print("PILIHAN TIDAK ADA")
            
if __name__ == '__main__':
    main()
    

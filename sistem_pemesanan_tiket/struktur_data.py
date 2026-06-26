# FILE 1
# LinkedList, Queue, Sorting

# LINKED LIST
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        node_baru = Node(data)
        if self.head is None:
            self.head = node_baru
        else:
            sekarang = self.head
            while sekarang.next is not None:
                sekarang = sekarang.next
            sekarang.next = node_baru

    def tampilkan(self):
        sekarang = self.head
        nomor = 1
        while sekarang is not None:
            print(f'  {nomor}. {sekarang.data}')
            sekarang = sekarang.next
            nomor += 1

    def kosong(self):
        return self.head is None


# QUEUE
class Queue:
    def __init__(self):
        self.data = []

    def masuk(self, item):
        self.data.append(item)

    def keluar(self):
        if not self.kosong():
            return self.data.pop(0)
        return None

    def kosong(self):
        return len(self.data) == 0

    def ukuran(self):
        return len(self.data)


# BUBBLE SORT
def bubble_sort(daftar, kolom):
    n = len(daftar)
    for i in range(n):
        for j in range(0, n - i - 1):
            try:
                a = float(daftar[j][kolom])
                b = float(daftar[j + 1][kolom])
            except:
                a = daftar[j][kolom]
                b = daftar[j + 1][kolom]
            if a > b:
                daftar[j], daftar[j + 1] = daftar[j + 1], daftar[j]
    return daftar


# LINEAR SEARCH
def linear_search(daftar, kolom, kata_kunci):
    hasil = []
    for item in daftar:
        if kata_kunci.lower() in item[kolom].lower():
            hasil.append(item)
    return hasil

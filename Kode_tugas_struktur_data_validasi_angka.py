# ==========================================
# SISTEM MANAJEMEN INVENTORI TOKO
# ==========================================

class BSTNode:
    def __init__(self, produk):
        self.produk = produk
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, produk):
        if root is None:
            return BSTNode(produk)

        if produk["nama"].lower() < root.produk["nama"].lower():
            root.left = self.insert(root.left, produk)
            
        else:
            root.right = self.insert(root.right, produk)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(
                f"SKU: {root.produk['sku']} | "
                f"Nama: {root.produk['nama']} | "
                f"Stok: {root.produk['stok']}"
            )
            self.inorder(root.right)

# ==========================================
# CIRCULAR QUEUE
# ==========================================

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.count = 0

    def enqueue(self, item):

        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.size

        if self.count < self.size:
            self.count += 1
        else:
            self.front = (self.front + 1) % self.size

    def display(self):

        if self.count == 0:
            print("Belum ada transaksi.")
            return
        print("\n===== RIWAYAT TRANSAKSI =====")

        idx = self.front

        for _ in range(self.count):
            print("-", self.queue[idx])
            idx = (idx + 1) % self.size

# ==========================================
# HASH TABLE
# ==========================================

inventory = {}

def tambah_produk(sku, nama, stok):
    inventory[sku] = {
        "sku": sku,
        "nama": nama,
        "stok": stok
    }

def cari_produk(sku):
    return inventory.get(sku)


def input_angka(pesan):
    while True:
        nilai = input(pesan)
        if nilai.isdigit():
            nilai = int(nilai)
            if nilai > 0:
                return nilai
            else:
                print("Jumlah harus lebih dari 0!")
        else:
            print("Input harus berupa angka!")

# ==========================================
# INISIALISASI
# ==========================================

bst = BST()

transaksi = CircularQueue(10)

# ==========================================
# MENU
# ==========================================

while True:
    print("\n")
    print("=" * 40)
    print(" SISTEM MANAJEMEN INVENTORI TOKO ")
    print("=" * 40)
    print("1. Tambah Produk")
    print("2. Cari Produk")
    print("3. Stok Masuk")
    print("4. Stok Keluar")
    print("5. Lihat Inventori")
    print("6. Riwayat Transaksi")
    print("0. Keluar")

    pilihan = input("Pilih menu : ")

    # ======================================
    # TAMBAH PRODUK
    # ======================================

    if pilihan == "1":

        sku = input("Masukkan SKU : ")

        if sku in inventory:
            print("SKU sudah ada!")
            continue

        nama = input("Nama Produk : ")
        stok = input_angka("Jumlah Stok : ")

        produk = {
            "sku": sku,
            "nama": nama,
            "stok": stok
        }

        inventory[sku] = produk

        bst.root = bst.insert(bst.root, produk)

        transaksi.enqueue(
            f"Tambah Produk {nama} (stok {stok})"
        )

        print("Produk berhasil ditambahkan!")

    # ======================================
    # CARI PRODUK
    # ======================================

    elif pilihan == "2":

        sku = input("Masukkan SKU : ")

        produk = cari_produk(sku)

        if produk:

            print("\nDATA PRODUK")
            print("SKU  :", produk["sku"])
            print("Nama :", produk["nama"])
            print("Stok :", produk["stok"])

        else:
            print("Produk tidak ditemukan!")

    # ======================================
    # STOK MASUK
    # ======================================

    elif pilihan == "3":

        sku = input("Masukkan SKU : ")

        if sku not in inventory:
            print("Produk tidak ditemukan!")
            continue

        jumlah = input_angka("Jumlah masuk : ")

        inventory[sku]["stok"] += jumlah

        transaksi.enqueue(
            f"{inventory[sku]['nama']} masuk {jumlah}"
        )

        print("Stok berhasil ditambah!")

    # ======================================
    # STOK KELUAR
    # ======================================

    elif pilihan == "4":

        sku = input("Masukkan SKU : ")

        if sku not in inventory:
            print("Produk tidak ditemukan!")
            continue

        jumlah = input_angka("Jumlah keluar : ")

        if inventory[sku]["stok"] < jumlah:
            print("Stok tidak mencukupi!")
            continue

        inventory[sku]["stok"] -= jumlah

        transaksi.enqueue(
            f"{inventory[sku]['nama']} keluar {jumlah}"
        )
        print("Transaksi berhasil!")
        if inventory[sku]["stok"] <= 5:
            print("⚠ PERINGATAN: STOK MENIPIS!")

    # ======================================
    # LIHAT INVENTORI
    # ======================================

    elif pilihan == "5":
        if len(inventory) == 0:
            print("Inventori masih kosong!")
        else:
            print("\n===== DATA INVENTORI =====")
            bst.inorder(bst.root)

    # ======================================
    # RIWAYAT TRANSAKSI
    # ======================================

    elif pilihan == "6":
        transaksi.display()

    # ======================================
    # KELUAR
    # ======================================

    elif pilihan == "0":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")

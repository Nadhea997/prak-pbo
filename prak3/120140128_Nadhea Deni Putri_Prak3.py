class Dagangan:
    total_barang = 0
    barang_list = []

    def __init__(self, nama, stok, harga):
        self.__nama = nama
        self.__stok = stok
        self.__harga = harga
        Dagangan.total_barang += 1
        Dagangan.barang_list.append((nama, stok, harga))

    @classmethod
    def tampil_barang(self):
        print(f"Total barang dagangan pada toko: {self.total_barang} buah")
        for i, barang in enumerate(self.barang_list, start=1):
            nama, stok, harga = barang
            print(f"{i}. {nama} harga Rp {harga} (stok: {stok})")

    def __del__(self):
        Dagangan.total_barang -= 1
        for i, barang in enumerate(Dagangan.barang_list):
            if barang[0] == self.__nama:
                del Dagangan.barang_list[i]
                break

Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)
Dagangan.tampil_barang()
print(f"\n{Dagangan1._Dagangan__nama} dihapus dari toko!\n")
del Dagangan1

Dagangan.tampil_barang()

print(f"\n{Dagangan2._Dagangan__nama} dihapus dari toko!")
del Dagangan2

print(f"\n{Dagangan3._Dagangan__nama} dihapus dari toko!")
del Dagangan3

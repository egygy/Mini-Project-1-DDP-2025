print("_"*50)
print("Nama: Muhammad Arzad")
print("NIM: 2509116014")
print("Kelas: Sistem Informasi A 2025")
print(" MINI PROJECT 1 ")
print("_"*50)

# Tuple untuk menu kopi 
jenis_kopi = ("Americano", "Latte", "Cappuccino", "Kenangan Mantan", "Spanish Latte")

# list
penjualan = []

# Menu Kopi yang Tersedia
print(" Menu Kopi yang Tersedia:")
print("1. Americano - Rp 17.000")
print("2. Latte - Rp 22.000")
print("3. Cappuccino - Rp 22.000")
print("4. Kenangan Mantan - Rp 19.000")
print("5. Spanish Latte - Rp 19.000")

# Menu Utama
print("1. Tambah Penjualan")
print("2. Hapus Penjualan") 
print("3. Keluar")
    
pilih = input("Pilih Menu Utama: ")



if pilih == "1":
    # Tambah Pepenjualan
    nama_pelanggan = input("Nama Pelanggan:, ")
    kopi = input("Nama kopi:, ")
    jumlah = int(input("Jumlah cup:, "))
    harga = int(input("Harga per cup:, "))
    total = jumlah * harga
        
    penjualan.append([nama_pelanggan, kopi, jumlah, harga, total])
    print(f"{nama_pelanggan} - {kopi} - Rp {total} ditambahkan!")
        
elif pilih == "2":
    # Hapus Penjualan
    if not penjualan:
        print("Belum ada penjualan!")
        
    else:
        print(f"Terakhir: {penjualan}")
    if input("Hapus? (Iya): ") == 'Iya':
        print(f"{penjualan} Berhasil dihapus!")
                
elif pilih == "3":
    print("Terima kasih!")
        
        
else:
    # Keluar
    print("Pilihan salah!")
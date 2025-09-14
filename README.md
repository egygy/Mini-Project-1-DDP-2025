# Mini-Project-1-DDP-2025
# Profil

Nama: Muhammad Arzad NIM: 2509116014 Sistem Informasi A'2025

# Deskripsi Singkat

Program Sistem Menejemen Penjualan Kopi Kenalan di buat untuk membantu usaha dalam mengelola transaksi penjualan harian mereka.
Sistem ini menawarkan 3 fungsi utama sebagai berikut:
- Menambah Penjualan Baru
- Menghapus Penjualan
- Keluar dari program

# Alur Program
**1. Menambah Penjualan Baru**

<img width="228" height="193" alt="image" src="https://github.com/user-attachments/assets/ca41835f-4bb1-43fb-b61a-bb2f1b567aa5" />

Pada menu menambah penjualan baru pengguna menginput Nama Pelanggan - Nama Kopi - Jumlah Cup - Harga Per Cup, program akan menghitung total harga pesanan, dan akan muncul output "Berhasil ditambahkan"

**2. Menghapus Pesanan**

<img width="317" height="26" alt="image" src="https://github.com/user-attachments/assets/a698c86f-c1ad-42e9-b79c-55157a5dee8c" />

Pada menu Menghapus Pesanan pengguna dapat menghapus pesanan yang sudah di tambahkan

**3. Keluar dari Program**

<img width="140" height="65" alt="image" src="https://github.com/user-attachments/assets/512b0b65-1ef0-441a-8916-3097dd943f63" />

Pada menu Keluar dari Program pengguna dapat keluar dari program jika tidak jadi menginput pesanan dan akan memberikan output "Terima Kasih"

# Penjelasan Flowcart

![Mini Project 1 DDP 2025](https://github.com/user-attachments/assets/6905624f-fb64-4f57-b1c3-5fbb7e80266e)


**1. Menu Utama**

Dimulai dengan menampilkan tiga opsi:
- Tambah Pesanan
- Hapus Pesanan
- Keluar

**2. Alur Tambah Pesanan**

Jika pengguna memilih 1, program akan:
- Meminta input: Nama Pelanggan - Nama Kopi - Jumlah Cup - Harga Per Cup
- Menghitung Total Harga (Jumlah Cup × Harga Per Cup)
- Menampilkan output "Berhasil Ditambahkan"
- Program Selesai

**3. Alur Hapus Pesanan**

  Jika pengguna memilih 2, program akan:
  - Memeriksa apakah list penjualan kosong
  - Jika kosong akan menampilakan "Belum Ada Penjualan!"
  - Jika tidak kosong: Menghapus pesanan dan meminta konfirmasi "Hapus? yes"
  - Menampilkan output "Nama Pelanggan - Nama Kopi - Jumlah Cup - Harga Per Cup" "Berhasil Dihapus"
  - Program selesai

**4. Alur Keluar**

Jika pengguna memilih 3, program akan
- Menampilkan "Terima Kasih"
- Program selesai

**5. Input tidak valid**

Jika pengguna memilih selain 1, 2, atau 3, program akan:
- Menampilkan "Pilihan salah"
- Program selesai

# Mini-Project-1-DDP-2025
Nama: Muhammad Arzad NIM: 2509116014 Sistem Informasi A'2025

**PENJELASAN PEMROGRAMAN**

Pemrograman ini merupakan sebuah sistem penjualan sederhana yang di rancang khusus untuk kafe seperti Kopi Kenangan. Sistem ini di bangun menggunakan bahasa pemrograman python dan berfungsi untuk mencatat dan mengelola transaksi penjualan berbagai menu kopi

Dalam pemrograman ini saya menggunakan Conditional Statements, List & Tuple. Untuk list berfungsi untuk menyimpan semua data transaksi penjualan yang terjadi, dan tuple berisi daftar menu kopi yang tersedia , yang bersifat tetap dan tidak dapat diubah selama program berjalan. Setiap transaksi dicatat dengan detail lengkap seperti Nama Pelanggan, Jenis Kopi yang di pesan, Jumlah Cup, Harga per Cup, dan Total harga yang harus di bayar.

Sistem ini menawarkan 3 fungsi utama sebagai berikut:
- Menambah Penjualan Baru
- Menghapus Penjualan
- Keluar dari program

**PENJELASAN FLOWCHART**
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

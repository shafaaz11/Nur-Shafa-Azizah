#FUNGSIONALITAS PROGRAM

Linked list adalah sekumpulan elemen bertipe sama, yang mempunyai keterurutan tertentu, yang setiap elemennya terdiri dari dua bagian Linked list berfungsi untuk untuk menyimpan suatu data dengan terstruktur sehingga dapat secara otomatis menciptakan suatu tempat baru untuk menyimpan data yang diperlukan.

Disini saya menggunakan struktur data Queue. Queue adalah struktur data linier yang menerapkan prinsip operasi dimana elemen data yang masuk pertama akan keluar lebih dulu. Prinsip ini dikenal dengan istilah FIFO (First In, First Out). Jadi program saya berfungsi untuk memudahkan pengguna dalam menginput data pembeli.



#CARA KERJA PROGRAM(RESTORAN) DAN OUTPUT PROGRAM

Dalam program ini kita membuat objek kelas Node dan kelas Queue. Kita juga menambahkan fungsi 'main' yang digunakan untuk meminta input dari pengguna dan menjalankan operasi pada antrian. Kemudian didalam fungsi 'main' kita membuat sebuah loop atau perulangan yang terus berjalan sampai pengguna memilih untuk keluar dari program. Dalam loop kita menampilkan pilihan menu yang tersedia untuk pengguna dengan menggunakan fungsi input.

Jika pengguna menjalankan program maka output akan menampilkan pilihan menu yang tersedia, pengguna disuruh memilih, jika pengguna memilih pilihan 1 maka akan diminta untuk memasukan nomor antrian, nama, dan pesenan yang ingin dipesan agar bisa ditambahkan kedalam antrian. Jika pengguna memilih pilihan 2 maka output akan mencetak pesanan yang dihapus (atau untuk logika program yang saya buat menu ini seperti menghapus pesanan pembeli yang pertama masuk karena telah dilayani sehingga pembeli dapat keluar dari antrian). Jika pengguna memilih pilihan 3 maka akan menampilkan seluruh pesanan yang telah input oleh pengguna (atau menu ini berfungsi agar pengguna tau pembeli mana yang harus dilayani selanjutnya sesuai dengan antrian). Jika pengguna memilih pilihan 4 maka pengguna akan keluar, kemudian program keluar dari loop 'while true' dan program selesai.



#METODE PROGRAM
Pada program yang saya buat, saya menggunakan beberapa metode berikut :
1. IsEmpty untuk memeriksa apakah antrian kosong
2. Enqueue untuk menambahkan elemen ke akhir antrian
3. Dequeue untuk menghapus elemen dari depan antrian
4. Display untuk menampilkan antrian yang ada
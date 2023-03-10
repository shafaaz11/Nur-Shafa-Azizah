# PENJELASAN PROGRAM 

Pertama disitu kita membuat fungsi untuk mencari item dari parameter mylist dan char, mylist itu list yang bakal kita pake dan char itu item yang bakal kita cari didalam mylist. Setelah itu kita membuat perulangan dimana sub_list itu adalah rentang panjang mylist jadi maksudnya for sub_list in mylist itu dia bakal ngejabarin mylist tadi. Karena sudah dijabarin mylist kita tadi menjadi sub_list kita buat baru pengkondisian buat nyari char yang kita pengen, jika char yang pengen kita cari itu ada di sub_list maka output akan menampilkan nilai indexnya. Kenapa ada index dan sub_index karena ada nested list atau list didalam list.


# CARA KERJA PROGRAM 

Jika user menjalankan program, maka output akan meminta user untuk memasukkan item yang ingin dicari oleh user. Setelah user menginput item yang diinginkan maka program akan mensearching menggunakan metode linearsearch dan kemudian menampilkan index dan kolom dari item yang dicari oleh user


# FUNGSIONALITAS PROGRAM 

Linear Search merupakan sebuah teknik pencarian data dengan menelusuri semua data satu per satu. Apabila ditemukan kecocokan data maka program akan mengembalikan output, jika tidak maka pencarian akan terus berlanjut hingga akhir dari array tersebut. Algoritma ini tidak cocok untuk set data dengan jumlah besar karena kompleksitas dari algoritma ini adalah 0(n) dimana n adalah jumlah item. Jika data yang dicari berada paling akhir dari array, maka program harus menelusuri semua array terlebih dahulu

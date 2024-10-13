
# Praktikum Mini Projek 2

# Profil Diri

Putri Syafana Afrillia | 2409116015 | Sistem Informasi A | Sistem Pembagian Nilai (Rapot)

# Flowchart

![MINPRO2 drawio](https://github.com/user-attachments/assets/e2f1c9a9-039b-4509-8701-123a7b78598b)


# Menu Login

![image](https://github.com/user-attachments/assets/c55519af-736b-4eb8-a406-7388787d77c4)


Gambar diatas menunjukan user akan dipilih sesuai rolenya yaitu Guru atau Murid. Menu yang akan ditampilkan sesuai dengan role yang dipilih.

# <sub>Penjelasan Menu Mode Login</sub>

  1. Admin (Guru) yang datanya terdaftar, bisa melakukan sistem CRUD (Create, Read, Update, Delete) pada list atau data siswa terutama nilai.
  2. Murid, hanya dapat melakukan login untuk melihat data nilai siswa juga melakukan pengajuan jika merasa keberatan dengan nilai yang sudah diumumkan.

Berikut kode untuk menampilkan halaman awal untuk memilih role.

![image](https://github.com/user-attachments/assets/3b1a13d0-15d1-45e0-a2b9-5dd76f939473)

     
* **Jika user memilih selain 1 atau 2, maka akan otomatis kembali ke menu utama**

![image](https://github.com/user-attachments/assets/7efb055d-4df8-4898-a5f4-1189bcd7bd9e)


Jika user menginputkan angka selain 1 dan 2 otomatis akan kembali ke Menu Mode Login. Berikut kode untuk data login para Guru dan Siswa yang telah terdaftar.

![image](https://github.com/user-attachments/assets/e1217cd0-95cc-461e-857f-700b61b24368)

Berikut kode untuk fungsi definisi untuk masing-masing login role. Jika user memasukkan data yang tidak terdaftar atau salah, maka akan diarahkan untuk mengisi data kembali.

![image](https://github.com/user-attachments/assets/d8290320-436f-4230-94d2-b99d3ff02823)


# Mode Guru

![image](https://github.com/user-attachments/assets/ec49d4c6-f4a2-40a3-9e71-895a38797aa6)

Di mode Guru akan diberikan 5 pilihan seperti gambar diatas, setelah input nomor pilihan, guru akan diarahkan sesuai dengan yang dipilih. Berikut kode untuk bagian ini. Setiap nomor pilihan yang akan dipilih, akan diarahkan ke masing-masing fungsi yang telah dibuat. 

![image](https://github.com/user-attachments/assets/1f40e133-c0cc-4134-a29f-4cc6e2e0f812)

# <sub>Penjelasan Fitur Admin</sub>

1. Tambah data nilai murid
   
   ![image](https://github.com/user-attachments/assets/b99e2f9d-b2c5-4840-b841-c1133cbe3066)

    Ketika user memilih opsi 1, maka langsung diarahkan ke fungsi definisi penambahan data dengan kode sebagai berikut. Guru harus menginput data siswa yang baru. 

   ![image](https://github.com/user-attachments/assets/f61c481c-9fcd-46d2-bb40-189589521572)

2. Lihat data

   ![image](https://github.com/user-attachments/assets/48bfd65a-9bd8-4c1d-851a-79a685b90325)

    Tabel ini berisi data yang ada di variabel 'data_tabel'. Tabel ini akan selalu diperbarui sesuai sistem yang berjalan, entah itu diubah, ditambah, atau dihapus. Berikut kode untuk menampilkan tabelnya.

   ![image](https://github.com/user-attachments/assets/0dfb0ee6-04e7-4d19-8208-1b8ac0517705)

3. Ubah data

  ![image](https://github.com/user-attachments/assets/f5f62ce1-5b2b-4e1a-856f-f5c6c91cbf96)

  Ketika guru memilih fitur ini, maka guru dapat mengubah data yang sudah ada dengan data yang baru, dimana guru memasukkan datanya sendiri, termasuk NISN dan nilai. Berikut kode untuk memunculkan fitur ini. Indeks yang dimasukkan harus sesuai.

  ![image](https://github.com/user-attachments/assets/d6e00ac5-89e5-4be1-8ecd-2d0afabf653f)
  
4. Hapus Barang

    ![image](https://github.com/user-attachments/assets/0ba327bc-2732-425f-ad06-2ed770906780)

   Contoh penghapusan data tertera, guru diminta memasukkan nama murid yang akan dihapus dari data penilaian. Jika nama yang dimasukkan tidak ditemukan di data, maka guru akan diarahkan untuk mengulang kembali pengisian nama yang ingin dihapus. Berikut kodenya, tabel akan otomatis diperbarui setelah salah satu nama dihapus.

   ![image](https://github.com/user-attachments/assets/62914899-b117-4ecd-9a05-526874d180af)

5. Logout (Keluar)
   
   Jika guru memilih untuk logout, maka program akan otomatis diberhentikan dengan fungsi exit yang sudah dibuatkan. Guru akan diyakinkan terlebih dahulu apakah ingin berhenti atau kembali ke menu guru.

   ![image](https://github.com/user-attachments/assets/18671c67-0329-43c7-831c-da2dada839b6)

   Berikut kode untuk mengakhiri program (exit).

   ![image](https://github.com/user-attachments/assets/e3bb3e51-a9ce-484b-a370-26770d8cb30b)

# Menu murid

![image](https://github.com/user-attachments/assets/c6a39091-f92d-4611-8951-ec4b4beea976)

Murid diharuskan login dengan data yang benar. Jika murid memasukkan data yang salah, maka program otomatis akan mengulang bagian login hingga data yang dimasukkan adalah data yang benar atau yang terdata dalam database (program). Ketika sudah berhasil masuk, maka murid akan ditampilkan menu sebagai berikut.

![image](https://github.com/user-attachments/assets/c215003b-066f-41fe-915d-4090937c0be4)

Sama seperti menu guru, ada nomor pilihan yang bisa dipilih. Jika yang dimasukkan adalah nomor diluar pilihan, maka output yang keluar menunjukkan bahwa pilihan/fitur tersedia, murid akan diarahkan untuk memilih kembali.

1. Melihat data nilai murid.

   ![image](https://github.com/user-attachments/assets/8f945997-0c49-4d02-b730-dcf83e5b0e30)

    Fitur ini akan menampilkan tabel yang berisi data yang ada di variabel 'data_tabel'. Tabel ini hanya bisa dimodifikasi oleh guru, murid hanya bisa melihat. Untuk menampilkan fitur tersebut,hanya perlu memanggil gungsi definisi untuk bagian tabel.
   
2. Mengajukan

 ![image](https://github.com/user-attachments/assets/72b3f3fd-ba16-4e7c-a8bd-b76daa79250c)

  Ketika murid memilih fitur ini, akan langsung diarahkan mengisi data diri dan alasan mengapa dilakukan pengajuan seputar nilai. Berikut kode yang dipakai.

  ![image](https://github.com/user-attachments/assets/202d7f52-30c9-48a5-8b53-16b88debf053)

3. Logout (Keluar)
   
   Jika murid memilih untuk logout, maka program akan otomatis diberhentikan dengan fungsi exit yang sudah dibuatkan.

   ![image](https://github.com/user-attachments/assets/18671c67-0329-43c7-831c-da2dada839b6)

   Kode untuk mengakhiri program (exit) sama seperti di menu guru


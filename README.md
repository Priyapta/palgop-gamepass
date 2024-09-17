![Screenshot 2024-09-17 213243](https://github.com/user-attachments/assets/f1f29ba9-27da-4a28-a161-f03961efe2e4)# PalgopGamepass 🏪

## Link Deployment -> [PalgopGamepass](http://priyapta-naufal-palgopgamepass.pbp.cs.ui.ac.id/)

## Tugas 3 PBP 2024/2025

### Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery berguna untuk pengiriman data dalam platform. Data delivery berfungsi untuk meingirmkan data dengan tepat dan aman tanpa adanya data delivery membuat pengiriman data dalam platform tidak efisien dan tepat.

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Penggunaan JSON lebih banyak dipakai karena secara penulisan code lebih mudah dibaca dan JSON tidak memerlukan tag tertutup sehingga menghindari kesalahan dalam menulis code.

### Jelaskan fungsi dari method 'is_valid()' pada form Django dan mengapa kita membutuhkan method tersebut?
Method ini berguna untuk memastikan input yang dimasukan user sesuai dengan ketentuan yang telah dibuat. Lalu, method ini akan mengembalikan kondisi True dan False jika True maka input sudah sesuai dan False jika ada data yang dimasukan user tidak sesuai.

### Mengapa kita membutuhkan 'csrf_token' saat membuat form di Django? Apa yang dapat terjadi jika kita tidak
csrf_token digunakan untuk melindungi data yang telah dikirimkan oleh pengguna. 'csrf_token' adalah token yang berfungsi sebagai security dan di-generate secara otomatis oleh Django untuk mencegah serangan berbahaya seperti serangan csrf (cross-site request forgery). Sebagai contoh jika data yang dikirimkan oleh pengguna kepada suatu platform atau web dan data yang sudah terautentikasi dilakukan pemalsuan seperti mengirimkan pesan email atau sms untuk memaksa user melakukan berbagai permintaan dari penyerang. Dengan menggunakan 'csrf_token' dapat menghindari dari serangan tersebut 

### Screenshot
XML
![Screenshot 2024-09-17 213243](https://github.com/user-attachments/assets/1f3d60c4-82ac-43c3-87d3-725ead8c0826)
JSON
![Screenshot 2024-09-17 213107](https://github.com/user-attachments/assets/9208e4d0-9a31-4b34-95da-a35f37991cb7)
XML ID
![Screenshot 2024-09-17 213456](https://github.com/user-attachments/assets/3d54175a-6d5e-4c5b-8046-6d90fc6ae02c)
JSON ID
![Screenshot 2024-09-17 213531](https://github.com/user-attachments/assets/66d8d2fa-bc1a-4f8b-92d2-ee49383e4933)





## Tugas 2 PBP 2024/2025

### Membuat Sebuah Projek Django Baru
Membuat project django baru pastikan sudah terinstall django dan python lalu check version. Setelah itu membuat direktori dengan nama "E-commerce" pilihan.

### Membuat aplikasi dengan nama main
Setelah membuat project django, selanjutnya menjalankan "python manage.py startapp main" untuk membuat direktori main

### Membuat aplikasi dengan nama main
Dalam file urls.py berisi request sehingga pada project main dapat terhubung

### Membuat model
Dalam membuat model membuat atribut Name,Price,Description yang mana models ini akan menyimpan ke dalam database nantinya

### Membuat fungsi views.py
Pada views.py berisi fungsi untuk menampilkan objek di html dari fungsi yang sudah dipanggil pada file html

### Membuat rooting Pada urls.py
Pada aplikasi main tambahkan urls.py untuk membuat jalan kepada view.py sehingga dapat mengakses file tersebut.

### Alur django

![Blank board](https://github.com/user-attachments/assets/37e77fa4-34d4-410c-829a-f92bf2d5fb65)

### Fungsi Git
Git adalah sistem kontrol versi (version control system) yang digunakan untuk melacak perubahan dalam kode atau file, memungkinkan banyak orang untuk bekerja bersama dalam sebuah proyek tanpa saling menimpa pekerjaan satu sama lain. 

### Alasan mengapa django menjadi framework untuk dijadikan permulaan
Django sering digunakan sebagai framework pengenalan karena mendukung pengembangan cepat (rapid development) dan menerapkan praktik terbaik, seperti arsitektur Model-View-Template (MVT). Kesederhanaannya membantu pemula memahami konsep dasar, seperti routing, templating, dan manajemen database, tanpa terbebani oleh kode yang kompleks. Selain itu, Django juga memiliki kominitas yang besar memudahkan pemula untuk menemukan sumber belajar dan solusi saat menghadapi kendal

### Mengapa model pada Django disebut ORM (Object-Relational Mapping)?
Model dalam Django disebut ORM (Object-Relational Mapping) karena berfungsi sebagai perantara antara database relasional dan objek Python. ORM memungkinkan pengembang untuk bekerja dengan data dari database menggunakan objek Python alih-alih menulis query SQL secara langsung. Berikut alasan mengapa model Django disebut ORM:




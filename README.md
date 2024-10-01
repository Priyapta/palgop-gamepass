# PalgopGamepass 🏪

## Link Deployment -> [PalgopGamepass](http://priyapta-naufal-palgopgamepass.pbp.cs.ui.ac.id/)

## Tugas 5 PBP 2024/2025

### Urutan Prioritas CSS Selector
1. Inline Styles (misalnya style="color: red;") memiliki prioritas tertinggi.
2. ID Selector (misalnya #header) 
3. Class Selector (misalnya .navbar :hover) 
4. Tag Selector (misalnya h1, p , div) 
5. Important Rule (!important) untuk override styling sebelumnya.

### Mengapa Responsive Design Penting?
Responsive Design merupakan design yang dapat berubah sesuai dengan pemakaian perangkat pastinya tampilan web dari desktop dan mobile berbeda karena space dari web itu sendiri. Penggunaan responsive design ini tentu sangat penting dalam pengembangan web.

Keuntungan Responsive Design
- Pengalaman Pengguna lebih baik
- Cakupan perangkat lebih luas
- Pengelolaan lebih efisien (tidak perlu membuat terpisah versi desktop dan mobile)

contoh responsive :
Desktop 
![image](https://github.com/user-attachments/assets/1cebb33e-301f-4964-85fd-f6ca7a19448f)
<br>
Mobile
<br>
![image](https://github.com/user-attachments/assets/d9b8ee27-ebf6-4644-a31a-17880f854a0c)
<br>

### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
1. Margin: Ruang di luar elemen, antara elemen dengan elemen lainnya.
2. Border: Garis yang membungkus elemen, terletak di antara margin dan padding.
3. Padding: Ruang di dalam elemen, antara konten dan border.
Contoh
![image](https://github.com/user-attachments/assets/76c5772b-3d66-4042-99dd-bf05421fcf5d)

### Konsep Flexbox dan Grid Layout
**Flexbox** dirancang untuk tata letak satu dimensi (baris atau kolom), yang memungkinkan elemen di dalam sebuah container untuk disusun dan didistribusikan secara fleksibel, baik dalam arah horizontal maupun vertikal.
**CSS Grid Layout** dirancang untuk tata letak dua dimensi (baris dan kolom). Ini memungkinkan untuk membuat tata letak yang lebih kompleks, seperti membagi halaman web menjadi beberapa area yang ditata dengan lebih terstruktur.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Melakukan kustomisasi pada halaman login, register, dan main
Untuk melakukan kusotmisasi, kita dapat menambahkan beberapa style pada bagian-bagian yang ingin dikustomisasi. Seperti pada study-tracker ini, saya sudah mengkustomisasi daftar item menjadi menggunakan card, mengkustomisasi tombol, mengatur posisi teks, dan mengatur warna latar belakang website.

Menambahkan Fitur Update dan Delete untuk Masing-Masing Item
Di berkas views.py pada folder main, tambahkan fungsi delete dan update.
```javascript
def delete_product(request, id):
   progress = Progress.objects.get(pk = id)
   progress.delete()
   return HttpResponseRedirect(reverse('main:show_main'))
```

```javascript
 def edit_product(request, id):
 progress = Progress.objects.get(pk = id)
 form = ProgressForm(request.POST or None, instance=progress)

 if form.is_valid() and request.method == "POST":
     form.save()
     return HttpResponseRedirect(reverse('main:show_main'))

 context = {'form': form}
 return render(request, "edit_progress.html", context)
```

Di folder yang sama, buka berkas urls.py, lalu import fungsi delete dan edit.
```python
from main.views import delete_product, edit_product
```
Masih di berkas yang sama, tambahkan path berikut pada urlpatterns
```javascript
path('edit-product/<int:id>', edit_progress, name='edit_product'),
path('delete/<int:id>', delete_product, name='delete_product'),
```





## Tugas 4 PBP 2024/2025

### Apa perbedaan antara HttpResponseRedirect() dan redirect()
Perbedaannya yaitu pada argumen pertamanya. redirect() lebih fleksibel dibandingkan dengan HttpResponseRedirect() yang hanya bisa diisi oleh url, sedangkan argumen pertama redirect() dapat diisi oleh model, view, atau url.

### Jelaskan cara kerja penghubungan model Product dengan User
Model Product biasanya dihubungkan dengan model User menggunakan ForeignKey. 
```user = models.ForeignKey(User, on_delete=models.CASCADE)```
argumen pertama berfungsi untuk mengarahkan ke User. argumen kedua berfungsi untuk memberi kondisi jika pengguna dihapus, semua produk yang terkait dengan pengguna tersebut juga akan dihapus.

### Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
- Authentication (Otentikasi)
  -> Memverifikasi identitas pengguna, contohnya login. Authorization, Memeriksa apa saja yang boleh dilakukan pengguna, contohnya admin dapat melakukan suntingan sedangkan pengguna biasa tidak.<br>
Proses:
1. Pengguna memasukkan kredensial (username/password).
2. Sistem memeriksa apakah kredensial tersebut cocok dengan yang ada di basis data.
3. Jika cocok, sistem mengesahkan bahwa pengguna tersebut benar.
- Authorization (Otorisasi)
 -> adalah proses memverifikasi apakah pengguna yang sudah terotentikasi memiliki izin untuk mengakses sumber daya tertentu atau melakukan tindakan tertentu. Ini mengontrol apa      yang dapat dan tidak dapat dilakukan oleh pengguna.
Contoh: Setelah pengguna berhasil login (authenticated), sistem memeriksa apakah pengguna tersebut memiliki izin (authorization) untuk mengakses halaman admin atau mengedit produk.<br>
Proses:
1. Setelah pengguna berhasil login, sistem memeriksa peran atau izin pengguna.
2. Sistem menentukan tindakan apa yang diizinkan untuk pengguna tersebut berdasarkan otorisasinya.

Proses Saat Pengguna Login:
- Authentication (Otentikasi)
1. User melakukan submisi form kredensialnya, biasanya username dan password.
2. View melakukan autentikasi dengan fungsi authenticate() yang akan mengecek submisi form pengguna pada database.
3. Jika sesuai, maka Django akan membuat sesi untuk pengguna tersebut.

- Authorization (Otorisasi) terjadi setelah pengguna berhasil login (authenticated).
1. Django menggunakan middleware untuk mengelola autentikasi dan otorisasi.
2. Django menyimpan pengguna yang telah diotentikasi di objek request sebagai request.user

### Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login dengan menggunakan cookies dan session. Cookies dan session dapat membuat http yang stateless memiliki holding state. Django tidak menyimpan informasi secara langsung pada cookies dengan alasan keamanan. Cookies pada django hanya menyimpan rangkaian token (sessionid) yang akan dipetakan ke database server dan penggunaan cookies menggunakan memory cache dari browser sehingga tidak memerlukan memory yang besar. 

Ciri-ciri cookies yang tidak aman adalah tidak menggunakan tokenizer. Dengan kata lain, informasi langsung disimpan pada cookies.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Buat fungsi register dengan memanfaatkan `UserCreationForm` yang sudah disediakan oleh django. Dalam `views.py`, buat fungsi register yang meminta input yakni username dan password dalam bentuk form:
```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully registered!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
Lalu sambungkan dengan sebuah `.html` file sebagai templates atau tampilan kepada user. Jangan lupa untuk menambahkan url `/register` ke dalam `urls.py`:
```python
from main.views imoport register
urlpatterns = [
    ...
    path('register/', register, name='register'),
    ...
```

### Buat page untuk login User
dalam `views.py` import terlebih dahulu fungsi `AuthenticationForm` agar dapat menyocokkan data yang di-input dengan yang ada di database dan juga fungsi `login` dari library Django. Lalu buat fungsi `login_user` untuk dapat menerima dan menyocokkan data:
```python
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)

    context = {'form': form}
    return render(request, 'login.html', context)
```
Sambungkan dengan file `.html` baru bernama `login.html` agar page login memiliki visual. Terakhir jangan lupa untuk import fungsi `login_user` ke `urls.py` agar dapat diakses via url yang dikehendaki

### Fungsi Logout
Import fungsi logout dari library Django dan buat fungsi logout di `views.py`:
```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
Tambahkan url untuk logout ke `urls.py` sehingga dapat diakses dengan menjalankan fungsi `logout_user` di `views.py`, jangan lupa import fungsi tersebut dari `views.py`. Selanjutnya dalam `main.html`, sertakan sebuah button yang ketike ditekan akan menuju ke url yang sudah ditetapkan.

### Menghubungkan User dengan Model (Product)
Buat foreign key untuk user pada `models.py` agar dapat menghubungkan suatu produk dengan suatu User:
```python
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
...
```
Setiap User menambahkan item atau product pada akunnya, simpan informasi tersebut ke User yang berkaitan dengan mwngubah fungsi `create_product` yang terdapat pada `views.py`. Lalu, pada fungsi `show_main`, akan menampilkan product pada user itu saja. Lalu, laukan migrasi.

### Membuat informasi last login 
Untuk membuat sebuah informasi last login, kita harus dapat menangkap waktu ketika user login. Maka dari itu, dibutuhkan import `time` dan juga `HttpResponsRedirect`. Setelah itu, set sebuah catatan ketika user log in dengan menambahkan hal berikut pada login_user:
```python
...
if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
...
```
Agar dapat dipakai dan ditampilkan ke `main.html`, informasi mengenai last login ini harus ditambahkan ke `context` di dalam fungsi `show_main`:
```python
def show_main(request):
...
context = {
...
'last_login': request.COOKIES['last_login'],
...
}
```

setelah menambahkan cookies, jangan lupa untuk menghapus informasi last login ini ketika user logout, lalu selanjutnya 

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
(https://github.com/user-attachments/assets/66d8d2fa-bc1a-4f8b-92d2-ee49383e4933)





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




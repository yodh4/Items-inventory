**1. Apa itu django user creation form, dan jelaskan kelebihan dan kekurangannya**

Django `UserCreationForm` adalah sebuah form yang disediakan oleh `Django authenthication framework` untuk menghandle pembuatan *user* baru. `UserCreationForm` memiliki tiga *field* yaitu `username` untuk *username* pengguna, `password1` untuk *password* akun pengguna, dan `password2` untuk *password confirmation* akun pengguna.

Django `UserCreationForm` memiliki beberapa kelebihan dan kekurangan.

**Kelebihan**: 
1. Mudah digunakan, `UserCreationForm` memiliki fitur yang sudah siap untuk diimplementasikan dan relatif mudah untuk digunakan
2. Memiliki fitur validasi, `UserCreationForm` akan secara otomatis memvalidasi apakah user memberikan input yang benar seperti pengecekan *username* yang unik, memastikan *password* yang kita masukkan sesuai dengan ketentuan dari Django `UserCreationForm`, dan memastikan *password* yang kita masukkan sesuai dengan *password* pertama yang kita masukkan
3. Bisa di-*customization*, kita bisa melakukan *customization* terhadap `UserCreationForm` seperti menambahkan *field email* dan melakukan validasi akun lewat *email* yang kita masukkan

**Kekurangan**:
1. Tampilan standar, `UserCreationForm` memiliki tampilan bawaan yang sangat standar, hal ini mungkin akan membuat website kita terlihat terlalu simpel dan tidak profesional. Jika kita ingin membuat tampilan *form* kita terlihat lebih menarik maka kita harus melakukan *customization* sendiri


**2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?**

Autentikasi adalah sebuah proses validasi/pembuktian terhadap identitas yang hendak memasuki sebuah sistem layanan. Autentikasi dilakukan agar kita dapat memastikan bahwa pengguna yang ingin masuk adalah pengguna dari akun tersebut dan bukan orang lain. 


Pada Django, sistem autentikasi berpusat pada objek `User`, objek ini merepresentasikan pengguna yang berinteraksi dengan *website* kita. Objek `User` memiliki beberapa atribut seperti `username`, `password`, `email`, `first_name`, dan `last_name`. Django menggunakan `authenticate()` untuk men-*verify* kredensial, `authenticate()` kredential ini berupa *keyword* parameter yaitu `usernamr` dan `password`. Selanjutnya `authenticate` akan mengecek terhadap `authentication backend`, jika kredensial yang diinput valid maka akan me-*return* objek `User`, jika kredensialnya tidak valid maka akan me-*return* `None`.


Otorisasi adalah proses mengontrol apa saja yang diizinkan oleh pengguna yang telah terautentifikasi, proses ini adalah proses selanjutnya dari autentikasi. Pada Django, otorisasi diatur oleh Django `admin`, beberapa otorisasi atau *permissions* yang ada adalah:
- Akses untuk *view* objek terbatas pada *user* dengan dengan *permission* `view` atau `change` untuk tipe objek tersebut
- Akses untuk *view* formulir `add` dan *add* sebuah objek terbatas pada *user* dengan *permission* `add` untuk tipe objek tersebut
- Akses untuk *view* list perubahan, *view* formulir `change`, dan mengubah sebuah objek terbatas pada *user* dengan *permission* `change` untuk tipe objek tersebut
- Akses untuk *delete* sebuah objek terbatas pada *user* dengan *permission* `delete` untuk tipe objek tersebut


Autentikasi dan otorisasi merupakan kedua hal yang sangat penting, dengan autentikasi kita dapat memastikan kemanan data yang berada di akun tersebut, memastikan pengguna yang mengakses suatu akun adalah pemilik akun tersebut, dan melakukan pemblokiran akun apabila kita merasa terdapat aktivitas yang mencurigakan pada akun tersebut. Selain autentikasi, otorisasi juga merupakan hal yang sangat penting karena otorisasi dapat membatasi aksesibilitas suatu *user* pada *website* kita, hal ini dapat mencegah kebocoran data atau perubahan data yang tidak kita inginkan.


**3.  Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?**

Cookies adalah file berukuran kecil yang disimpan di komputer *user* oleh *web server* ketika pengguna mengunjungi suatu *website*, *cookies* ini akan digunakan untuk menyimpan data tentang pengguna yang dapat digunakan kembali saat pengguna berinteraksi dengan *website* tersebut. 

Cara Django menggunakan *cookies* untuk mengelola data sesi pengguna adalah:
1. Saat pengguna mengakses suatu *website*, server dapat membuat suatu *session* untuk pengguna tersebut
2. Untuk mengidentifikasi *session* yang telah dibuat, server akan mengirim sebuah *ID* ke pengguna atau *client side* menggunakan *cookies*
3. Data dari *session* ini(seperti informasi autentikasi pengguna, preferensi pengguna, dll) akan disimpan oleh server dalam *session* yang sesuai
4. Server dapat menggunakan *ID* dari *cookies* untuk mengaitkan *request* dari *client* dengan *session* yang sesuai

Pada Django, kita dapat mengakses `attributes` dari suatu *sessions* menggunakan `HttpRequest` 


**4.  Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?**

*Cookies* disimpan pada sisi klien, yang berarti data yang disimpan dalam *cookies* dapat diakses dan dimodifikasi oleh pengguna atau pihak ketiga jika tidak dienkripsi atau diotentikasi dengan benar. Hal ini dapat menyebabkan bahaya jika terdapat informasi penting yang tersimpan pada *cookies* tersebut dan *cookies* kita diakses oleh orang lain. Oleh karena itu, pastikan untuk mengenkripsi *cookies* kita agar tidak dapat dibaca oleh pihak yang tidak berwenang


**5. Penjelasan step by step implementasi checklist**

1. Jalankan *virtual environment*
2. Membuat fungsi `register` pada `views.py` yang ada di subdirektori `main`
3. Membuat *file* `register.html` pada `main\templates`
4. Menambahkan *path url* ke `urlpatterns` untuk mengakses fungsi `register`
5. Membuat fungsi `login` 
6. Membuat *file* `login.html`
7. Menambahkan *path url* ke `urlpatterns` untuk mengakses fungsi `login`
8. Membuat fungsi `logout`
9. Menambahkan *button* untuk *logout* pada `main.html`
10. Menambahkan *path url* ke `urlpatterns` untuk mengakses fungsi `logout`
11. Merestriksi halaman `main` agar *user* perlu login terlebih dahulu untuk mengakses halaman `main`
12. Buat 2 akun baru 
13. Menambahkan kode `user = models.ForeignKey(User, on_delete=models.CASCADE)` pada model `Product` kita untuk menghubungkan suatu produk dengan seorang *user*
14. Memodifikasi fungsi `create_product` agar menghubungkan objek yang ditambahkan kepada *user* yang sedang *login*
15. Memodifikasi fungsi `show_main` agar menampilkan *username* akun yang sedang login dan menampilkan objek `Product` yang terasosiasi dengan akun tersebut
16. Melakukan migrasi model
17. Memodifikasi fungsi `login_user` dan `show_main` untuk menambahkan *cookie* `last_login` 
18. Memodifikasi fungsi `logout_user` agar menghapus *cookie* `last_login` saat *user* logout
19. Memodifikasi `main.html` agar dapat menampilkan kapan *user* terakhir *login*
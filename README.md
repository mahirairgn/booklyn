Link Adaptable: https://booklyn.adaptable.app/main/

# Tugas 4
### Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?
UserCreationForm adalah sebuah formulir bawaan yang disediakan oleh framework Django untuk memudahkan pembuatan formulir user baru dalam aplikasi web. Dengan adanya formulir ini, user dapat mendaftarkan dirinya di website tanpa harus menulis kode yang banyak dari awal. Namun, UserCreationForm juga memiliki keterbatasan dalam menyimpan input dari user (hanya nama, email, dan password) sehingga perlu dilakukan penambahan field lain secara terpisah jika membutuhkan kustomisasi.

### Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
- Autentikasi adalah proses verifikasi identitas user dari data yang di-input, misalnya berdasarkan username / email dengan passwordnya.
- Otorisasi adalah proses pengaturan akses dengan menentukan apa saja yang diizinkan dan tidak diizinkan oleh user dalam aplikasi.
Kedua hal ini sangat penting untuk meningkatkan keamanan aplikasi. Autentikasi membantu mencegah user yang tidak sah dalam mengakses aplikasi, kemudian otorisasi membantu memastikan bahwa user hanya bisa mengakses fitur dan informasi yang diizinkan.

### Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies adalah sebuah data kecil yang dikirim oleh server web ke browser web dan disimpan di perangkat user ketika terdapat interaksi dengan web. Cookies dapat digunakan untuk menyimpan informasi user seperti nama dan email. Selain itu, cookies juga berperan dalam pengelolaan data sesi user sehingga dapat mengenali user ketika masuk kembali ke web tersebut.
Pengelolaan tersebut dilakukan oleh Django dengan cara membuat cookie berisi ID sesi yang unik ketika user masuk. Kemudian Django akan memeriksa ID sesi dari cookie untuk mengidentifikasi user. Lalu jika user keluar dari aplikasi, Django akan menghapus data sesi karena sesinya telah berakhir.

### Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Pada umumnya, cookies relatif aman untuk digunakan secara default. Namun, user harus tetap waspada karena cookies dapat digunakan untuk mengekstrak informasi sensitif user sehingga dapat menimbulkan risiko seperti Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF), pelacakan dan pencurian data, hingga Cookie Sniffing.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Menambahkan import pada file `views.py` di `main`. Import tersebut adalah `redirect`, `UserCreationForm`, `messages`. `authenticate`, `login`, `logout`, `login_required`, `datetime`
2. Membuat fungsi baru bernama `register`, `login_user`, dan `logout_user` pada file tersebut, dengan isi kode sesuai pada github saya
3. Menambahkan button logout pada file `main.html`
4. Membuat berkas html baru bernama `register.html`, `login.html`. Lalu isi file tersebut dengan kode html sesuai kebutuhan
5. Mengimpor fungsi-fungsi yang baru dibuat pada poin 2 ke file `urls.py` dan menambahkan path url nya ke dalam bagian `urlpatterns`
6. Mengatur akses halaman main agar hanya bisa diakses oleh user yang sudah login dengan menambahkan kode di atas fungsi `show_main`
7. Menambahkan informasi cookie `last_login` ke bagian `context` pada `views.py` dan pada `main.html`
8. Mengimpor model pada `models.py` dan menambahkan kode untuk menghubungkan produk dengan seorang user
9. Melakukan migrasi model

--------------------------------------------------------------------------------------------------------------------------------------

# Tugas 3
### Apa perbedaan antara form POST dan form GET dalam Django?
POST dan GET adalah metode pada HTTP yang berperan untuk mengirim data browser ke server. Perbedaan utama dari keduanya terletak pada cara mentransfer data dari user ke server.
##### POST
- Mengirim data dalam bentuk tubuh pesan HTTP
- Tidak menampilkan data di URL karena dikirim secara terenkripsi
- Relatif lebih aman
- Biasanya digunakan pada sistem login
##### GET
- Mengirim data sebagai bagian dari URL
- Menampilkan data di URL dan dapat dibaca secara publik
- Kurang aman jika dibandingkan dengan GET
- Biasanya digunakan pada sistem pencarian

### Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
Ketiganya adalah format data yang digunakan dalam proses pengiriman data antaraplikasi. Perbedaannya adalah:
##### XML
- Berbasis tag
- Menyimpan dan mengirim data yang terstruktur
- Tingkat kompleksitasnya tinggi karena memiliki struktur yang lebih rumit
- Digunakan pada dokumen, API, dan konfigurasi
##### JSON
- Berbasis objek
- Pertukaran data sederhana yang mirip dengan struktur data pada bahasa pemrograman, serta bersifat hierarkis
- Tingkat kompleksitasnya rendah karena memiliki format yang sederhana
- Digunakan pada data dan API
##### HTML
- Berbasis tag
- Berkaitan dengan data yang dapat dibaca manusia dan halaman web
- Tingkat kompleksitasnya rendah
- Digunakan pada dokumen web

### Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
Karena JSON memiliki format yang ringan, sederhana, dan kompatibel sehingga lebih ringan dan efisien untuk ditransfer melalui jaringan. Selain itu, JSON juga dapat digunakan di berbagai aplikasi karena didukung oleh berbagai bahasa pemrograman dan platform

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
1. Mengaktifkan virtual environment
2. Menghilangkan path `main/` pada bagian `urlpatterns` di file `urls.py` pada subdirektori `booklyn`
3. Membuat file bernama `base.html` pada subdirektori `templates`
4. Menyesuaikan kode di `settings.py` pada subdirektori `booklyn` agar file `base.html` dapat terdeteksi sebagai template
5. Mengubah kode pada file `main.html` di subdirektori `templates`
6. Membuat file baru bernama `forms.py` pada direktori `main` untuk menerima data produk baru
7. Menambahkan import `HttpResponseRedirect`, `ItemForm`,`reverse`, `HttpResponse`, dan `Serializer` pada file `views.py` di subdirektori `main` dan membuat fungsi baru bernama `create_item`
8. Menyesuaikan isi dari fungsi `show_main` serta membuat fungsi baru bernama `show_xml`, `show_json`, `show_xml_by_id`, dan `show_jsin_by_id` pada file `views.py`
9. Mengimport fungsi `create_item`, `show_xml`, `show_json`, `show_xml_by_id` dan `show_json_by_id` di file `urls.py` pada subdirektori `main` kemudian menambahkan path url baru ke bagian `urlpatterns`
10. Membuat file baru bernama `create_product.html` pada direktori `main/templates`

### Hasil screenshot Postman
**HTML**
<img src='/images/Tugas3_Postman_HTML.png'>

**XML**
<img src='/images/Tugas3_Postman_XML.png'>

**JSON**
<img src='/images/Tugas3_Postman_JSON.png'>

**XML by ID**
<img src='/images/Tugas3_Postman_XMLbyID.png'>

**JSON by ID**
<img src='/images/Tugas3_Postman_JSONbyID.png'>

--------------------------------------------------------------------------------------------------------------------------------------

# Tugas 2

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step!
1. Membuat repositori github bernama `booklyn`
2. Membuat direktori utama bernama `booklyn` dan menginisiasikannya sebagai repositori git
3. Menambahkan berkas `.gitignore`
4. Melakukan deployment aplikasi pada adaptable
5. Membuat virtual environment pada direktori utama dan mengaktifkannya
6. Membuat file bernama `requirements.txt` yang berisi beberapa dependencies kemudian memasang
7. Membuat proyek Django bernama `booklyn`
8. Menambahkan tanda `*` pada bagian `ALLOWED_HOST` di `settings.py` untuk mengizinkan akses dari semua host
9. Membuat aplikasi baru bernama `main` pada direktori proyek `booklyn`
10. Mendaftarkan aplikasi main ke proyek dengan menambahkan `main` pada bagian `INSTALLED_APPS` di `settings.py` pada direktori proyek
11. Membuat direktori baru bernama `templates` dalam direktori aplikasi `main`
12. Membuat file bernama `main.html` dan isi file tersebut sesuai keinginan
13. Mengisi file `models.py` dengan nama model `Product` dan field `name`, `amount`, `description`
14. Membuat dan menerapkan migrasi model
15. Mengimport modul pada file `views.py`, kemudian membuat fungsi `show_main` yang berisi data dari field pada model
16. Membuat file bernama `urls.py` pada direktori `main` lalu import fungsi yang diperlukan dan berikan nama unik yang akan digunakan pada URL
17. Membuka file `urls.py` yang ada di direktori proyek `booklyn` lalu import fungsi yang diperlukan dan tambahkan rute URL dalam bagian `urlpatterns`
18. Menonaktifkan virtual environment
19. Melakukan `add`, `commit`, dan `push` untuk memperbarui github

### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
<img src='/images/Tugas2_No2_Bagan.jpg'>

### Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Karena suatu project membutuhkan dependencies yang berbeda-beda dalam suatu OS sehingga memerlukan virtual environment untuk menjalankannya agar tidak perlu mengubah configurations pada OS. Dalam membuat aplikasi web berbasis Django, kita bisa melakukannya tanpa menggunakan virtual environment tetapi tidak disarankan karena akan lebih sulit untuk mengelola dependencies dan mengisolasi projectnya.

### Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
Baik MVC, MVT, maupun MVVM adalah pola desain arsitektur dalam sistem pengembangan website. Ketiga pola tersebut terdiri dari komponen Model (mewakili data dan logic) dan View(berkaitan dengan interface pengguna). Namun, masing-masing pola memiliki perbedaan pendekatan, yaitu:
- MVC (Model-View-Controller) -> Memiliki komponen Controller yang bertanggungjawab menghubungkan Model dan View, serta mengatur alur kerja dan mengendalikan interaksi pengguna
- MVT (Model-View-Template) -> Merupakan turunan dari MVC. Memiliki komponen Template yang berperan untuk memisahkan View dari Controller. Template akan berisi file HTML dengan kode yang bisa diisi oleh Model
- MVVM (Model-View-ViewModel) -> Memiliki komponen ViewModel yang menghubungkan model dan view, serta bertanggung jawab untuk mengkonversi data dari Model agar sesuai dengan kebutuhan tampilan dan mengatur interaksi pengguna
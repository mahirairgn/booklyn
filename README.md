Link Adaptable: https://booklyn.adaptable.app/main/

# Tugas 6
### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming
- Asynchronous Programming bersifat *multi-thread* sehingga dapat mengeksekusi tugas secara paralel atau bersamaan. Sedangkan, Synchronous Programming bersifat *single-thread* sehingga hanya bisa mengeksekusi satu tugas dalam satu waktu.
- Asynchronous Programming bersifat *non-blocking* sehingga dapat melanjutkan eksekusi tugas lain tanpa harus menunggu suatu tugas selesai dieksekusi. Sedangkan, Synchronous Programming bersifat *blocking* sehingga eksekusi suatu tugas bergantung pada penyelesaian tugas sebelumnya. Jika belum selesai, maka suatu tugas tidak bisa dieksekusi.
- Asynchronous Programming umumnya lebih cepat karena bisa menjalankan beberapa tugas sekaligus. Sedangkan, Synchronous Programming cenderung lebih lambat.

### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Paradigma event-driven programming adalah sebuah 

### Jelaskan penerapan asynchronous programming pada AJAX
Dengan menerapkan asynchoronous programming, AJAX dapat mengambil dan mengirim data dari/ke server web tanpa harus melakukan *refresh* pada halaman web tersebut sehingga aplikasi web tetap responsif saat melakukan *request* ke server. Contoh penerapan:
1. Aplikasi web pencarian yang menampilkan hasil pencarian secara *real-time* saat user sedang mengetik
2. Dalam sistem voting atau rating, halaman web akan memperbarui hasil perhitungannya tanpa mengubah tampilan atau *reload halaman*
3. Fitur chat di suatu web tidak akan tertutup ketika kita membuka halaman lain dalam web tersebut

### Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.


### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

--------------------------------------------------------------------------------------------------------------------------------------

# Tugas 5
### Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya
- `*` digunakan untuk memilih semua elemen pada halaman HTML. Biasanya digunakan kertika perlu melakukan sesuatu kepada seluruh elemen di web, misalnya saat mengatur default elemen
- `element` digunakan untuk memilih semua elemen pada bagian yang disebutkan. Sebaiknya digunakan saat harus melakukan sesuatu pada bagian tertentu saja, misalnya `p` ketika akan memilih semua elemen paragraf (`<p>`). Dapat digunakan dengan combinator agar terhubung dengan `element` lain.
-  `[attribute]` **dan sebagainya**, digunakan untuk memilih elemen pada attribute yang ditentukan. Selain itu, kita dapat menyespesifikkan elemen yang akan dipilih melalui perintah tambahan. Sebaiknya digunakan ketika kita perlu melakukan sesuatu pada suatu atribut yang spesifik. Misalnya `[title~="flower"]` hanya akan memilih elemen dengan atribut title yang memiliki kata "flower" di dalamnya

### Jelaskan HTML5 Tag yang kamu ketahui
1. `<a>` untuk membuat hyperlink ke web lain, dokumen, dan sumber lainnya
2. `<body>` untuk mendefinisikan body dokumen, isinya adalah konten-konten yang akan ditampilkan 
3. `<br>` untuk membuat break sebanyak 1 baris dalam teks
4. `<button>` untuk membuat tombol yang bisa di-click oleh user
5. `<embed>` untuk embed aplikasi lain (biasanya audio atau video) ke dokumen
6. `<h1> to <h6>` untuk menunjukkan headings dalam web, dimana `<h1>` memiliki ukuran paling besar dan `<h6>` yang paling kecil
7. `<img>` untuk menampilkan gambar
8. `<p>` untuk menunjukkan paragraf
9. `<table>` untuk membuat tabel

### Jelaskan perbedaan antara margin dan padding
- **Margin** adalah space di luar elemen dengan elemen lain di sekitarnya. Contoh penggunaannya adalah ketika ingin mengatur jarak dari elemen yang terpisah atau saat ingin membuat suatu elemen sejajar dengan elemen lainnya
- **Padding** adalah space antara elemen dengan content di dalamnya. Contoh penggunaannya adalah ketika ingin menambahkan space kosong di sekitar konten.

### Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
- **Tailwind** membuat tampilan menggabungkan kelas-kelas utilitas yang sebelumnya sudah didefinisikan sehingga ukuran file CSS nya lebih kecil daripada Bootstrap. Selain itu, tailwind juga lebih fleksibel dan mudah diadaptasikan terhadap proyek. Sebaiknya Tailwind digunakan pada proyek yang memerlukan fleksibilitas karena lebih mudah untuk dikustomisasi.
- **Bootstrap** membuat tampilan dari gaya dan komponen yang sudah jadi dan memiliki tampilan sehingga bisa langsung digunakan. Hal ini membuat file CSS nya lebih besar. Tampilan pada bootstrap cenderung konsisten. Sebaiknya Bootstrap digunakan untuk proyek yang tidak membutuhkan banyak perubahan tampilan dan oleh pemula karena lebih mudah dipelajari.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
1. Menambahkan Bootstrap CSS dan JS serta script JS pada file `base.html`
2. Menmbuat fitur edit dan delete produk pada aplikasi dengan menambahkan fungsi baru pada `views.py` lalu diimport ke `urls.py` dan menambahkan path urlnya ke dalam `urlpatterns`
3. Mengubah kode pada `main.html` untuk menampilkan fitur baru tersebut
4. Menambahkan bagian `<style>` pada file-file di folder `templates` untuk mengatur tampilan dari masing-masing halaman menggunakan CSS

--------------------------------------------------------------------------------------------------------------------------------------

# Tugas 4
### Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?
UserCreationForm adalah sebuah formulir bawaan yang disediakan oleh framework Django untuk memudahkan pembuatan formulir user baru dalam aplikasi web. Dengan adanya formulir ini, user dapat mendaftarkan dirinya di website tanpa harus menulis kode yang banyak dari awal. Namun, UserCreationForm juga memiliki keterbatasan dalam menyimpan input dari user (hanya nama, email, dan password) sehingga perlu dilakukan penambahan field lain secara terpisah jika membutuhkan kustomisasi.

### Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
- **Autentikasi** adalah proses verifikasi identitas user dari data yang di-input, misalnya berdasarkan username / email dengan passwordnya.
- **Otorisasi** adalah proses pengaturan akses dengan menentukan apa saja yang diizinkan dan tidak diizinkan oleh user dalam aplikasi.
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
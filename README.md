Link Adaptable: https://booklyn.adaptable.app/main/

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
<img src='/Tugas2_No2_Bagan.jpg'>

### Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Karena suatu project membutuhkan dependencies yang berbeda-beda dalam suatu OS sehingga memerlukan virtual environment untuk menjalankannya agar tidak perlu mengubah configurations pada OS. Dalam membuat aplikasi web berbasis Django, kita bisa melakukannya tanpa menggunakan virtual environment tetapi tidak disarankan karena akan lebih sulit untuk mengelola dependencies dan mengisolasi projectnya.

### Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
Baik MVC, MVT, maupun MVVM adalah pola desain arsitektur dalam sistem pengembangan website. Ketiga pola tersebut terdiri dari komponen Model (mewakili data dan logic) dan View(berkaitan dengan interface pengguna). Namun, masing-masing pola memiliki perbedaan pendekatan, yaitu:
- MVC (Model-View-Controller) -> Memiliki komponen Controller yang bertanggungjawab menghubungkan Model dan View, serta mengatur alur kerja dan mengendalikan interaksi pengguna
- MVT (Model-View-Template) -> Merupakan turunan dari MVC. Memiliki komponen Template yang berperan untuk memisahkan View dari Controller. Template akan berisi file HTML dengan kode yang bisa diisi oleh Model
- MVVM (Model-View-ViewModel) -> Memiliki komponen ViewModel yang menghubungkan model dan view, serta bertanggung jawab untuk mengkonversi data dari Model agar sesuai dengan kebutuhan tampilan dan mengatur interaksi pengguna
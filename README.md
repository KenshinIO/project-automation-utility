🚀 Project Automation & File Manager (PAFM)

PAFM adalah utilitas Python serbaguna yang dirancang untuk membantu pengembang dan programmer dalam mengelola tugas berulang dan operasi sistem berkas. Ini menyediakan antarmuka terstruktur untuk otomatisasi proyek dasar.

✨ Fitur Utama

Manajemen Direktori: Membuat struktur direktori yang kompleks dengan mudah.

Pembuatan Berkas Dummy: Membuat berkas dengan konten kustom untuk pengujian atau inisialisasi.

Pembersihan Berkas Lanjut: Menghapus berkas lama secara otomatis berdasarkan usia di hari (berguna untuk membersihkan cache/log).

Penjadwal Tugas Modular: Menambahkan dan menjalankan tugas yang ditentukan (fungsi Python) dalam struktur yang terkontrol.

Pencatatan Berstempel Waktu (Timestamped Logging): Semua output dicatat dengan stempel waktu untuk pelacakan yang akurat.

🛠️ Instalasi dan Penggunaan

Proyek ini hanya membutuhkan Python standar.

Kloning Repositori:

git clone [URL-REPOSITORI-ANDA]
cd [NAMA-FOLDER-REPOSITORI]


Jalankan Skrip:

python automation_tool.py


🏗️ Struktur Proyek

Berkas

Deskripsi

automation_tool.py

Berkas Python utama berisi kelas FileManager dan TaskScheduler.

README.md

Dokumen ini.

proyek_logs/

(Dibuat saat dijalankan) Direktori untuk berkas log.

proyek_cache/

(Dibuat saat dijalankan) Direktori untuk berkas sementara/cache.
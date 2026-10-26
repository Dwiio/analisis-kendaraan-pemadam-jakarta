# Optimalisasi Alokasi dan Analisis Kondisi Armada Operasional Damkar DKI Jakarta

Proyek Data Science — Program Studi Informatika, Fakultas Teknik Industri, Universitas Pembangunan Nasional “Veteran” Yogyakarta.

##  Nomor Kelompok : 50
##  Nama Kelompok : Next Level
##  Anggota Kelompok :

- Dwirizki Adithya Putra — 123240021
- Satya Dio Putranto — 123240121
- Sebastian Alvaro Huller — 123240162
- Paksi Dwirangga — 123240172

## Ringkasan

Proyek ini menganalisis inventaris kendaraan operasional penanggulangan kebakaran dan penyelamatan DKI Jakarta pada periode data 2025. Fokus proyek ini adalah **Business Understanding** dan **Data Understanding**: audit kualitas, eksplorasi kondisi aset, analisis kategori, dan penilaian kelayakan awal untuk pemodelan lanjutan.

**Penting:** kolom `Kondisi` (BAIK/RUSAK) adalah label kondisi yang tercatat, bukan pengukuran kesiapan operasional aktual atau kesiapan real-time. Dataset tidak memuat koordinat, waktu respons, riwayat perawatan, ketersediaan kru, atau beban kejadian. Karena itu, proyek ini tidak mengklaim telah mengoptimalkan alokasi armada secara operasional dan tidak menyebut klaster administratif sebagai klaster geografis berbasis jarak.

## Temuan awal dari berkas yang diberikan

- Ukuran data sumber: **1.153 baris × 10 kolom**.
- Periode pada semua baris: **2025**.
- Label kondisi: **984 BAIK (85,34%)** dan **169 RUSAK (14,66%)**.
- Terdapat **5 nilai kosong** pada `plat_nomor`; kolom ini dikeluarkan dari dataset portofolio yang disertakan.
- Tidak ditemukan baris duplikat identik pada pemeriksaan awal.
- Dataset sanitasi dalam repositori berisi 9 kolom, tanpa `plat_nomor`, untuk mengurangi paparan identifier aset.

Angka tersebut merujuk pada file komponen data yang disediakan bersama tugas. Jalankan notebook untuk memverifikasi hasil pada salinan data yang disertakan.

## Struktur repositori

```text
uts-data-science-armada/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/                 
│   └── processed/
│       └── kendaraan_2025_sanitized.csv
├── notebooks/
│   ├── 01_business_data_understanding.ipynb
│   ├── 02_preparation_baseline_model.ipynb
│   └── 03_clustering_profil_administratif.ipynb
├── Laporan/
│   └── Laporan_UTS_DataScience.md
└── src/
    └── data_utils.py
```

## Menjalankan di Mac/Linux/Windows

Disarankan Python 3.10–3.12. Dari direktori proyek:

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter lab
```

Buka notebook di folder `notebooks/` dan jalankan dari sel pertama sampai terakhir. Notebook menggunakan path relatif dan dataset sanitasi yang sudah disertakan.

## Alur analisis

1. `01_business_data_understanding.ipynb`: ringkasan data, missing values, duplikasi, distribusi kondisi, profil per wilayah/jenis kendaraan, dan asosiasi kategorikal eksploratif.
2. `02_preparation_baseline_model.ipynb`: split stratifikasi, pipeline encoding, baseline DummyClassifier dan model kandidat; metrik macro-F1, balanced accuracy, recall kelas RUSAK, serta confusion matrix.
3. `03_clustering_profil_administratif.ipynb`: clustering profil agregat wilayah. Karena koordinat tidak tersedia, ini **bukan** klasterisasi spasial berbasis jarak geografis.

Model di notebook 02 adalah demonstrasi akademik awal, bukan sistem keputusan yang siap dipakai. Performa dapat berubah pada validasi lain; jangan menafsirkan prediksi sebagai pengganti inspeksi teknis.

## Data, privasi, dan lisensi

Sumber: [Satu Data Jakarta — Data Kendaraan Operasional Penanggulangan Kebakaran dan Penyelamatan](https://satudata.jakarta.go.id/open-data/detail?kategori=dataset&page_url=data-kendaraan-operasional-penanggulangan-kebakaran-dan-penyelamatan&data_no=1).

File sumber yang diperiksa berformat ekstensi `.xls`, tetapi terbaca sebagai tabel HTML oleh `pandas.read_html`. File sumber mentah tidak disertakan dalam repositori ini karena memuat identifier `plat_nomor`. Dataset sanitasi yang disertakan menghapus kolom tersebut.

**Jangan mengasumsikan lisensi CC0.** Sebelum publikasi, periksa metadata dan ketentuan penggunaan spesifik dataset di portal. Catat tanggal akses dan versi sumber. Bila lisensi atau ketentuan redistribusi tidak jelas, tautkan sumber resmi dan distribusikan hanya kode serta ringkasan yang diizinkan.

## Batasan utama

- Snapshot satu periode (2025), bukan data longitudinal.
- Label `Kondisi` tidak memiliki definisi inspeksi/waktu pencatatan pada file.
- Kategori administratif tidak sama dengan koordinat geografis.
- Proporsi pada kelompok kecil memiliki ketidakpastian tinggi; tampilkan jumlah dan persentase.
- `plat_nomor` tidak digunakan sebagai fitur model.
- Asosiasi bukan kausalitas; model tidak membuktikan penyebab kerusakan atau kecukupan alokasi.

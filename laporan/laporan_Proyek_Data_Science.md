# Dokumentasi Proyek Data Science

## 1. Halaman Judul

**DOKUMENTASI PROYEK DATA SCIENCE**

**OPTIMALISASI ALOKASI DAN PREDIKSI KESIAPAN ARMADA KENDARAAN OPERASIONAL PENANGGULANGAN KEBAKARAN DAN PENYELAMATAN DI DKI JAKARTA BERBASIS KLASIFIKASI KONDISI ASET DAN KLASTERISASI SPASIAL**

Disusun oleh:

1. Dwirizki Adithya Putra — 123240021
2. Satya Dio Putranto — 123240121
3. Sebastian Alvaro Huller — 123240162
4. Paksi Dwirangga — 123240172

Dosen Pengampu: Dhimas Arief Dharmawan

PROGRAM STUDI INFORMATIKA  
JURUSAN INFORMATIKA  
FAKULTAS TEKNIK INDUSTRI  
UNIVERSITAS PEMBANGUNAN NASIONAL “VETERAN” YOGYAKARTA  
2026

> Tata letak akhir (logo, spasi, margin, dan tipografi) perlu disesuaikan dengan pedoman sampul resmi atau template yang diberikan dosen.

## 2. Business Understanding

### 2.1 Latar Belakang

Ketersediaan kendaraan operasional yang terawat dan ditempatkan secara proporsional merupakan salah satu unsur pendukung layanan penanggulangan kebakaran dan penyelamatan. Inventaris yang memuat kondisi aset serta lokasi administratif dapat digunakan untuk memetakan komposisi armada, mengidentifikasi pola pencatatan yang perlu diverifikasi, dan merumuskan prioritas pemeriksaan aset. Namun, inventaris tidak secara langsung menggambarkan kesiapan operasional aktual. Kesiapan juga dipengaruhi oleh status aktif, ketersediaan kru, bahan bakar, kelengkapan peralatan, riwayat perawatan, dan kondisi kendaraan pada waktu kejadian.

Proyek ini menggunakan dataset **Data Kendaraan Operasional Penanggulangan Kebakaran dan Penyelamatan** dari portal Satu Data Jakarta. Berkas yang dianalisis memuat 1.153 baris dan 10 kolom dengan periode data 2025. Proyek ini difokuskan pada pemahaman kebutuhan bisnis dan karakteristik data sesuai kerangka CRISP-DM. Oleh karena itu, hasil yang disajikan merupakan analisis inventaris dan rancangan evaluasi, bukan klaim penerapan sistem operasional.

### 2.2 Pernyataan Masalah

Bagaimana data inventaris kendaraan periode 2025 dapat dimanfaatkan untuk (1) menggambarkan proporsi kondisi BAIK dan RUSAK secara keseluruhan dan menurut wilayah maupun jenis kendaraan; (2) menilai kelayakan fitur yang tersedia untuk mengklasifikasikan label kondisi tercatat secara terukur; dan (3) mengeksplorasi kemiripan profil komposisi armada antarunit administratif sebagai masukan awal bagi evaluasi alokasi?

Istilah “prediksi kesiapan” pada judul dibatasi secara metodologis. Variabel target yang tersedia adalah `Kondisi` dengan label BAIK/RUSAK. Label ini tidak membuktikan apakah kendaraan siap beroperasi pada saat tertentu. Jika model dikembangkan, targetnya adalah **klasifikasi kondisi yang tercatat**, bukan prediksi kesiapan operasional real-time.

### 2.3 Tujuan SMART

- **Specific:** memetakan kondisi aset dan distribusi inventaris menurut wilayah administratif, jenis kendaraan, klasifikasi, fungsi, dan penempatan.
- **Measurable:** menghasilkan audit dimensi, missing value, duplikasi, kategori unik, distribusi kelas, proporsi RUSAK per kelompok, dan asosiasi kategorikal. Jika pemodelan dilakukan, laporkan macro-F1, balanced accuracy, precision/recall kelas RUSAK, dan confusion matrix.
- **Achievable:** menggunakan dataset terbuka yang diberikan, Python, pandas, scikit-learn, dan Jupyter Notebook dengan pipeline yang dapat dijalankan ulang.
- **Relevant:** menyediakan bukti awal untuk verifikasi kualitas inventaris dan diskusi prioritas pemeriksaan/pemeliharaan, tanpa menggantikan inspeksi teknis atau keputusan petugas.
- **Time-bound:** pada tahap awal menyelesaikan Business Understanding, Data Understanding, audit kualitas, data dictionary, dan EDA; pada tahap lanjutan menyelesaikan preprocessing, pembandingan baseline, evaluasi model, serta eksplorasi klaster administratif.

### 2.4 Pertanyaan Analitik

1. Berapa jumlah dan proporsi kendaraan yang tercatat BAIK dan RUSAK pada snapshot data ini?
2. Bagaimana proporsi RUSAK bervariasi menurut wilayah, jenis kendaraan, klasifikasi, fungsi, dan penempatan?
3. Apakah model klasifikasi mengungguli baseline sederhana pada data uji yang tidak digunakan saat pelatihan?
4. Dapatkah unit administratif dikelompokkan berdasarkan profil agregat armadanya, dan apakah kelompok tersebut dapat dijelaskan serta stabil?
5. Informasi tambahan apa yang diperlukan sebelum hasil analitik layak digunakan untuk mendukung perencanaan operasional?

### 2.5 Metrik Keberhasilan

| Komponen | Metrik/bukti | Kriteria interpretasi |
|---|---|---|
| Kualitas data | Dimensi, missing value, duplikasi, konsistensi kategori | Semua langkah pembersihan terdokumentasi dan dapat direproduksi |
| EDA | Jumlah dan proporsi BAIK/RUSAK; tabel kondisi menurut wilayah/jenis | Selalu tampilkan denominator; hindari klaim berlebihan pada kelompok kecil |
| Asosiasi | Tabel silang dan Cramér’s V; uji chi-square bila asumsi memadai | Asosiasi bukan kausalitas; periksa frekuensi harapan |
| Klasifikasi | Dummy baseline, macro-F1, balanced accuracy, recall/precision RUSAK, confusion matrix | Bandingkan pada split yang sama; fokus pada kesalahan false negative kelas RUSAK |
| Klasterisasi | Profil klaster, ukuran klaster, silhouette score bila sesuai, stabilitas | Interpretabilitas dan kegunaan lebih penting daripada satu skor |
| Reprodusibilitas | Notebook berjalan dari awal sampai akhir dan dependensi tercatat | Path relatif, random_state tetap, data mentah tidak ditimpa |

Tidak ditetapkan ambang performa model yang seolah-olah sudah disepakati oleh pemilik layanan. Ambang penerimaan perlu dirumuskan bersama pemangku kepentingan berdasarkan konsekuensi kesalahan dan kapasitas verifikasi.

### 2.6 Nilai Bisnis dan Use Case

1. **Ringkasan inventaris:** menyediakan hitungan armada dan proporsi kondisi tercatat menurut wilayah serta jenis kendaraan.
2. **Penyaringan untuk verifikasi:** menandai kelompok dengan proporsi RUSAK relatif tinggi untuk diperiksa lebih lanjut, dengan selalu menyertakan jumlah observasi.
3. **Peningkatan kualitas data:** mengidentifikasi kategori tidak konsisten, metadata kosong, dan pencatatan yang perlu dikonfirmasi.
4. **Perencanaan analitik lanjutan:** merumuskan kebutuhan data tambahan seperti koordinat resmi, riwayat pemeliharaan, status aktif, ketersediaan kru, dan indikator kebutuhan layanan.
5. **Pembelajaran yang dapat direproduksi:** menyediakan notebook, dependensi, dan dokumentasi agar hasil akademik dapat diperiksa ulang.

### 2.7 Pemetaan Stakeholder

| Stakeholder | Kebutuhan | Keluaran potensial | Batasan/risiko |
|---|---|---|---|
| Dinas Penanggulangan Kebakaran dan Penyelamatan DKI Jakarta | Gambaran inventaris dan kondisi tercatat | Ringkasan agregat dan opsi evaluasi | Kondisi pada dataset bukan kesiapan aktual |
| Suku dinas/unit wilayah | Rincian komposisi armada | Tabel jumlah dan proporsi per wilayah | Bandingkan jumlah dan persentase, bukan persentase saja |
| Pengelola aset/pemeliharaan | Daftar aset/kelompok yang perlu diverifikasi | Daftar pemeriksaan awal | Bukan pengganti inspeksi teknis |
| Pengelola data/portal | Metadata, definisi variabel, frekuensi pembaruan | Catatan kualitas dan kebutuhan metadata | Lisensi dan definisi harus dikonfirmasi |
| Masyarakat/publik | Informasi agregat yang dapat dipahami | Visualisasi tanpa identifier | Hindari publikasi plat nomor dan penempatan sensitif |
| Peneliti/mahasiswa | Metode yang transparan dan dapat direproduksi | Notebook, dokumentasi, hasil evaluasi | Nyatakan batasan dan versi data |

### 2.8 Asumsi dan Batasan

- Data adalah snapshot periode 2025; tidak otomatis merepresentasikan keadaan saat ini.
- `Kondisi` diperlakukan sebagai label sumber BAIK/RUSAK; definisi prosedural dan waktu inspeksi belum diverifikasi secara independen.
- Dataset tidak memuat koordinat geografis, jarak ke lokasi kejadian, waktu respons, usia kendaraan, riwayat servis, jam operasi, ketersediaan kru, atau tingkat keparahan kerusakan.
- Nama wilayah administratif dapat digunakan untuk agregasi, tetapi bukan pengganti koordinat.
- Satu periode tidak mendukung analisis tren temporal atau prediksi deret waktu.
- Asumsi satu baris sama dengan satu kendaraan perlu dikonfirmasi dengan dokumentasi sumber dan pemeriksaan identifier.
- Dataset yang disertakan untuk GitHub telah menghapus `plat_nomor`; analisis yang menggunakan file sanitasi tidak dapat memverifikasi keunikan kendaraan berdasarkan plat.

### 2.9 Risiko, Etika, dan Mitigasi

| Risiko | Dampak | Mitigasi |
|---|---|---|
| Ketidakseimbangan kelas | Model mengutamakan BAIK dan melewatkan RUSAK | Laporkan macro-F1, balanced accuracy, recall RUSAK dan confusion matrix |
| Data leakage | Evaluasi terlalu optimistis | Keluarkan identifier; lakukan split sebelum fitting preprocessing; gunakan Pipeline |
| Bias cakupan/pencatatan | Inventaris tidak mencerminkan status operasional aktual | Nyatakan snapshot dan verifikasi definisi label dengan pemilik data |
| Denominator kecil | Proporsi ekstrem tampak meyakinkan padahal berbasis sedikit entri | Tampilkan jumlah dan persentase; gunakan bahasa hati-hati |
| Privasi/keamanan aset | Identifier dapat mengungkap aset operasional | Jangan mempublikasikan `plat_nomor`; gunakan data agregat |
| Ketidakjelasan lisensi | Redistribusi dapat melanggar ketentuan | Periksa metadata spesifik; jangan mengasumsikan CC0 hanya karena data terbuka |
| Otomasi berlebihan | Prediksi dianggap keputusan final | Jadikan hasil sebagai pendukung keputusan; verifikasi manusia tetap wajib |
| Bias spasial | Nama administratif dianggap mewakili jarak atau waktu tempuh | Sebut klaster profil administratif kecuali koordinat resmi tersedia |

### 2.10 Rencana CRISP-DM

| Fase | Rencana keluaran |
|---|---|
| Business Understanding | Masalah, tujuan SMART, metrik, stakeholder, nilai bisnis, batasan, risiko |
| Data Understanding | Audit sumber, data dictionary, kualitas data, EDA, bias dan representativitas |
| Data Preparation | Standarisasi kategori, audit identifier, penanganan missing value, encoding, split dan pipeline |
| Modeling | Baseline klasifikasi dan kandidat model; klasterisasi profil agregat bila unit analisis memadai |
| Evaluation | Metrik, confusion matrix, analisis kesalahan, stabilitas, fairness antarwilayah, manfaat dan risiko |
| Deployment | Demonstrasi notebook/dashboard secara proporsional, dokumentasi input-output, pemantauan drift dan evaluasi ulang |

## Catatan sumber dan sitasi

Dataset: Pemerintah Provinsi DKI Jakarta, Satu Data Jakarta, *Data Kendaraan Operasional Penanggulangan Kebakaran dan Penyelamatan*. URL: https://satudata.jakarta.go.id/open-data/detail?kategori=dataset&page_url=data-kendaraan-operasional-penanggulangan-kebakaran-dan-penyelamatan&data_no=1. Metadata lisensi spesifik perlu diverifikasi sebelum dokumentasi menyatakan CC0 atau sebelum data didistribusikan ulang.

Chapman, P., et al. (2000). *CRISP-DM 1.0: Step-by-step data mining guide*. SPSS. https://www.the-modeling-agency.com/crisp-dm.pdf

Pedregosa, F., et al. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research, 12*, 2825–2830. https://jmlr.org/papers/v12/pedregosa11a.html

Cramér, H. (1946). *Mathematical methods of statistics*. Princeton University Press.

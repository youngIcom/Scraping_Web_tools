# Scraper Data Program Studi SNBP

Sebuah skrip Python sederhana untuk melakukan pengambilan data (scraping) program studi dari situs web Seleksi Nasional Berdasarkan Prestasi (SNBP). Data yang diambil mencakup nama prodi, jenjang, daya tampung, jumlah peminat, dan jenis portofolio.

## Fitur

- Mengambil data dari halaman detail PTN berdasarkan ID.
- Menyimpan hasil scraping ke dalam format file `.csv`.
- Antarmuka baris perintah (CLI) yang mudah digunakan.
- Ekstraksi header tabel secara dinamis untuk ketahanan terhadap perubahan layout.

## Prasyarat

- Python 3.6+
- `pip` (Python package installer)

## Instalasi

1.  **Clone repository ini:**
    ```bash
    git clone https://github.com/youngIcom/Scraping_Web_tools.git
    cd Scraping_Web_tools
    ```

2.  **(Direkomendasikan) Buat dan aktifkan virtual environment:**
    ```bash
    # Untuk Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # Untuk Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install dependensi yang dibutuhkan:**
    Anda bisa menginstal library yang dibutuhkan satu per satu, atau lebih baik lagi, gunakan file `requirements.txt` (lihat rekomendasi di bawah).
    ```bash
    pip install requests beautifulsoup4 pandas
    ```

## Cara Penggunaan

Jalankan skrip dari terminal dengan memberikan dua argumen: `ptn_id` dan `nama_file_output`.

```bash
python scraping_data/scraping_snbp_cli.py <ptn_id> <nama_file_output>
```

**Contoh:**

Untuk mengambil data dari Universitas Syiah Kuala (ID: 111) dan menyimpannya sebagai `data_usk.csv`:

```bash
python scraping_data/scraping_snbp_cli.py 111 data_usk
```

Program akan secara otomatis menambahkan ekstensi `.csv` jika belum ada. File hasil akan tersimpan di direktori utama proyek.

## Daftar ID Perguruan Tinggi Negeri (PTN)

Berikut adalah daftar `ptn_id` yang dapat Anda gunakan:

| PTN ID | Nama Universitas |
| :--- | :--- |
| 111 | UNIVERSITAS SYIAH KUALA |
| 112 | UNIVERSITAS MALIKUSSALEH |
| 113 | UNIVERSITAS TEUKU UMAR |
| 114 | UNIVERSITAS SAMUDRA |
| 115 | ISBI ACEH |
| 121 | UNIVERSITAS SUMATERA UTARA (USU) |
| 122 | UNIVERSITAS NEGERI MEDAN (UNIMED) |
| 131 | UNIVERSITAS RIAU |
| 133 | UNIVERSITAS MARITIM RAJA ALI HAJI |
| 141 | UNIVERSITAS ANDALAS |
| 142 | UNIVERSITAS NEGERI PADANG |
| 143 | ISI PADANGPANJANG |
| 151 | UNIVERSITAS JAMBI |
| 161 | UNIVERSITAS BENGKULU |
| 171 | UNIVERSITAS SRIWIJAYA |
| 181 | UNIVERSITAS BANGKA BELITUNG |
| 191 | UNIVERSITAS LAMPUNG |
| 192 | INSTITUT TEKNOLOGI SUMATERA (ITERA) |
| 311 | UNIVERSITAS SULTAN AGENG TIRTAYASA |
| 321 | UNIVERSITAS INDONESIA (UI) |
| 323 | UNIVERSITAS NEGERI JAKARTA (UNJ) |
| 324 | UPN "VETERAN" JAKARTA |
| 329 | UNIVERSITAS TERBUKA |
| 331 | UNIVERSITAS SINGAPERBANGSA KARAWANG |
| 332 | INSTITUT TEKNOLOGI BANDUNG (ITB) |
| 333 | UNIVERSITAS PADJADJARAN |
| 334 | UNIVERSITAS PENDIDIKAN INDONESIA (UPI) |
| 335 | ISBI BANDUNG |
| 341 | IPB UNIVERSITY |
| 342 | UNIVERSITAS SILIWANGI |
| 351 | UNIVERSITAS JENDERAL SOEDIRMAN |
| 352 | UNIVERSITAS TIDAR |
| 353 | UNIVERSITAS SEBELAS MARET |
| 354 | ISI SURAKARTA |
| 355 | UNIVERSITAS DIPONEGORO (UNDIP) |
| 356 | UNIVERSITAS NEGERI SEMARANG |
| 361 | UNIVERSITAS GADJAH MADA (UGM) |
| 362 | UNIVERSITAS NEGERI YOGYAKARTA (UNY) |
| 363 | UPN "VETERAN" YOGYAKARTA |
| 364 | ISI YOGYAKARTA |
| 371 | UNIVERSITAS JEMBER |
| 372 | UNIVERSITAS BRAWIJAYA (UB) |
| 373 | UNIVERSITAS NEGERI MALANG |
| 381 | UNIVERSITAS AIRLANGGA |
| 382 | INSTITUT TEKNOLOGI SEPULUH NOPEMBER (ITS) |
| 383 | UNIVERSITAS NEGERI SURABAYA |
| 384 | UNIVERSITAS TRUNOJOYO MADURA |
| 385 | UPN "VETERAN" JAWA TIMUR |
| 511 | UNIVERSITAS TANJUNGPURA |
| 521 | UNIVERSITAS PALANGKARAYA |
| 531 | UNIVERSITAS LAMBUNG MANGKURAT |
| 541 | UNIVERSITAS MULAWARMAN |
| 542 | INSTITUT TEKNOLOGI KALIMANTAN |
| 551 | UNIVERSITAS BORNEO TARAKAN |
| 611 | UNIVERSITAS UDAYANA |
| 612 | UNIVERSITAS PENDIDIKAN GANESHA |
| 613 | ISI DENPASAR |
| 621 | UNIVERSITAS MATARAM |
| 631 | UNIVERSITAS NUSA CENDANA |
| 632 | UNIVERSITAS TIMOR |
| 711 | UNIVERSITAS HASANUDDIN |
| 712 | UNIVERSITAS NEGERI MAKASSAR |
| 718 | INSTITUT TEKNOLOGI B.J. HABIBIE |
| 721 | UNIVERSITAS SAM RATULANGI |
| 722 | UNIVERSITAS NEGERI MANADO |
| 731 | UNIVERSITAS TADULAKO |
| 741 | UNIVERSITAS SULAWESI BARAT |
| 751 | UNIVERSITAS HALU OLEO |
| 752 | UNIVERSITAS NEGERI GORONTALO |
| 753 | UNIVERSITAS SEMBILAN BELAS NOVEMBER KOLAKA |
| 811 | UNIVERSITAS PATTIMURA |
| 821 | UNIVERSITAS KHAIRUN |
| 911 | UNIVERSITAS CENDERAWASIH |
| 912 | UNIVERSITAS MUSAMUS MERAUKE |
| 913 | ISBI TANAH PAPUA |
| 921 | UNIVERSITAS PAPUA |

Gunakan kode ini dengan bijak dan untuk keperluan edukasi dan riset.

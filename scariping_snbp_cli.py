import requests
from bs4 import BeautifulSoup
import pandas as pd

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def scrape_snbp(ptn_id, output_filename):
    """
    Fungsinya adalah untuk mengumpulkan data PTN berdasarkan PTN_ID dan menyimpannya kedalam bentuk csv
    """

    url = f"https://sidatagrun-public-1076756628210.asia-southeast2.run.app/ptn_sn.php?ptn={ptn_id}"

    try:
        print(f"Mencoba mengakses URL: {url}")
        response = requests.get(url, headers=HEADERS, timeout=20)
        response.raise_for_status()
        print("Halaman berhasil di download...")

        soup = BeautifulSoup(response.text, 'html.parser')
        target_table = soup.find('table', class_='table table-striped vtop')

        if not target_table:
            print("Tidak ada tabel yang ditemukan di halaman")
            return 
        
        rows = target_table.find('tbody').find_all('tr')
        print(f"Menemukan {len(rows)} baris data program studi")

        extracted_data = []

        for row in rows:
            cols = row.find_all('td')
            if len(cols) == 7:
                nama_prodi_tag = cols[2].find('a')
                nama_prodi = nama_prodi_tag.text.strip() if nama_prodi_tag else cols[2].text.strip()
                data_prodi = {
                    'NO': cols[0].text.strip(),
                    'KODE': cols[1].text.strip(),
                    'NAMA PRODI': cols[2].text.strip(),
                    'JENJANG': cols[3].text.strip(),
                    'DAYA TAMPUNG 2025': cols[4].text.strip(),
                    'PEMINAT 2024': cols[5].text.strip(),
                    'JENIS PORTOFOLIO': cols[6].text.strip()
                }

                extracted_data.append(data_prodi)
        if not extracted_data:
            print("Tidak ada data yang berhasil di ekstrak...")
            return
        
        #kita pastikan kalau nama file harus berekstensi .csv agar lebih rapi
        if not output_filename.lower().endswith(".csv"):
            output_filename = f"{output_filename}.csv"

        df = pd.DataFrame(extracted_data)
        df.to_csv(output_filename, index=False, encoding='utf-8-sig')

        print("\nProses Scraping telah selesai...")
        print(f"Data berhasil disimpan dalam file: {output_filename}")
        print("menampilkan 10 baris data pertama")
        print(df.head(10))
    
    except requests.exceptions.RequestException as e:
        print(f"Terjadi Error ketika mengakses URL, Error: {e}")
    except Exception as e:
        print(f"Terjadi error tak terduga: {e}")

if __name__ == "__main__":
    ptn_id = input("Masukkan ptn_id, misalnya 111 untuk universitas syiah kumala : ")
    output_file = input("Masukkan nama file output (tanpa .csv pada akhir nama file: ")
    scrape_snbp(ptn_id, output_file)
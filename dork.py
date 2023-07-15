from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
import os
import time

pages_data = [0]

def get_pages(params):
    pages = int(params + "0")
    for i in range(1, pages):
        if i % 10 == 0:
            pages_data.append(i)

def get_dork(params):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.79'
    }
    results = []  # List untuk menyimpan hasil print
    with tqdm(total=len(pages_data), desc="Scanning pages") as pbar:
        for i in pages_data:
            url = "https://www.google.com/search?q=" + params + "&start=" + str(i)
            dork = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
            for j in dork.find_all('div', attrs={'class': 'g'}):
                result = j.find('a', href=True)['href']
                results.append(result)  # Menyimpan hasil print ke list
            pbar.update(1)  # Memperbarui progress bar
    return results

pages = input("Input Pages: ")
dork = input("Input Data: ")
get_pages(pages)
results = get_dork(dork)

# Simpan hasil print ke file teks
timestamp = str(int(time.time()))  # Menggunakan timestamp saat ini
filename = f"hasil{timestamp}.txt"
file_path = os.path.join(os.getcwd(), filename)

with open(file_path, "w") as file:
    for result in results:
        file.write(result + "\n")

print(f"Hasil pemindaian telah disimpan dalam file {filename}")

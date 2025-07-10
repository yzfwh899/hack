# fake_ransomware.py
# Simulasi ransomware, ga ngerusak apa pun

import os
import time

def ransomware_simulasi():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("File kamu udah dikunci.")
    print("Kalau mau balikin, kirim 0.5 BTC ke alamat ini:")
    print(">> [alamat-btc-palsu]")
    time.sleep(3)
    print("Tenang, ini cuma simulasi. Gak ada file yang beneran dikunci.")

if __name__ == "__main__":
    ransomware_simulasi()

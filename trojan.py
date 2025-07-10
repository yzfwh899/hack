# trojan_simulator.py
# Simulasi trojan yang connect ke server palsu (localhost)

import socket

def koneksi_simulasi():
    host = "127.0.0.1"
    port = 4444
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        print("Berhasil terhubung ke server command (simulasi).")
        s.close()
    except Exception as e:
        print("Gagal konek:", e)

if __name__ == "__main__":
    koneksi_simulasi()
# Simulasi ini hanya untuk tujuan edukasi, tidak untuk digunakan secara ilegal
# Pastikan untuk selalu mematuhi hukum dan etika saat belajar tentang keamanan siber.
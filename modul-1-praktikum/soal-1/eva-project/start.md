# Nomor 5
docker build -t eva-web-11:v1 ./v1
docker build -t eva-web-11:v2 ./v2

# Verifikasi image berhasil dibuat
docker images
---

# Nomor 6
# Menjalankan v1 di port 8080
docker run -d -p 8080:80 --name eva-container-11-v1 eva-web-11:v1

# Menjalankan v2 di port 8081
docker run -d -p 8081:80 --name eva-container-11-v2 eva-web-11:v2

# Pastikan keduanya berstatus "Up"
docker ps -a

---
# Nomor 7
Buka browser 8080 dan 8081

---
# Nomor 8
# 1. Hentikan dan hapus container v1 yang lama
docker stop eva-container-11-v1
docker rm eva-container-11-v1

# 2. Jalankan ulang dengan Volume (Bind Mount)
# Catatan: $(pwd) bekerja di Linux/Mac/PowerShell. Jika menggunakan CMD Windows, gunakan %cd%
docker run -d -p 8080:80 -v ./v1:/usr/share/nginx/html --name eva-container-11-v1 eva-web-11:v1

---
# Nomor 9
Buka v1/index.html , lalu tambahkan baris status (paling bawah)

<h1>EVANGELION STATUS SYSTEM</h1>
<p>Unit-02 Pilot: Asuka Langley Soryu</p>
<p>Version: v1 - Lightweight</p>
<p>Status: Unit-02 Launch Successful</p>

refresh dan cek 8080

---
# Nomor 10
# Masuk ke shell bash di dalam container v2
docker exec -it eva-container-11-v2 bash

# 1. Cek isi file HTML
cat /var/www/html/index.html

# 2. Verifikasi versi Nginx
nginx -v

# Keluar dari container jika sudah selesai
exit
 




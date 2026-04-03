#4
docker build -t eva-web-11:v1 .

docker images

#5
#docker run -d \ #karena diminta berjalan di background

--name eva-container-01 \ #karena diminta untuk menamai container

-p 8080:80 \ #kenapa :80 karena sebelumnnya diminta untuk ke port 80

docker run -d --name eva-container-11 -p 8080:80 -v ${PWD}/app:/usr/share/nginx/html -v ${PWD}/logs:/var/log/nginx eva-web-11:v1

#6. mengecek ke browser http://localhost:8080
#7. untuk melakukan ini tinggal mengubah di index.html nya pada baris kedua 
Unit-01 Launch Successful

#8. 
docker exec -it eva-container-11 /bin/bash
ls /usr/share/nginx/html
cat /usr/share/nginx/html/index.html #untuk menampilkan isi file
cat /var/log/nginx/access.log 
exit #

#9.
 docker ps #daftar container
 docker images #daftar image
docker logs eva-container-11 #daftar logs
docker stats eva-container-11 #untuk melihat statistik penggunaan

#10.
docker stop eva-container-11 #untuk menghentikan container
docker rm eva-container-11 #untuk menghapus container
docker rmi eva-web-11:v1 #untuk menghapus image
# eva-project/v2/Dockerfile
FROM ubuntu:latest
# Update repository dan install nginx tanpa prompt interaktif
RUN apt-get update && apt-get install -y nginx
COPY index.html /var/www/html/index.html
EXPOSE 80
# Menjalankan nginx di foreground
CMD ["nginx", "-g", "daemon off;"]
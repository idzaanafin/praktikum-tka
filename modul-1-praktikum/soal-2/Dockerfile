FROM debian:10

RUN echo "deb http://archive.debian.org/debian buster main" > /etc/apt/sources.list && \
    echo "deb http://archive.debian.org/debian-security buster/updates main" >> /etc/apt/sources.list && \
    apt update -y && apt upgrade -y && apt install -y mariadb-server && apt clean

CMD service mysql start && tail -f /dev/null
# Praktikan 2
5027241103 - Ni'mah Fauziyyah A

## 1. role baru khusus untuk deploy backend.
```
ansible-galaxy init roles/backend
```

## 2. vars atau vault untuk group khusus backend dalam inventory yang ada:
db_name
db_ username
backend_port
db_password
jwt_secret

- update  `inventory.yml`
```
# inventory.yml
all:
  children:
    backend:
      hosts:
        vps1:
          ansible_host: 143.198.212.108
        vps2:
          ansible_host: 143.198.197.59
```

- buat folder `group_vars`
``` mkdir group vars```

- Buat file Vault untuk grup backend:

``` ansible-vault create group_vars/backend.yml```

isi `backend.yml`:
```
---
# Poin 2: Variabel Backend

db_name: "modul_3_tka"
db_username: "kel11_tka"
backend_port: 5000
db_password: "kel11_tka"
jwt_secret: "rahasia_jwt_2067"
```

## 3. menyiapkan Dockerfile
- masuk ke folder backend
- buat Dockerfile 
``` nano Dockerfile```
- isi Dockerfile :
```
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 5000

CMD ["npm", "start"]
```

## 4. template Jinja2 untuk .env dan docker-compose.yml

- buat folder template dulu
```
mkdir -p roles/backend/templates
```

### A. template .env.j2
buat di `roles/backend/templates/env.j2`

```
# Database Configuration
DB_NAME={{ db_name }}
DB_USER={{ db_username }}
DB_PASSWORD={{ db_password }}
DB_HOST=db
DB_PORT=5432

# App Configuration
PORT={{ backend_port }}
JWT_SECRET={{ jwt_secret }}
```

### B. template `docker-compose.yml`
buat di `roles/backend/templates/docker-compose.yml.j2`

```
version: '3.8'

services:
  # i. Postgres untuk database [cite: 45]
  db:
    image: postgres:15-alpine
    restart: always
    environment:
      POSTGRES_DB: "{{ db_name }}"
      POSTGRES_USER: "{{ db_username }}"
      POSTGRES_PASSWORD: "{{ db_password }}"
    volumes:
      - db_data:/var/lib/postgresql/data

  # ii. Service backend dengan Dockerfile [cite: 46]
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    restart: always
    ports:
      - "{{ backend_port }}:{{ backend_port }}"
    env_file:
      - .env
    depends_on:
      - db

volumes:
  db_data:
```

## 5. membuat playbook
buka file `roles/backend/tasks/main.yml`

isi dengan :
```
# a. Membuka port backend sesuai backend_port [cite: 42]
- name: Membuka port backend di firewall
  become: true
  community.general.ufw:
    rule: allow
    port: "{{ backend_port | string }}"
    proto: tcp

- name: Memastikan direktori aplikasi ada di VPS
  file:
    path: "~/app-backend"
    state: directory
    mode: '0755'

- name: Mengirim folder backend ke VPS
  copy:
    src: backend/
    dest: "~/app-backend/backend/"
    mode: '0644'

- name: Mengolah template .env ke VPS
  template:
    src: env.j2
    dest: "~/app-backend/.env"
    mode: '0600'

- name: Mengolah template docker-compose.yml ke VPS
  template:
    src: docker-compose.yml.j2
    dest: "~/app-backend/docker-compose.yml"
    mode: '0644'

# b. Menyalakan backend dengan Docker Compose [cite: 43]
- name: Menjalankan container menggunakan Docker Compose
  community.docker.docker_compose_v2:
    project_src: "~/app-backend"
    state: present
    build: always

# c. Health check menggunakan perintah "uri"
- name: Melakukan health check ke backend
  ansible.builtin.uri:
    url: "http://localhost:{{ backend_port }}/" # Diarahkan ke root sesuai server.js
    method: GET
    status_code: 200
  register: health_result
  until: health_result.status == 200
  retries: 15  # Ditambah karena ada setTimeout 5 detik di server.js
  delay: 5
```


## 6. modifikasi playbook utama
`nano playbook.yml`

isi : 
```
---
- name: Install Docker di semua node
  hosts: all
  become: true
  roles:
    - role: docker

- name: Setup Backend Service
  hosts: backend
  roles:
    - role: backend

```

## 7. verifikasi
`ansible-playbook playbook.yml`

### a. curl health check
``` curl http://143.198.212.108:5000/ ```

### b. register user
``` 
curl -X POST http://143.198.212.108:5000/api/register \
     -H "Content-Type: application/json" \
     -d '{"username": "ninim2_tka", "password": "password_aman2"}'
```

### c. login 
```
curl -X POST http://143.198.212.108:5000/api/login \
     -H "Content-Type: application/json" \
     -d '{"username": "ninim2_tka", "password": "password_aman2"}'
```

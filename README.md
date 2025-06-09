## 📡 Network Management Platform (Flask + MikroTik + OLT)

This is a modular Flask web application designed to securely manage and automate network devices like MikroTik Routers and OLTs (Optical Line Terminals) using Python. It provides a simple web interface to handle PPPoE, IP pools, profiles, ONT provisioning, and more.

### 🔧 Features

- MikroTik Integration
- OLT Integration (Multi-Vendor Ready)
- Web Features

### 🗂️ Tech Stack

- Python 3.11+
- Flask (with Blueprint structure)
- Paramiko / Netmiko for SSH-based OLT control
- RouterOS API for MikroTik
- MongoDB with Flask-PyMongo
- Jinja2 templates for frontend rendering
- Docker-ready
- JWT for API security
- dotenv for environment management

### 🚀 Getting Started

#### Step 1: Copy `.env.example` file content, create one `.env` file and change credentials according to you.

#### Step 2: You must have docker install in your system or you can download and install it from [Docker's official website](https://www.docker.com/products/docker-desktop/). Now, run the `docker-compose` file using the command in your terminal below.

```bash
docker-compose up --build
```

#### Step 3: Now, you can visit `http://127.0.0.1:5001/` to find your index page that tells you your installation is done.

#### Step 4: You can start contributing...

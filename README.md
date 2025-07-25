# 🔐 Encrypted RDP-Like Communication via AES (Educational)

This is a simple educational project simulating a basic encrypted remote communication channel between a **server** and a **client**, using Python sockets and **AES encryption** (CFB mode).  
It is designed for learning **network programming**, **cryptography basics**, and secure command exchange.

---

## 🚀 Features

- 🔗 Encrypted communication with AES (16-byte key, CFB mode)
- 🧠 Base64-encoded message transmission
- 💬 Shell-style command execution (input/output)
- 📡 Simple socket server for handling a remote connection
- 🔐 No plain-text transfer – everything is encrypted

---

## ⚠️ Legal Disclaimer

> This project is strictly for **educational** purposes (e.g., learning encryption, Python sockets).  
**Do NOT use it for unauthorized access, penetration testing without consent, or malicious activity.**

---

## 🧪 How It Works

1. The **server** waits for incoming connections on a port (e.g., `4444`)
2. The **client** connects to the server.
3. Commands sent by the server are encrypted using AES and sent to the client.
4. The client executes the command locally and sends back the encrypted result.
5. The server decrypts and displays the response.

---

## 📁 Files

- `server.py`: Runs a socket server, sends encrypted commands
- `client.py`: Connects to server, decrypts commands, runs them, and returns encrypted results
- `requirements.txt`: Required packages for the project

---

## 🔧 Requirements

- Python 3.12+
- `pycryptodome` for AES encryption

Install dependencies:

```bash
pip install -r requirements.txt

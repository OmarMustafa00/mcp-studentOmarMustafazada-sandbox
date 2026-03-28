import os

def connect():
    aws_secret_key = os.getenv("AWS_SECRET_KEY")
    if not aws_secret_key:
        print("Hata: AWS_SECRET_KEY ortam degiskeni bulunamadi.")
        return
    print("Guvenli bir sekilde baglanti kuruluyor...")

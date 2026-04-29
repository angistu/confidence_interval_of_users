import csv
import random
from daftar import *

# nama file nantinya
nama_file = "HIGO_User_v2.csv"

def generate_dataset(n):
    dataset = []
    i = 0
    for nomor in range(1, n + 1):
        # inisiasi perhitungan
        i += 1
        
        jam_login = random.randint(0,23)
        menit_login = random.randint(0,59)

        durasi_jam = jam_login+random.randint(1,5)
        durasi_menit = menit_login+random.randint(10,50)

        jam_logout = durasi_jam if durasi_jam < 24 else durasi_jam-24
        menit_logout = durasi_menit if durasi_menit < 60 else durasi_menit-60

        # inisialisasi kolom
        user_id = i
        login = f"{jam_login:02d}:{menit_login:02d}"
        logout = f"{jam_logout:02d}:{menit_logout:02d}"
        user = f"{random.choice(daftarNama)} {random.choice(daftarNama)}"
        email = f"{str.split(user," ")[0]}{random.choice(daftarEmail)}"
        phone = f"+628{random.randint(1000000000,9999999999)}"
        year_of_birth = random.randint(1960,2002)
        phone_type = random.choice(daftarHP)
        interest = random.choice(digitalInterest)
        location = random.choice(daftarLokasi)

        # Kolom
        data = [
            user_id,
            login,
            logout,
            user,
            email,
            phone,
            year_of_birth,
            phone_type,
            interest,
            location
        ]
        dataset.append(data)
    return dataset

# memanggil fungsi
try:
    dataset = generate_dataset(3000)
except ValueError as e:
    print(f"ada error: {e}")


# header dataset
header = [
    "user_id",
    "login",
    "logout",
    "user",
    "email",
    "phone",
    "year_of_birth",
    "phone_type",
    "interest",
    "location"
    ]

# menyimpan ke file csv
with open(nama_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(dataset)

# pemberitahuan
print("Dataset berhasil digenerate dan disimpan dalam " + nama_file)

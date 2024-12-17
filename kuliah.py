import random

class Mahasiswa:
    def __init__(self, nama, spp):
        self.nama = nama
        self.spp = spp
        self.nilai_tugas = 0
        self.nilai_ujian = 0
        self.nilai_akhir = 0

    def bayar_spp(self):
        print(f"{self.nama} telah membayar SPP sebesar {self.spp} IDR.")

    def mengikuti_kuliah(self):
        print(f"{self.nama} sedang mengikuti kuliah Informatika...")

    def mengerjakan_tugas(self):
        # Simulasi nilai tugas
        self.nilai_tugas = random.randint(60, 100)
        print(f"{self.nama} telah mengerjakan tugas dengan nilai: {self.nilai_tugas}")

    def mengikuti_ujian(self):
        # Simulasi nilai ujian
        self.nilai_ujian = random.randint(60, 100)
        print(f"{self.nama} telah mengikuti ujian dengan nilai: {self.nilai_ujian}")

    def hitung_nilai_akhir(self):
        # Menghitung nilai akhir (misalnya, 40% tugas dan 60% ujian)
        self.nilai_akhir = (0.4 * self.nilai_tugas) + (0.6 * self.nilai_ujian)
        print(f"Nilai akhir {self.nama} adalah: {self.nilai_akhir:.2f}")

def main():
    # Input nama mahasiswa dan SPP
    nama_mahasiswa = input("Masukkan nama mahasiswa: ")
    spp = int(input("Masukkan jumlah SPP yang harus dibayar (dalam IDR): "))

    # Membuat objek mahasiswa
    mahasiswa = Mahasiswa(nama_mahasiswa, spp)

    # Proses mengikuti kuliah
    mahasiswa.bayar_spp()
    mahasiswa.mengikuti_kuliah()
    mahasiswa.mengerjakan_tugas()
    mahasiswa.mengikuti_ujian()
    mahasiswa.hitung_nilai_akhir()

if __name__ == "__main__":
    main()


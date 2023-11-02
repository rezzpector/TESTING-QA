import unittest

# Fungsi sederhana yang akan diuji
def hitung_gaji(gaji_pokok, tunjangan):
    if gaji_pokok < 0:
        return "Gaji tidak valid"
    if tunjangan < 0:
        return "Tunjangan tidak valid"

    total_gaji = gaji_pokok + tunjangan
    return total_gaji

# Kelas unit testing white-box
class TestHitungGaji(unittest.TestCase):

    def test_gaji_positif(self):
        result = hitung_gaji(5000, 1000)
        self.assertEqual(result, 6000)  # Memastikan gaji positif berfungsi dengan benar

    def test_gaji_negatif(self):
        result = hitung_gaji(-5000, 1000)
        self.assertEqual(result, "Gaji tidak valid")  # Memastikan gaji negatif berfungsi dengan benar

    def test_tunjangan_negatif(self):
        result = hitung_gaji(5000, -1000)
        self.assertEqual(result, "Tunjangan tidak valid")  # Memastikan tunjangan negatif berfungsi dengan benar

    def test_gaji_dan_tunjangan_negatif(self):
        result = hitung_gaji(-5000, -1000)
        self.assertEqual(result, "Gaji tidak valid")  # Memastikan gaji dan tunjangan negatif berfungsi dengan benar

    def test_gaji_dan_tunjangan_nol(self):
        result = hitung_gaji(0, 0)
        self.assertEqual(result, 0)  # Memastikan gaji dan tunjangan nol berfungsi dengan benar

if __name__ == '__main__':
    unittest.main()

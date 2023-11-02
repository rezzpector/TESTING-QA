import unittest

# Fungsi sederhana yang akan diuji
def tambah(a, b):
    return a + b

# Kelas unit testing
class TestTambah(unittest.TestCase):

    def test_tambah_angka_positif(self):
        self.assertEqual(tambah(2, 3), 5)  # Memastikan 2 + 3 = 5

    def test_tambah_angka_negatif(self):
        self.assertEqual(tambah(-2, -3), -5)  # Memastikan -2 + (-3) = -5

    def test_tambah_campuran(self):
        self.assertEqual(tambah(2, -3), -1)  # Memastikan 2 + (-3) = -1

if __name__ == '__main__':
    unittest.main()
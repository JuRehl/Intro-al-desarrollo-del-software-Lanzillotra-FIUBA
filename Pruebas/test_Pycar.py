import unittest
from PyCar import Pycar

class test_Pycar(unittest.TestCase):
    def test_encerder(self):
        auto=Pycar()
        self.assertTrue(auto.encender())
    def test_apagar(self):
        auto=Pycar()
        self.assertFalse(auto.apagar())
    def test_acelerar(self):
        auto=Pycar()
        auto.acelerar()
        self.assertGreater(auto.acelerar(),0)
    def test_frenar(self):
        auto=Pycar()
        auto.frenar()
        self.assertEqual(auto.frenar(),0)
    # def test_doblar_izquierda(self):
    #     auto=Pycar()
    #     auto.direccion()
    #     self.assertEqual(auto.doblarizq())
    # def test_doblar_derecha(self):
    #     auto=Pycar()
    #     self.assertEqual(auto.doblarder())
    def test_retroceder(self):
        auto=Pycar()
        auto.retroceder()
        self.assertLess(auto.retroceder(), 0)

if __name__=='__main__':
    unittest.main()
import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_tilavuus_nollataan(self):
        v = Varasto(0, -1)
        self.assertAlmostEqual(v.tilavuus, 0)

    def test_saldo_nollataan(self):
        v = Varasto(0, -1)
        self.assertAlmostEqual(v.saldo, 0)

    def test_ylijaama(self):
        v = Varasto(1, 2)
        self.assertAlmostEqual(v.saldo, 1)

    def test_ei_negatiivista(self):
        v = self.varasto.lisaa_varastoon(-1)
        self.assertEqual(v, None)

    def test_liikaa(self):
        self.varasto.lisaa_varastoon(20)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ota_negatiivinen(self):
        v = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(v, 0)

    def test_ota_liikaa(self):
        self.varasto.lisaa_varastoon(3)
        v = self.varasto.ota_varastosta(4)
        self.assertAlmostEqual(self.varasto.saldo, 0)
        self.assertAlmostEqual(v, 3)

    def test_str(self):
        v = self.varasto.__str__()
        self.assertEqual(v, "saldo = 0, vielä tilaa 10")

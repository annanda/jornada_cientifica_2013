import random
import unittest

from fatoracao import fermat, fatoracao_trivial

class TestFatoracaoFunctions(unittest.TestCase):

    def setUp(self):
        #roda a cada execucao de teste
        self.seq = range(10)

    def test_fermat(self):
        self.assertEqual(fermat(25),[5,5])
        self.assertEqual(fermat(15),[5,3])
        self.assertEqual(fermat(17),[1,17])
        # self.assertEqual(fermat(20),[5,4])

    def test_fatoracao_trivial(self):
        self.assertEqual(fatoracao_trivial(15),3)

        # self.assertEqual(fermat(15),[3,5])

    # def test_choice(self):
    #     element = random.choice(self.seq)
    #     self.assertTrue(element in self.seq)

    # def test_sample(self):
    #     with self.assertRaises(ValueError):
    #         random.sample(self.seq, 20)
    #     for element in random.sample(self.seq, 5):
    #         self.assertTrue(element in self.seq)

import random
import unittest

from fatoracao import fermat, fatoracao_trivial, RetornoTrivialCompleta,\
 fatoracao_trivial_completa, crivo

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


    def test_retorno_fatoracao_trivial_completa(self):
        retorno = RetornoTrivialCompleta([3,5,7],[4,7,2])
        self.assertEqual(retorno.list_fatores, [3,5,7])
        self.assertEqual(retorno.list_expoentes, [4,7,2])


    def test_fatoracao_trivial_completa(self):
        self.assertEqual(fatoracao_trivial_completa(20).list_fatores, [2,5])
        self.assertEqual(fatoracao_trivial_completa(20).list_expoentes, [2,1])

    def test_crivo(self):
        self.assertEqual(crivo(5),[2,3,5])
        self.assertEqual(crivo(6),[2,3,5])
        self.assertEqual(crivo(7),[2,3,5,7])
        self.assertEqual(crivo(10),[2,3,5,7])
        self.assertEqual(crivo(11),[2,3,5,7,11])
        self.assertEqual(crivo(20),[2,3,5,7,11,13,17,19])

    # def test_choice(self):
    #     element = random.choice(self.seq)
    #     self.assertTrue(element in self.seq)

    # def test_sample(self):
    #     with self.assertRaises(ValueError):
    #         random.sample(self.seq, 20)
    #     for element in random.sample(self.seq, 5):
    #         self.assertTrue(element in self.seq)

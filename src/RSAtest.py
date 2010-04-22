'''
Created on Apr 1, 2010

@author: oc
'''
from RSA import RSA, DynamInt
import unittest

class TestRSAOperations(unittest.TestCase):

    def setUp(self):
        self.p= DynamInt(10)
        self.q = DynamInt(10)
        #self.p.setData("821089628001493")
        #self.q.setData("1872967539195764008553239")   
        
        self.rsa = RSA(0)        
        self.rsa.createkeys(self.p, self.q)
    def test_encdec(self):
        '''
        Test regular encoding and decoding of numbers
        '''
        a = DynamInt()
        a.setData("25")
        rsa = RSA(0)
        rsa.p.setData("11")
        rsa.q.setData("3")
        rsa.e.setData("3")
        rsa.n.setData("33")
        rsa.phi.setData("20")
        rsa.d.setData("7")
        d =  rsa.powmod(a,rsa.e,rsa.n)
        f =  rsa.powmod(d,rsa.d,rsa.n)
        self.assertEqual(a.data, f.data)
        
        
        
    def test_disguise(self):
        strr = "iamaboy"
        rsa = RSA(0)
        num=rsa.disguise(strr)
        self.assertEqual("iamaboy", rsa.reveal(num))
    def test_encryptionDecryption(self):
        # make sure we can encrypt and decrypt
        crypted = self.rsa.encrypt("iam")
        result = self.rsa.decrypt(crypted)
        temp=''
        for i in result:
            temp = temp+i
        self.assertEqual("iam", temp)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRSAOperations)
    unittest.TextTestRunner(verbosity=5).run(suite)
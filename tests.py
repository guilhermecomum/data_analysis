import unittest
from data_analysis import read_file, calculate_sale, parse_salesman, parse_client, parse_sale

class TestDataAnalysis(unittest.TestCase):
    def test_calculate_sale(self):
        self.assertEqual(calculate_sale('[1-10-100,2-30-2.50,3-40-3.10]'), 1199.0)
        self.assertEqual(calculate_sale('[1-34-10,2-33-1.50,3-40-0.10]'), 393.5)

    def test_parse_salesman(self):
        self.assertEqual(parse_salesman('001ç1234567891234çDiegoç50000'), ['1234567891234','Diego','50000'])
        self.assertEqual(parse_salesman('001ç3245678865434çRenatoç40000.99'), ['3245678865434','Renato','40000.99'])

    def test_parse_client(self):
        self.assertEqual(parse_client('002ç2345675434544345çJose da SilvaçRural'), ['2345675434544345','Jose da Silva','Rural'])
        self.assertEqual(parse_client('002ç2345675433444345çEduardo PereiraçRural'), ['2345675433444345','Eduardo Pereira','Rural'])

    def test_parse_sale(self):
        self.assertEqual(parse_sale('003ç10ç[1-10-100,2-30-2.50,3-40-3.10]çDiego'), ['10',1199.0,'Diego'])
        self.assertEqual(parse_sale('003ç08ç[1-34-10,2-33-1.50,3-40-0.10]çRenato'), ['08', 393.5,'Renato'])


    def

if __name__ == '__main__':
    unittest.main()

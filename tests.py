import unittest
import data_analysis


class TestDataAnalysis(unittest.TestCase):
    def setUp(self):
        self.collection = ['001ç1234567891234çDiegoç50000\n', '001ç3245678865434çRenatoç40000.99\n', '002ç2345675434544345çJose da SilvaçRural\n', '002ç2345675433444345çEduardo PereiraçRural\n', '003ç10ç[1-10-100,2-30-2.50,3-40-3.10]çDiego\n', '003ç08ç[1-34-10,2-33-1.50,3-40-0.10]çRenato\n']

    def test_calculate_sale(self):
        self.assertEqual(data_analysis.calculate_sale('[1-10-100,2-30-2.50,3-40-3.10]'), 1199.0)
        self.assertEqual(data_analysis.calculate_sale('[1-34-10,2-33-1.50,3-40-0.10]'), 393.5)

    def test_parse_salesman(self):
        self.assertEqual(data_analysis.parse_salesman('001ç1234567891234çDiegoç50000'), ['1234567891234','Diego','50000'])
        self.assertEqual(data_analysis.parse_salesman('001ç3245678865434çRenatoç40000.99'), ['3245678865434','Renato','40000.99'])

    def test_parse_client(self):
        self.assertEqual(data_analysis.parse_client('002ç2345675434544345çJose da SilvaçRural'), ['2345675434544345','Jose da Silva','Rural'])
        self.assertEqual(data_analysis.parse_client('002ç2345675433444345çEduardo PereiraçRural'), ['2345675433444345','Eduardo Pereira','Rural'])

    def test_parse_sale(self):
        self.assertEqual(data_analysis.parse_sale('003ç10ç[1-10-100,2-30-2.50,3-40-3.10]çDiego'), ['10',1199.0,'Diego'])
        self.assertEqual(data_analysis.parse_sale('003ç08ç[1-34-10,2-33-1.50,3-40-0.10]çRenato'), ['08', 393.5,'Renato'])

    def test_ranking_salesman(self):
        sales = ['003ç10ç[1-10-100,2-30-2.50,3-40-3.10]çDiego','003ç08ç[1-34-10,2-33-1.50,3-40-0.10]çRenato']
        salesmans = ['001ç1234567891234çDiegoç50000','001ç3245678865434çRenatoç40000.99']
        self.assertEqual(data_analysis.ranking_salesman(sales, salesmans), [('Renato', 393.5), ('Diego', 1199.0)])

    def test_expensive_sale(self):
        sales = ['003ç10ç[1-10-100,2-30-2.50,3-40-3.10]çDiego','003ç08ç[1-34-10,2-33-1.50,3-40-0.10]çRenato']
        self.assertEqual(data_analysis.expensive_sale(sales), ['10', 1199.0, 'Diego'])

    def test_sales_collection(self):
        sales = ['003ç10ç[1-10-100,2-30-2.50,3-40-3.10]çDiego','003ç08ç[1-34-10,2-33-1.50,3-40-0.10]çRenato']
        self.assertEqual(data_analysis.sales_collection(sales), [['10',1199.0,'Diego'], ['08', 393.5,'Renato']])

    def test_salesman_collection(self):
        salesmans = ['001ç1234567891234çDiegoç50000','001ç3245678865434çRenatoç40000.99']
        self.assertEqual(data_analysis.salesmans_collection(salesmans), [['1234567891234','Diego','50000'],['3245678865434','Renato','40000.99']])

    def test_parse_collection(self):
        self.assertDictEqual.__self__.maxDiff = None
        self.assertDictEqual(
            data_analysis.parse_data(self.collection),
            {
                'salesmans': [['1234567891234', 'Diego', '50000'], ['3245678865434', 'Renato', '40000.99']],
                'clients': [['2345675434544345', 'Jose da Silva', 'Rural'], ['2345675433444345', 'Eduardo Pereira', 'Rural']],
                'sales': [['10', 1199.0, 'Diego'], ['08', 393.5, 'Renato']]
            })

if __name__ == '__main__':
    unittest.main()

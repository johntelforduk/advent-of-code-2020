from solution14 import dec_to_bin, bin_to_dec, apply_mask
import unittest


class TestFunctions(unittest.TestCase):

    def test_functions(self):
        self.assertEqual(dec_to_bin('11'), '000000000000000000000000000000001011')
        self.assertEqual(dec_to_bin('73'), '000000000000000000000000000001001001')
        self.assertEqual(dec_to_bin('101'), '000000000000000000000000000001100101')

        self.assertEqual(bin_to_dec('000000000000000000000000000000001011'), 11)
        self.assertEqual(bin_to_dec('000000000000000000000000000001001001'), 73)
        self.assertEqual(bin_to_dec('000000000000000000000000000001100101'), 101)

        self.assertEqual(apply_mask('000000000000000000000000000000001011',
                                    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'),
                                    '000000000000000000000000000001001001')

        self.assertEqual(apply_mask('000000000000000000000000000001100101',
                                    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'),
                                    '000000000000000000000000000001100101')

        self.assertEqual(apply_mask('000000000000000000000000000000000000',
                                    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'),
                                    '000000000000000000000000000001000000')


if __name__ == '__main__':
    unittest.main()

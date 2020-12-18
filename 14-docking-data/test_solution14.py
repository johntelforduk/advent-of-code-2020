# Unit tests for day 14 of AOC 2020, Docking Data.

from solution14 import dec_to_bin, bin_to_dec, apply_mask, apply_new_mask, decoder
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

        self.assertEqual(apply_new_mask(mask='000000000000000000000000000000X1001X', binary=dec_to_bin('42')),
                                             '000000000000000000000000000000X1101X')

        self.assertEqual(apply_new_mask(mask='00000000000000000000000000000000X0XX', binary=dec_to_bin('26')),
                                             '00000000000000000000000000000001X0XX')

        self.assertEqual(decoder('000000000000000000000000000000011010'), ['000000000000000000000000000000011010'])

        self.assertEqual(decoder('000000000000000000000000000000X1101X'),
                                ['000000000000000000000000000000011010',
                                 '000000000000000000000000000000011011',
                                 '000000000000000000000000000000111010',
                                 '000000000000000000000000000000111011'])

        self.assertEqual(decoder('00000000000000000000000000000001X0XX'),
                                ['000000000000000000000000000000010000',
                                 '000000000000000000000000000000010001',
                                 '000000000000000000000000000000010010',
                                 '000000000000000000000000000000010011',
                                 '000000000000000000000000000000011000',
                                 '000000000000000000000000000000011001',
                                 '000000000000000000000000000000011010',
                                 '000000000000000000000000000000011011'])


if __name__ == '__main__':
    unittest.main()

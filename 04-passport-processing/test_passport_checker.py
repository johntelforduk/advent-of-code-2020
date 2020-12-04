# Script to test the PassportChecker class.

from passport_checker import PassportChecker
import unittest


class TestPassportChecker(unittest.TestCase):

    def test_single_checks(self):
        this_checker = PassportChecker()

        self.assertTrue(this_checker.check_byr('2002'))
        self.assertFalse(this_checker.check_byr('2003'))

        self.assertTrue(this_checker.check_hgt('60in'))
        self.assertTrue(this_checker.check_hgt('190cm'))
        self.assertFalse(this_checker.check_hgt('190in'))
        self.assertFalse(this_checker.check_hgt('190'))

        self.assertTrue(this_checker.check_hcl('#123abc'))
        self.assertFalse(this_checker.check_hcl('#123abz'))
        self.assertFalse(this_checker.check_hcl('123abc'))

        self.assertTrue(this_checker.check_ecl('brn'))
        self.assertFalse(this_checker.check_ecl('wat'))

        self.assertTrue(this_checker.check_pid('000000001'))
        self.assertFalse(this_checker.check_pid('0123456789'))

    def test_single_whole_passports(self):
        this_checker = PassportChecker()

        self.assertFalse(this_checker.check_passport({'eyr': '1972',
                                                      'cid': '100',
                                                      'hcl': '#18171d',
                                                      'ecl': 'amb',
                                                      'hgt': '170',
                                                      'pid': '186cm',
                                                      'iyr': '2018',
                                                      'byr': '1926'}))

        self.assertFalse(this_checker.check_passport({'iyr': '2019',
                                                      'hcl':  '#602927',
                                                      'eyr': '1967',
                                                      'hgt': '170cm',
                                                      'ecl': 'grn',
                                                      'pid': '012533040',
                                                      'byr': '1946'}))

        self.assertFalse(this_checker.check_passport({'hcl': 'dab227',
                                                      'iyr': '2012',
                                                      'ecl': 'brn',
                                                      'hgt': '182cm',
                                                      'pid': '021572410',
                                                      'eyr': '2020',
                                                      'byr': '1992',
                                                      'cid': '277'}))

        self.assertFalse(this_checker.check_passport({'hgt': '59cm',
                                                      'ecl': 'zzz',
                                                      'eyr': '2038',
                                                      'hcl': '74454a',
                                                      'iyr': '2023',
                                                      'pid': '3556412378',
                                                      'byr': '2007'}))

        self.assertTrue(this_checker.check_passport({'pid': '087499704',
                                                     'hgt': '74in',
                                                     'ecl': 'grn',
                                                     'iyr': '2012',
                                                     'eyr': '2030',
                                                     'byr': '1980',
                                                     'hcl': '#623a2f'}))

        self.assertTrue(this_checker.check_passport({'eyr': '2029',
                                                     'ecl': 'blu',
                                                     'cid': '129',
                                                     'byr': '1989',
                                                     'iyr': '2014',
                                                     'pid': '896056539',
                                                     'hcl': '#a97842',
                                                     'hgt': '165cm'}))
        self.assertTrue(this_checker.check_passport({'hcl': '#888785',
                                                     'hgt': '164cm',
                                                     'byr': '2001',
                                                     'iyr': '2015',
                                                     'cid': '88',
                                                     'pid': '545766238',
                                                     'ecl': 'hzl',
                                                     'eyr': '2022'}))

        self.assertTrue(this_checker.check_passport({'iyr': '2010',
                                                     'hgt': '158cm',
                                                     'hcl': '#b6652a',
                                                     'ecl': 'blu',
                                                     'byr': '1944',
                                                     'eyr': '2021',
                                                     'pid': '093154719'}))


if __name__ == '__main__':
    unittest.main()

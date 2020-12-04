import re


class PassportChecker:

    def __init__(self):
        pass

    @staticmethod
    def check_byr(byr: str) -> bool:
        """byr (Birth Year) - four digits; at least 1920 and at most 2002."""
        return re.match('^[0-9]{4}$', byr) is not None and ('1920' <= byr <= '2002')

    @staticmethod
    def check_iyr(iyr: str) -> bool:
        """iyr (Issue Year) - four digits; at least 2010 and at most 2020."""
        return re.match('^[0-9]{4}$', iyr) is not None and ('2010' <= iyr <= '2020')

    @staticmethod
    def check_eyr(eyr: str) -> bool:
        """eyr (Expiration Year) - four digits; at least 2020 and at most 2030."""
        return re.match('^[0-9]{4}$', eyr) is not None and ('2020' <= eyr <= '2030')

    @staticmethod
    def check_hgt(hgt: str) -> bool:
        """hgt (Height) - a number followed by either cm or in:
           If cm, the number must be at least 150 and at most 193.
           If in, the number must be at least 59 and at most 76."""
        if re.match('^[0-9]{3}cm$|^[0-9]{2}in$', hgt) is None:
            return False
        return hgt[-2:] == 'cm' and ('150' <= hgt[:3] <= '193') or '59' <= hgt[:3] <= '76'

    @staticmethod
    def check_hcl(hcl: str) -> bool:
        """hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f."""
        return re.match('^#[0-9|a-f]{6}$', hcl) is not None

    @staticmethod
    def check_ecl(ecl: str) -> bool:
        """ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth."""
        return re.match('^amb|blu|brn|gry|grn|hzl|oth$', ecl) is not None

    @staticmethod
    def check_pid(pid: str) -> bool:
        """pid (Passport ID) - a nine-digit number, including leading zeroes."""
        return re.match('^[0-9]{9}$', pid) is not None

    def check_passport(self, passport) -> bool:
        for required_key, checker in [('byr', self.check_byr),
                                      ('iyr', self.check_iyr),
                                      ('eyr', self.check_eyr),
                                      ('hgt', self.check_hgt),
                                      ('hcl', self.check_hcl),
                                      ('ecl', self.check_ecl),
                                      ('pid', self.check_pid)]:
            if required_key not in passport:
                return False
            if checker(passport[required_key]) is False:
                return False
        return True

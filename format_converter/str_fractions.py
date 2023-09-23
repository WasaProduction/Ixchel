from fractions import Fraction


class StrFractions:
    def __init__(self, my_fraction='0'):
        self.my_value = 0
        #   Look for rational number
        if '/' in my_fraction:
            #   Look for whole number (space)
            if ' ' in my_fraction:
                #   Separate whole number from rational part (space)
                pair = my_fraction.split()
                #   Cast pieces into int
                try:
                    whole = int(pair[0])
                except ValueError:
                    #   TODO
                    whole = 0
                    print('Impossible to cast whole', pair[0], 'to int')
                #   Second part into Fraction
                try:
                    self.my_value = self.break_fraction(pair[1])
                except ValueError:
                    #   TODO
                    self.my_value = 0
                    print('Impossible to cast whole', pair[0], 'to int')
                self.my_value += Fraction(whole, 1)
            #   Only rational
            else:
                self.my_value = self.break_fraction(my_fraction)

        #   Look for decimal number
        elif '.' in my_fraction:
            #   Decimal
            decimal = None
            try:
                decimal = float(my_fraction)
            except ValueError:
                #   TODO
                print('Impossible to cast', my_fraction, 'to fraction')
            self.my_value = Fraction(decimal)

    def break_fraction(self, frac):
        my_fraction = frac.split('/')
        try:
            num = int(my_fraction[0])
            denom = int(my_fraction[1])
            return Fraction(num, denom)
        except ValueError:
            #   TODO
            print('Impossible to cast fraction', my_fraction, 'to int')
            return Fraction(0)

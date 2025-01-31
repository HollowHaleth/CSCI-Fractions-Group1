class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        #TODO
        pass

    def gcd(firstNumber, secondNumber):
        '''
        Gets the Greatest Common Denominator of firstNumber and secondNumber
        '''

        firstNumber = abs(firstNumber)
        secondNumber = abs(secondNumber)

        if firstNumber == 0 or secondNumber == 0:
            return 0

        elif firstNumber == secondNumber:
            return firstNumber

        else: 
            for i in range(min(firstNumber, secondNumber), 0, -1):
                if firstNumber % i == 0 and secondNumber % i == 0:
                    return i

    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass

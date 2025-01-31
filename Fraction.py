class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        
        if type(numerator) == int:
            self.numerator_holder = numerator
            if type(denominator) == int:
                self.denominator_holder = denominator


        elif type(numerator)== str:
            try:
                numerator = numerator.strip()
                self.numerator_holder = int(numerator.split("/")[0])
                self.denominator_holder = int(numerator.split("/")[1])

            except:
                self.numerator_holder = 0
                self.denominator_holder = 1

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

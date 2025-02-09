class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        '''
        Initialize numerator and denominator
        '''

        self.numerator_holder = 0
        self.denominator_holder = 1
        
        # Integer Inputs
        if type(numerator) == int:
            self.numerator_holder = numerator
            
            if type(denominator) == int:
                self.denominator_holder = denominator

        # String Inputs
        elif type(numerator)== str and numerator.count("/") <= 1:
            try:
                numerator = numerator.strip()
                self.numerator_holder = int(numerator.split("/")[0])
                
                if numerator.count("/") == 1 and numerator.split("/")[1] != "":
                    self.denominator_holder = int(numerator.split("/")[1])

            except:
                None
                
        if self.denominator_holder == 0:
            raise ZeroDivisionError

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
        try:
            # Simplified Numerator
            return f"{int(self.numerator_holder / Fraction.gcd(self.numerator_holder,self.denominator_holder)) }"
        except:
            return 0

    def get_denominator(self):
        try:
            # Simplified Denominator
            return f"{int(self.denominator_holder / Fraction.gcd(self.numerator_holder,self.denominator_holder))}"
        except:
            return 0

    def get_fraction(self):
        positive_numerator = abs(int(self.get_numerator()))
        positive_denominator = abs(int(self.get_denominator()))

        if self.denominator_holder == 1:
            return f"{self.numerator_holder}"
        else:
            if (self.numerator_holder < 0 and self.denominator_holder < 0) or \
            (self.numerator_holder > 0 and self.denominator_holder > 0):
                return f"{positive_numerator}/{positive_denominator}"
            elif(self.numerator_holder > 0 and self.denominator_holder < 0) or \
            (self.numerator_holder < 0 and self.denominator_holder > 0):
                return f"-{positive_numerator}/{positive_denominator}"
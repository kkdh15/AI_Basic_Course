# Operator Override
class Complex:
    def __init__(self,i,j):
        self.__i = i
        self.__j = j
    
    def __add__(self, complex_other):
        i = self.__i + complex_other.__i
        j = self.__j + complex_other.__j
        return Complex(i,j)

    def __sub__(self, complex_other):
        i = self.__i - complex_other.__i
        j = self.__j - complex_other.__j
        return Complex(i,j)

    def __mul__(self,complex_other):
        i = (self.__i * complex_other.__i) - (self.__j * complex_other.__j)
        j = (self.__i * complex_other.__j) + (self.__i * complex_other.__j)
        return Complex(i,j)
        #숙제 : 복소수의 나눗셈

    def __str__(self): # print() 호출
        return str(self.__i) + " + " + str(self.__j) + "i"
cp1 = Complex(1,2)
cp2 = Complex(5,6)
cp3 = cp1 + cp2
print(cp3)
cp4 = cp1 * cp2
print(cp4)
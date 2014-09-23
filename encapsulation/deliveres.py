__author__ = 'ednaldafakira'
class Delivered(object):#class to call the attributes of objects.
    def __init__(self): #Construction method to design the object (Delivered)
        self.sale1= 0
        self.sale2= 0
        self.sale3= 0
        self.sale4= 0
        self.sale5= 0
        self.__total= 0 #private attribute only access inside this class


 #decorators treating properties as variables
    @property #getter: to return the total sales. It's accessing the total monthly sales attribute that is private only accessed inside the class Delivered.
    def total(self):#function
        return self.__total # return the total monthly sales attribute

    @total.setter #setter: It gives the ability to update the total monthly sales result as it need.
    def total(self, new_total):
        self.__total = new_total

    def calc_total(self):#function to calculate the total monthly sales by adding the sales together.
        self.__total = self.sale1 + self.sale2 + self.sale3 + self.sale4 + self.sale5

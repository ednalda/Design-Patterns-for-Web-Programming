__author__ = 'ednaldafakira'
from view import AppView
class AppForm(AppView):
    def __init__(self):#construction function for class appView
        super(AppForm, self).__init__()#AppForm inherit object from AppView
        self.form_open = '<form method="GET">'# form attributes
        self.form_close = '</form>'
        self.__inputs = []#private attribute protect information collected by user through input
        self.form_inputs = ''

    @property#to be able access the inputs attributes and overrides, the decorator: property is here and empty.
    def inputs(self):
        pass

    @inputs.setter #Setter: overrides attribute inputs to access data
    def inputs(self, arr):
        self.__inputs = arr
        for item in arr:#sending data "from" the attribute inputs to the array: view.inputs as requested
            self.form_inputs += '<input type="' + item[1] + '" name"' + item[0]+'" />'



    def print_out_form(self):
        data = self.head +  self.body + self.form_open + self.form_inputs + self.form_close + self.close
        data = data.format(**locals())
        return data
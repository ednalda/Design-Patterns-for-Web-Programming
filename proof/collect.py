__author__ = 'ednaldafakira'
from view import AppView
class AppForm(AppView):
    def __init__(self):#construction function for class appView
        super(AppForm, self).__init__()
        self.form_open = '<form method="GET">'
        self.form_close = '</form>'
        self.__inputs = []
        self.form_inputs = ''

    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, arr):
        self.__inputs = arr
        for item in arr:
            self.form_inputs += '<input type="' + item[1] + '" name"' + item[0]+'" />'



    def print_out_form(self):
        data = self.head +  self.body + self.form_open + self.form_inputs + self.form_close + self.close
        data = data.format(**locals())
        return data


class Employee:
    increm = 1.2
    
    def __init__(self,first,last,pay):
        self.f_name=first
        self.l_name=last
        self.paid=pay

    def full_name(self):
        return '{} {}'.format(self.f_name,self.l_name)
        
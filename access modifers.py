# This Is For OOPS ON GLOBAL NOT ONLY PYTHON , PYTHON DOESNT ENFORCE IT 
# Public , Private , Encrypted/Protected Access Modifiers
# all Variables are by Default Public

class employee:
    def __init__(self):
        self.__name = "Harry"
        

a = employee()
# print(a.__name) Cannot Be Accessed Directly



# The Above is a Private Access  It is Indicated Using "   __         "
print(a._employee__name) # can be accessed Indirectly



print(a.__dir__())


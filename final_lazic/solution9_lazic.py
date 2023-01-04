class pet():
    #Forgot colon in the pet tag

    #type is a python function 
    def __init__(self, types, color):
        self.type = types
        self.color = color
     
    def show(self):
        #wrong quotations used
        print("type is", self.type )
        #self.model is not defined, it is supposed to be self.type
        print("color is", self.color )

        #in the requirements you said it had to output Color is Brown for this
        #first result but you set it to blue
        #that might not be an error but im gonna change it anyway
        
austin = pet("dog", "brown")
        #wrong quotations used
whitney = pet("fish", "green")

austin.show()   

whitney.show()
#forgot the brackets for whitney.show()

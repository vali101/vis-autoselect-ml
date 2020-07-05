class classifiedArray: 
    
    def __init__(self, data, types):
        self.type = types
        self.data = data
        
    def __str__(self):
        return str(self.__dict__)
    

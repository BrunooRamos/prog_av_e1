class List:

    '''
    Clase que representa un monad de lista. 
    Se puede instanciar con un valor o sin él.
    '''

    def __init__(self, value=None):
        self.value = value

    def bind(self, func):
        if self.value is None:
            return List()
        else:
            try:
                result = func(self.value)
                return List(result)
            except Exception as e:
                print("Error:", e)
                return List()
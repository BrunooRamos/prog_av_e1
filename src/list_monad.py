class List:

    '''
    This class is a simple implementation of the List monad.
    The List monad is a type of monad that represents a list of values.
    '''

    def __init__(self, value=None):
        '''
        The constructor of the List class.
        It takes an optional value as an argument.
        '''

        self.value = value

    def bind(self, func):

        '''
        This method takes a function as an argument and applies it to the value of the List.
        It returns a new List with the result of the function.
        '''

        if self.value is None:
            return List()
        else:
            try:
                result = func(self.value)
                return List(result)
            except Exception as e:
                print("Error:", e)
                return List()
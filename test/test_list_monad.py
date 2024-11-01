from src.list_monad import List
import unittest

class TestListMonad(unittest.TestCase):

    def test_initialization_with_value(self):
        # Caso en el que se inicializa con un valor
        list_instance = List(10)
        self.assertEqual(list_instance.value, 10)

    def test_initialization_without_value(self):
        # Caso en el que se inicializa sin un valor
        list_instance = List()
        self.assertIsNone(list_instance.value)

    def test_bind_with_function(self):
        # Prueba que bind aplique la función correctamente
        list_instance = List(5)
        result = list_instance.bind(lambda x: x * 2)
        self.assertEqual(result.value, 10)

    def test_bind_with_none(self):
        # Prueba que bind retorne una instancia vacía si value es None
        list_instance = List()
        result = list_instance.bind(lambda x: x * 2)
        self.assertIsNone(result.value)

    def test_bind_with_exception_handling(self):
        # Prueba que bind maneje excepciones y retorne una instancia vacía
        list_instance = List(5)
        result = list_instance.bind(lambda x: x / 0)  # Esto causará una excepción
        self.assertIsNone(result.value)

if __name__ == '__main__':
    unittest.main()

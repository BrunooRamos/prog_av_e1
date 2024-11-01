import unittest
from unittest.mock import patch, mock_open
import io
from src.functions import load_questions, unique_random_generator, choose_questions, ask_question

class TestTriviaFunctions(unittest.TestCase):

    def test_load_questions(self):
        # Datos simulados del archivo CSV sin espacios adicionales al inicio
        csv_content = """question,option1,option2,option3,correct_option
"What is the capital of France?","New York","London","Paris","Paris"
"What is the capital of Spain?","New York","London","Madrid","Madrid"
        """
        with patch("builtins.open", mock_open(read_data=csv_content)):
            questions = load_questions("trivia_questions.csv")
            expected_result = [
            ["What is the capital of France?", "New York", "London", "Paris", "Paris"],
            ["What is the capital of Spain?", "New York", "London", "Madrid", "Madrid"]
        ]
        self.assertEqual(questions, expected_result)


    def test_unique_random_generator(self):
        # Prueba que el generador retorne `count` valores únicos
        count = 5
        gen = unique_random_generator(count)
        generated_numbers = list(gen)
        
        self.assertEqual(len(generated_numbers), count)
        self.assertEqual(len(set(generated_numbers)), count)  # Todos deben ser únicos

    def test_choose_questions(self):
        # Lista simulada de preguntas
        questions = [
            ["What is the capital of France?", "New York", "London", "Paris", "Paris"],
            ["What is the capital of Spain?", "New York", "London", "Madrid", "Madrid"],
            ["What is the capital of Italy?", "New York", "Rome", "Paris", "Rome"],
            ["What is the capital of Germany?", "New York", "London", "Berlin", "Berlin"],
            ["What is the capital of England?", "New York", "London", "Paris", "London"],
            ["What is the capital of Portugal?", "New York", "Lisbon", "Paris", "Lisbon"]
        ]
        selected_questions = choose_questions(questions)
        
        self.assertEqual(len(selected_questions), 5)
        for question in selected_questions:
            self.assertIn(question, questions)  # Las preguntas elegidas deben estar en la lista original

    @patch('builtins.input', side_effect=['3'])
    def test_ask_question_correct(self, mock_input):
        # Prueba de una respuesta correcta
        question = ["What is the capital of France?", "New York", "London", "Paris", "Paris"]
        
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            result = ask_question(question)
            self.assertTrue(result)
            self.assertIn('Correct', fake_output.getvalue())

    @patch('builtins.input', side_effect=['1'])
    def test_ask_question_incorrect(self, mock_input):
        # Prueba de una respuesta incorrecta
        question = ["What is the capital of France?", "New York", "London", "Paris", "Paris"]
        
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            result = ask_question(question)
            self.assertFalse(result)
            self.assertIn('Incorrect', fake_output.getvalue())

if __name__ == '__main__':
    unittest.main()

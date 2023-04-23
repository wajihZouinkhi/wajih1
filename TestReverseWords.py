import unittest
from unittest.mock import patch, Mock
from TDD_reverse_words import reverse_words
class TestReverseWords(unittest.TestCase):
    
    def test_reverse_words_empty_string(self):
        self.assertEqual(reverse_words(''), None)
        
    def test_reverse_words_single_word(self):
        self.assertEqual(reverse_words('hello'), None)
        
    def test_reverse_words_multiple_words(self):
        self.assertEqual(reverse_words('hello world'), None)
    
    def test_reverse_words_with_mock_return_value(self):
        mock_words = Mock()
        mock_words.split.return_value = ['world', 'hello']
        self.assertEqual(reverse_words(mock_words), None)
    
    def test_reverse_words_with_mock_side_effect(self):
        mock_words = Mock()
        mock_words.split.side_effect = lambda: ['world', 'hello']
        self.assertEqual(reverse_words(mock_words), None)
    
    def test_reverse_words_with_return_value(self):
        result = reverse_words('hello world')
        self.assertEqual(result, None)

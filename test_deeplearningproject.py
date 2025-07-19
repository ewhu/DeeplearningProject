# test_deeplearningproject.py
"""
Tests for DeeplearningProject module.
"""

import unittest
from deeplearningproject import DeeplearningProject

class TestDeeplearningProject(unittest.TestCase):
    """Test cases for DeeplearningProject class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DeeplearningProject()
        self.assertIsInstance(instance, DeeplearningProject)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DeeplearningProject()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

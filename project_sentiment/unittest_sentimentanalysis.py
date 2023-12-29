##Flask = Micro-framework, minimal to no dependence on external libraries
##AssertEqual compares two values and determines if equal (actual, expected)

import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):
   def test_sentiment_analyzer(self):
      result1 = sentiment_analyzer("I love working with Python")
      self.assertEqual(result1['label'], 'SENT_POSITIVE')
      result2 = sentiment_analyzer("I hate working with Python")
      self.assertEqual(result2['label'], 'SENT_NEGATIVE')
      result3 = sentiment_analyzer("I am neutral with Python")
      self.assertEqual(result3['label'], 'SENT_NEUTRAL')

if __name__ == "__main__":
    unittest.main()
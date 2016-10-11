import unittest
from weather_api import get_weather

class TestWeatherApi(unittest.TestCase):
    """Test weather api"""

    def test_response(self):
        self.assertTrue(get_weather())

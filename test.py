from assistant import NutritionalAssistant

# Test the class with a real example and a few meals

assistant = NutritionalAssistant('John', 25, 180, 72)
assistant.add_meal(500)
assistant.add_meal(700)
assistant.add_meal(300)
assistant.add_meal(400)

print(assistant.get_calories())
print(assistant.get_bmr())

# Write a unit test for the NutritionalAssistant class using unittest

import unittest

class TestNutritionalAssistant(unittest.TestCase):
  def test_calories(self):
    assistant = NutritionalAssistant('John', 25, 180, 72)
    assistant.add_meal(500)
    assistant.add_meal(700)
    assistant.add_meal(300)
    assistant.add_meal(400)
    self.assertEqual(assistant.get_calories(), 1900)

  def test_bmr(self):
    assistant = NutritionalAssistant('John', 25, 180, 72)
    self.assertEqual(assistant.get_bmr(), 2100.0)

  def test_preferences(self):
    assistant = NutritionalAssistant('John', 25, 180, 72)
    assistant.set_preferences('meat and pizza')
    self.assertEqual(assistant.preferences, 'meat and pizza')

  def test_allergies(self):
    assistant = NutritionalAssistant('John', 25, 180, 72)
    assistant.set_allergies('gluten')
    self.assertEqual(assistant.allergies, 'gluten')

if __name__ == '__main__':
  unittest.main()

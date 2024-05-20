"""
Develop a class called NutritionalAssistant that will help users to track their daily
food intake and provide nutritional information about the food they eat.
The class should have the following methods:
1. __init__(self, name: str, age: int, weight: float, height: float
2. add_meal(self, calories: int)
3. get_calories(self) -> int
4. get_bmr(self) -> float
5. set_preferences(self, preferences: str)
6. set_allergies(self, allergies: str)
7. run(self)
"""

import requests

class NutritionalAssistant:
  def __init__(self, name: str, age: int, weight: float, height: float):
    self.name = name
    self.age = age
    self.weight = weight
    self.height = height

    self.preferences = "meat and pizza"
    self.allergies = "gluten"

    self.meals = []

  def add_meal(self, calories: int):
    self.meals.append({ 'calories': calories })

  def get_calories(self) -> int:
    return sum([meal['calories'] for meal in self.meals])

  def get_bmr(self) -> float:
    return 10 * self.weight + 6.25 * self.height - 5 * (self.age + 5)

  # Add methods to set preferences
  def set_preferences(self, preference: str = ""):
    if preference:
      self.preferences = preference
    else:
      self.preferences = input('Enter preferences: ')

  # Add methods to set allergies
  def set_allergies(self, allergie: str = ""):
    if allergie:
      self.allergies = allergie
    else:
      self.allergies = input('Enter allergies: ')

  def run(self):
    while True:
      print('Commands: add, calories, bmr, preferences, allergies, suggestion')
      command = input('Enter a command: ')
      if command == 'add':
        calories = int(input('Enter calories: '))
        self.add_meal(calories)
      elif command == 'calories':
        print(self.get_calories())
      elif command == 'bmr':
        print(self.get_bmr())
      elif command == 'preferences':
        self.set_preferences()
      elif command == 'allergies':
        self.set_allergies()
      elif command == 'suggestion':
        self.create_suggestion()

  #  Add a method to create suggestion using OpenAI API 
  def create_suggestion(self):
    response = requests.post(
      'https://api.openai.com/v1/chat/completions',
      headers={
        'Content-Type': 'application/json',
        'Authorization': 'Bearer sk-proj-54n9OoR05BFA7vAhH62NT3BlbkFJZqWCHOPP6GaHBwJ6hUll',
        'OpenAI-Organization': 'org-PtxPei9rsDZ7WznQ2DBDYCvF',
        'OpenAI-Project': 'proj_dPgwdW0OXgQprnyBZtutgsdK',
      },
      json={
        'model': 'gpt-3.5-turbo-0125',
        'response_format': { 'type': 'json_object' },
        'messages': [
          {
            'role': 'user',
            'content': f'What should I eat for breakfast? I am a {self.age} year old {self.preferences} who is {self.allergies} and weighs {self.weight} kg and is {self.height} cm tall. I have the following preferences: {self.meals} and the following allergies: {self.allergies}. The output format should be JSON.'
          }
        ]
      }
    )

    print(f"""
Suggestion:
{response.json()['choices'][0]['message']['content']}
""")

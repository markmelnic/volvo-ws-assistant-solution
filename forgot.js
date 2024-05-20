// Create a list of 10 food types with calories, protein, fat, and carbs

const foods = [
  {
    name: "apple",
    calories: 95,
    protein: 0.5,
    fat: 0.3,
    carbs: 25
  },
  {
    name: "banana",
    calories: 105,
    protein: 1.3,
    fat: 0.4,
    carbs: 27
  },
  {
    name: "orange",
    calories: 62,
    protein: 1.2,
    fat: 0.2,
    carbs: 15
  },
  {
    name: "grapes",
    calories: 69,
    protein: 0.7,
    fat: 0.2,
    carbs: 18
  },
  {
    name: "strawberries",
    calories: 49,
    protein: 0.9,
    fat: 0.4,
    carbs: 11
  },
  {
    name: "blueberries",
    calories: 57,
    protein: 0.7,
    fat: 0.3,
    carbs: 14
  },
  {
    name: "raspberries",
    calories: 64,
    protein: 1.5,
    fat: 0.8,
    carbs: 15
  },
  {
    name: "blackberries",
    calories: 43,
    protein: 2,
    fat: 0.5,
    carbs: 10
  },
  {
    name: "pineapple",
    calories: 82,
    protein: 0.5,
    fat: 0.2,
    carbs: 22
  },
  {
    name: "watermelon",
    calories: 46,
    protein: 0.9,
    fat: 0.2,
    carbs: 11
  }
]

// Filter out the food types that have more than 10g of protein
const highProteinFoods = foods.filter(food => food.protein > 10)

// Sort foods by calories
const sortedFoods = foods.sort((a, b) => a.calories - b.calories)

// Sort foods by calories and name
const sortedFoodsByName = foods.sort((a, b) => {
  if (a.calories === b.calories) {
    return a.name.localeCompare(b.name)
  }
  return a.calories - b.calories
})

// How many apples will it take to reach 1000 calories?
const applesTo1000Calories = Math.ceil(1000 / foods.find(food => food.name === "apple").calories)

// How many calories are in 5 bananas?
const caloriesIn5Bananas = foods.find(food => food.name === "banana").calories * 5

// Et cetera

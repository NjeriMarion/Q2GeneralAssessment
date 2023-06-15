# **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.

class AncestralStories:
    def __init__(self, length, moral_lesson, age_group):
        self.length = length
        self.moral_lesson = moral_lesson
        self.age_group= age_group
        self.language = "English"
        self.stories = {}
        self.storytellers= {}

    def story(self,tittle, story):
        if tittle in self.stories:
            return f"The story with the tittle {tittle} is already in the system"
        else:
            self.stories[tittle] = story
            return f"{tittle} was added successfully, here is the list of all stories available{self.stories}"
#checking if the story and the story teller are already in the system thenadding them if not
    def storyteller(self,story, storyteller):
        if story in self.storytellers:
            return f"The story {story} was narrated by {storyteller} "
        else:
            self.storytellers[story] = storyteller
            return f"{storyteller} was added successfully to {self.storytellers}"
  #checking if the language requested is the same as the initial language then display the story in the language requested    
    def translator(self,story, story_language):
        if story_language == self.language:
            return f'{self.stories[story]}'
        else:
            return f'{story} has been translated from {self.language} to {story_language},\n{self.stories[story]} '
        
#creating an instance for the above class

river_and_the_source = AncestralStories(200, "independence", "16-20")
print(river_and_the_source.story("River and the source", "This is a story of a young lady from the home of..."))
print(river_and_the_source.story("The pearl", "This is a story of a young lady from the home of..."))
print(river_and_the_source.storyteller("River and the source", "Ogola"))
print(river_and_the_source.translator("River and the source", "English"))
print(river_and_the_source.translator("River and the source", "Kiswahili"))


# **African Cuisine:** You're creating a recipe app specifically for African cuisine.
# The app needs to handle recipes from different African countries, each with its
# unique ingredients, preparation time, cooking method, and nutritional
# information. Consider creating a `Recipe` class, and think about how you might
# create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# methods.


class Recipe:
    def __init__(self):
        self.meals = []
        self.ingredients = {}
        self.prep_time = {}
        self.nutritional_info = {}

    def add_recipes (self, meal , ingredients, prep_time, nutritional_info):
        if meal in self.meals:
            return f"{meal} is already in the recipe app"
        else: 
            self.ingredients[meal] = ingredients
            self.nutritional_info[meal] = nutritional_info
            self.prep_time[meal] = prep_time
            return f'{meal} has been added to the recipe app. It uses the following ingredients{self.ingredients[meal]}, with a prep time of {self.prep_time[meal]} and {self.nutritional_info} as its nutritional info'

    def remove_recipe(self, meal):
        if meal in self.meals:
            self.ingredients.pop(meal)
            self.nutritional_info.pop(meal)
            self.prep_time.pop(meal)
            return f"{meal} has been removed from the app"
        else:
            return f"{meal} is not on the app"
    
    def display_recipe(self, meal):
        if meal in self.meals:
            return f" {meal} \n{self.ingredients[meal]} \n{self.prep_time[meal]}, \n{self.nutritional_info[meal]}"
        else:
            return f"{meal} is not found"
        
appOne = Recipe()
appOne.add_recipes("Pilau", ["rice","meat", "spices"], "2hrs", "Energy giving")
appOne.add_recipes("Pilau", ["rice","meat", "spices"], "2hrs", "Energy giving")
appOne.remove_recipe("Pilau")
appOne.display_recipe("Pilau")
appOne.display_recipe("Pizza")

# **Wildlife Preservation:** You're a wildlife conservationist working on a
# program to track different species in a national park. Each species has its own
# characteristics and behaviors, such as its diet, typical lifespan, migration
# patterns, etc. Some species might be predators, others prey. You'll need to
# create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
# these classes might relate to each other through inheritance.


class Wildlife:
    def __init__(self, diet, lifespan, migrationPatterns):
        self.diet = diet
        self.lifespan = lifespan
        self.migration= migrationPatterns

class PreyOrPredator(Wildlife):
    def __init__(self, diet, lifespan, migrationPatterns):
        super().__init__(diet, lifespan, migrationPatterns)
        # self.animal_status = animal
        self.prey = {"cat":"Prey"}
    def status(self,status , animal):
        if animal in self.prey :
            return f"{animal} is a prey"
        else:
            return f"{animal} is a predator"
        
tsavo = PreyOrPredator("Carnivore", range(30), "Tsavo_north to Tsavo_south")
tsavo.status("prey", "Lion")
tsavo.status("prey", "cat")



# Create a class called Product with attributes for name, price, and quantity.
# Implement a method to calculate the total value of the product (price * quantity).
# Create multiple objects of the Product class and calculate their total values.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_value(self):
        total = self.price * self.quantity
        return total
    
rice = Product("rice", 200, 3)
print(rice.total_value)
sugar = Product("rice", 400, 5)
print(sugar.total_value)
pepper = Product("rice", 600, 6)
print(pepper.total_value)

# Implement a class called Student with attributes for name, age, and grades (a
# list of integers). Include methods to calculate the average grade, display the
# student information, and determine if the student has passed (average grade >=
# 60). Create objects for the Student class and demonstrate the usage of these
# methods.
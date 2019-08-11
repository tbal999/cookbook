# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 15:17:36 2019

@author: thoma
"""
#Cooking app.
#You can:
#Create Recipes and give them a name, with ingredients.
#Search for Recipe from name.
#Type in ingredients and find a Recipe that matches them.

import csv
from copy import copy

recipe = []
ingredients = []
nest = []

def Start():
    print(recipe)
    print(ingredients)
    print("== Cook Book ==")
    print("Please choose from the following options...")
    print("c - to create a recipe")
    print("s - to select a recipe")
    print("e - to export to a cookbook")
    print("i - to import a cookbook")
    print("Press anything else to quit.")
    x = input("Please choose now:" )
    if x == "c":
        createRecipe1()
    if x == "s":
        selectRecipe1()
    if x == "e":
        exportRecipe()
    if x == "i":
        importRecipe()
    else:
        quit()
        
def createRecipe1():
    print("Create Recipe!")
    x = input("First, type in the name of your Recipe:" )
    recipe.append(x)
    print("Your recipe is called "+x+"! Now let's talk about ingredients.")
    createRecipe2()
    
def createRecipe2():
    global ingredients
    global nest
    x = input("Type in your ingredient:" )
    nest.append(str(x))
    x = input("Ok, "+x+"... now would you like to add another ingredient? y/n:")
    if x == "y":
        createRecipe2()
    else:
        ingredients.append(copy(nest))
        nest.clear()
        print(ingredients)
        Start()

def selectRecipe1():
    x = input("What recipe would you like to pick?")
    recipeindex = 0
    for a in recipe[recipeindex:]:
        if a == x:
            print("You selected "+a+".")
            print("This is recipe number "+str(recipeindex)+".")
            break
        else:
            recipeindex = recipeindex + 1
    for a in ingredients[recipeindex:]:
        print("The ingredients for this recipe are....")
        print(a)
        break
    Start()
    
def exportRecipe():
    global recipe
    global ingredients
    with open('recipe.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(recipe)
    csvFile.close()
    with open('ingredients.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(ingredients)
    csvFile.close()
    Start()
    
def importRecipe():
    global recipe
    global ingredients
    with open("recipe.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            recipe.append(row)
    with open("ingredients.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            ingredients.append(row)
    Start()

Start()

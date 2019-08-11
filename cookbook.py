# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 15:17:36 2019

@author: thomasbalcombe
"""
#Cooking app.

import csv
from copy import copy
import time

recipe = []
instructions = []
ingredients = []
nest = []

def Start():
    print("The Cookbook!")
    print("Please choose from the following options...")
    print("s - to select a recipe")
    print("c - to create a recipe")
    print("d - to delete a recipe")
    print("p - to print out recipe names")
    print("e - to export what you've created to csv")
    print("i - to import from csv")
    print("Or press anything else to quit.")
    x = input("Please choose an option:" )
    if x == "c":
        createRecipe1()
    if x == "s":
        selectRecipe1()
    if x == "e":
        exportRecipe()
    if x == "i":
        importRecipe()
    if x == "p":
        printRecipe()
    if x == "d":
        deleteRecipe()
    else:
        quit()
        
def createRecipe1():
    global recipe
    global nest
    print("Create Recipe!")
    x = input("First, type in the name of your Recipe:" )
    nest.append(str(x))
    print("Your recipe is called "+x+"! Now let's talk about ingredients.")
    recipe.append(copy(nest))
    nest.clear()
    createRecipe2()
    
def createRecipe2():
    global ingredients
    global nest
    x = input("Type in your ingredient:" )
    nest.append(str(x))
    x = input("Ok... now would you like to add another ingredient? y/n:" )
    if x == "y":
        createRecipe2()
    else:
        ingredients.append(copy(nest))
        nest.clear()
    createRecipe3()
        
def createRecipe3():
    global ingredients
    global nest
    x = input("Now please type in the instructions:" )
    nest.append(str(x))
    x = input("Ok... now would you like to add additional instructions? y/n:" )
    if x == "y":
        createRecipe3()
    else:
        instructions.append(copy(nest))
        nest.clear()
    Start()
        

def selectRecipe1():
    xa = input("What recipe would you like to pick?" )
    x = str(xa)
    recipeindex = 0
    for a in recipe[recipeindex:]:
        for i in a:
            if i == x:
                print("You selected "+i+".")
                print("This is recipe number "+str(recipeindex)+".")
                break
        else:
            recipeindex = recipeindex + 1
    for a in ingredients[recipeindex:]:
        print("The ingredients for this recipe are....")
        print("...")
        for i in a:
            print("")
            print(i)
            time.sleep(0.5)
        break
    for a in instructions[recipeindex:]:
        print("The instructions for this recipe are....")
        print("...")
        for i in a:
            print("")
            print(i)
            time.sleep(1)
        break
    recipeindex = 0
    print("---------------")
    Start()
    
def deleteRecipe():
    xa = input("What recipe would you like to delete?" )
    print("---the recipe below---")
    x = str(xa)
    print(x)
    recipeindex = 0
    for a in recipe[recipeindex:]:
        for i in a:
            if i == x:
                recipe.remove(recipe[recipeindex])
                break
        else:
            recipeindex = recipeindex + 1
    for a in ingredients[recipeindex:]:
        ingredients.remove(ingredients[recipeindex])
        break
    for a in instructions[recipeindex:]:
        instructions.remove(instructions[recipeindex])
        break
    recipeindex = 0
    print("---has been deleted---")
    Start()
    
def exportRecipe():
    global recipe
    global ingredients
    with open('recipe.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(recipe)
    csvFile.close()
    with open('ingredients.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(ingredients)
    csvFile.close()
    with open('instructions.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(instructions)
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
    with open("instructions.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            instructions.append(row)
    Start()
    
def printRecipe():
    print("---")
    print(recipe)
    print("---")
    Start()

Start()

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 15:17:36 2019

@author: thoma
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
    print("Cookbook!")
    print("Please choose from the following options...")
    print("c - to create a recipe")
    print("s - to select a recipe")
    print("e - to export what you've created")
    print("i - to import what you've already created")
    print("p - print out recipe names")
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
    if x == "p":
        printRecipe()
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
    x = input("Ok, "+x+"... now would you like to add another ingredient? y/n:")
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
    x = input("Ok, "+x+"... now would you like to add additional instructions? y/n:")
    if x == "y":
        createRecipe3()
    else:
        instructions.append(copy(nest))
        nest.clear()
    Start()
        

def selectRecipe1():
    xa = input("What recipe would you like to pick?")
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
    print("---------------")
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
    print(recipe)
    print(ingredients)
    Start()

Start()

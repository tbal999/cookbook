# cookbook
for cooking recipes
uses regular expressions & string interpolation

The Cookbook!
Simple command line cookbook that lets you select multiple options:
s - to select a recipe
c - to create a recipe
d - to delete a recipe
p - to print out recipe names
e - to export what you've created to csv
i - to import from csv
also:
ed - delete exported data
x - ingredients search (regex - search for an ingredient and it will provide you recipes that use that ingredient)

USE CASES:
Press c,
type in name of recipe i.e white loaf
type in ingredients i.e 500g strong white flour, tablespoon of olive oil etc
then type in instructions i.e mix flour and water, leave to proove etc etc.

Press s,
type "white loaf"
Then the ingredients & instructions will be printed.

Press d,
type "white loaf"
This recipe will be deleted.

Press e,
This will append the current recipes to a few CSVs (containing recipe names,ingredients,instructions).

Press i,
This allows you to quickly import any recipes you've already created from the same CSVs.


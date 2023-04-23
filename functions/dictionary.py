thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict.get("model"))
print(thisdict.get("year"))
print(thisdict.values())

#On your interpreter, create the dictionary for the data in this table. 
#Each name will be a key and year of birth will be the value
#Name-Year of birth,Cathy:2002,Mercy:2003,Grace:2004
#Add Rebecca born in 2005 to the dictionary
#Remove Mercy from the dictionary
information={"cathy":2000,"mercy":2003,
             "grace":2004}
information["rebecca"]=2005
print(information)
print(information.values())
del information["mercy"]
print(information)

#Write a Python program to combine two 
#dictionary by adding values for common keys.
from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300,'e':500}
d2 = {'a': 300, 'b': 200, 'd':400,'c':600}
d = Counter(d1) + Counter(d2)
print(d)

# Write a Python program to find the highest 3 
#values of corresponding keys in a dictionary.

from heapq import nlargest
my_dict = {'a':1000, 'b':5874, 'c': 5600,'d':4000, 'e':5874, 'f': 2000}  
three_largest = nlargest(3, my_dict, key=my_dict.get)
print(three_largest)



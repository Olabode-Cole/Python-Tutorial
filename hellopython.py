import random
import sys
import os

grocery_list = ['juice', 'Tomatoes', 'potatoes', 'Bananas']

print('First Item', grocery_list[0])

grocery_list[0] = "Green juice"
print('First Item', grocery_list[0])

print(grocery_list[1:3])

other_events = ['Wash Car', 'Pick Up Kids', 'Cash check']

music_song = ['Too much money out here', 'Pipe it up', 'The plug']


to_do_list =[other_events,grocery_list,music_song]
print(to_do_list)

print((to_do_list[1][1]))

grocery_list.append('Onions')
print(to_do_list)

grocery_list.insert(1, "pickle")

grocery_list.remove("pickle")

grocery_list.sort()

grocery_list.reverse()

del grocery_list[4]
print(to_do_list)

to_do_list2 = other_events + grocery_list

print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))

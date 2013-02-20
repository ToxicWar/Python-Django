# coding=utf-8
def my_shiny_new_decorator(func):
    def the_wrapper_around_the_original_function():
        print "Before the function runs"
        func()
        print "After the function runs"
    return the_wrapper_around_the_original_function

def a_stand_alone_function():
    print "I am a stand alone function, don't you dare modify me"

a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function_decorated()

def bread(func):
    def wrapper():
        print "</------\>"
        func()
        print "<\______/>"
    return wrapper
 
def ingredients(func):
    def wrapper():
        print "#tomatoes#"
        func()
        print "~salad~"
    return wrapper
 
def sandwich(food="--ham--"):
    print food
 
sandwich()
#print: --ham--

sandwich = bread(ingredients(sandwich))
sandwich()
#print:
# </------\>
# #tomatoes#
# --ham--
# ~salad~
# <\______/>

@bread
@ingredients
def sandwich2(food="-1chicken1-"):
    print food

sandwich2()
#print:
# </------\>
# #tomatoes#
# -1chicken1-
# ~salad~
# <\______/>
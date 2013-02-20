# coding=utf-8
def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2): # arguments arrive from here
        print "I got args! Look:", arg1, arg2
        function_to_decorate(arg1, arg2)
    return a_wrapper_accepting_arguments

@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print "My name is", first_name, last_name
 
print_full_name("Peter", "Venkman")
# outputs:
#I got args! Look: Peter Venkman
#My name is Peter Venkman

print "===================================="

# Decorators are ORDINARY functions
def my_decorator(func):
    print "I am a ordinary function"
    def wrapper():
        print "I am function returned by the decorator"
        func()
    return wrapper
 
# Therefor, you can call it without any "@"
 
def lazy_function():
    print "zzzzzzzz"
 
decorated_function = my_decorator(lazy_function)
#ouputs: I am a ordinary function

print "===================================="

decorated_function()
#I am function returned by the decorator
#zzzzzzzz

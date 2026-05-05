#Functions used in preparing Guido's gorgeous lasagna.
#This is a module docstring, used to describe the functionality
#of a module and its functions and/or classes.

#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.

EXPECTED_BAKE_TIME = 40 
PREPARATION_TIME = 2

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.

def bake_time_remaining(elapsed_bake_time):
    """ This returns remaining bake time in min """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


#TODO: Define the 'preparation_time_in_minutes()' function below.
def preparation_time_in_minutes(number_of_layers):
    """ this returns the preparation time in minutes based on layers """
    return number_of_layers * PREPARATION_TIME

#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):

    """ this returns the total time spent ( prep + baking"""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    


# TODO: Remember to go back and add docstrings to all your functions

#  (you can copy and then alter the one from bake_time_remaining.)
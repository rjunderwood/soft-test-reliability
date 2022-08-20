
import random 
from itertools import permutations


OPERATORS = ['*', '+', '-', '/']

#Target number of permutations for the program to generate 
NUMBER_OF_PERMUATIONS =15

class Permutation():

    a_operator = None 
    b_operator = None

    def __init__(self, a_operator, b_operator):
        self.a_operator = a_operator
        self.b_operator = b_operator 

    def get_a_operator(self):
        return self.a_operator 
        
    def get_b_operator(self):
        return self.b_operator 



class Permutations():

    permutations = [] 
    correct_permutation = None


    def __init__(self, correct_permutation):
        self.correct_permutation = correct_permutation
        self.create_alternative_permutations()


    # Generate the Alternative permutations
    def create_alternative_permutations(self): 
        
        print("Creating Permutations") 
        while len(self.permutations) < NUMBER_OF_PERMUATIONS:

            
            new_permutation = Permutation(OPERATORS[random.randrange(4)],OPERATORS[random.randrange(4)])
            #Check if this is a new permutation
            if not self.permuatation_not_exist(new_permutation):
                print(new_permutation.get_a_operator() + "  " +new_permutation.get_b_operator())
            
                self.permutations.append(new_permutation)

        print("Finished Creating Permutations")


    
    ##The new permutation is checked against the correct and the existing ones that were created 
        
    def permuatation_not_exist(self, new_permutation):
        
        exists=False 
        for permutation in self.permutations:
            if (permutation.get_a_operator() == new_permutation.get_a_operator()) and (permutation.get_b_operator() == new_permutation.get_b_operator()):
                exists=True 

        #Check that the permutation does not exist for the correct permuation
        if (self.correct_permutation.get_a_operator() == new_permutation.get_a_operator()) and (self.correct_permutation.get_b_operator() == new_permutation.get_b_operator()):
            exists=True 
        
        return exists 
            


    def get_permutations(self):
        return self.permutations

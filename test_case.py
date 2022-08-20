import operator 

class TestCase():

    a_operator = None
    b_operator = None 
    permutation_state = None 
    correct_state = None
    a_value = None
    b_value = None 

    correct_state_solution = None
    permutation_state_solution = []
    


    def __init__(self, correct_state, permutation_state, a_value, b_value):
        self.correct_state = correct_state 
        self.permutation_state = permutation_state
        self.a_value = a_value
        self.process_solutions() 

    

    def process_solutions(self): 
        #First get solution for the correct_state 
        for permutation in self.permutation_state:
            self.permutation_state_solution.append(self.calculate_solution(permutation))

        
    def calculate_solution(self, permutation): 
        #Calculate Solution 
        return ((self.a_value get_operator(permutation.get_a_operator()) self.b_value) get_operator(permutation.get_b_operator()) self.b_value)
    




def get_operator(operator_string):
    if operator_string == "+":
        return operator.add
    if operator_string == "-":
        return operator.sub
    if operator_string == "*":
        return operator.mul
    if operator_string == "-":
        return operator.truediv
        
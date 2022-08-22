
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
        self.b_value = b_value
        self.process_solutions() 
        self.correct_state_solution = self.calculate_solution(correct_state)


    

    def process_solutions(self): 
        #First get solution for the correct_state 
        for permutation in self.permutation_state:
            self.permutation_state_solution.append({"permutation":permutation, "result":self.calculate_solution(permutation)})

        
    def calculate_solution(self, permutation): 
  
        #Calculate Solution 
        line_1 = operate(permutation.get_a_operator(), self.a_value, self.b_value) 
        line_2 = operate(permutation.get_b_operator(), line_1, self.b_value)
        return line_2

    #None of the permutation C output matches the expected C output
    def satisfies_test_objective(self):
        for solution in self.permutation_state_solution:
            if solution['result'] == self.correct_state_solution:
                return False
        return True

    #Return the permutations that match the correct permutation result
    def get_matching_permutations(self):
        matches = [] 
        for solution in self.permutation_state_solution:
            if solution['result'] == self.correct_state_solution:
                matches.append(solution)
        return matches 

    def get_permutation_state_solution(self):
        return self.permutation_state_solution

    def get_correct_state_solution(self):
        return self.correct_state_solution

def operate(operator_string,val_1,val_2):
    if operator_string == "+":
        return operator.add(val_1, val_2)
    if operator_string == "-":
        return operator.sub(val_1, val_2) 
    if operator_string == "*":
        return operator.mul(val_1, val_2)
    if operator_string == "/":
        return operator.truediv(val_1, val_2)
        
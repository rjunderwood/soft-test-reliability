
###################
#Riley Underwood 
###################


from permutation import Permutation, Permutations
from test_case import TestCase
#Create the Test Permutation 


#Correct Permutation 
CORRECT_PERMUTATION = Permutation("-","*")
#Test Case
A_VALUE = 8
B_VALUE = 2

#Create Permutations
permutations = Permutations(CORRECT_PERMUTATION)


#Test Case
test_case = TestCase(CORRECT_PERMUTATION, permutations.get_permutations(), A_VALUE,B_VALUE)

#Print the expected / correct program output 
print("CORRECT SOLUTION")
correct_solution = test_case.get_correct_state_solution()
print("\nA = (A "+CORRECT_PERMUTATION.get_a_operator()+ " B)\n" +"C = A "+CORRECT_PERMUTATION.get_b_operator()+ " B")
print(correct_solution)


#Print the permutation solutions
print("\n\nPERMUTATION SOLUTIONS")
for solution in test_case.get_permutation_state_solution():
    soltution_permutation = solution['permutation']
    print("\nA = (A "+soltution_permutation.get_a_operator()+ " B)\n" +"C = A "+soltution_permutation.get_b_operator()+ " B")
    print(solution['result'])



#Print if satisfy test objective
print("\nTest CASE (A="+str(A_VALUE)+", B="+str(B_VALUE)+")\nSatisfactory : "+str(test_case.satisfies_test_objective()))


#If it is not a satisfactory test case then output the matching C solution permutations 
#Matching permutations from the test case. 
matching_permutations = test_case.get_matching_permutations()
for match in matching_permutations: 

    match_permutation = match['permutation'] 
    print("\n\nMATCH PERMUTATION:\n""A = (A "+match_permutation.get_a_operator()+ " B)\n" +"C = A "+match_permutation.get_b_operator()+ " B")
    print(match['result'])







from permutation import Permutation, Permutations
#Create the Test Permutation 


#Correct Permutation 
CORRECT_PERMUTATION = Permutation("-","*")
permutations = Permutations(CORRECT_PERMUTATION)

print("\n\nCORRECT PERMUTATION:\n""A = (A "+CORRECT_PERMUTATION.get_a_operator()+ " B)\n" +"C = A "+CORRECT_PERMUTATION.get_b_operator()+ " B\n\n")


print("\n\nINCORRECT :: \n---------------\n" + str(len(permutations.get_permutations())))

for permutation in permutations.get_permutations():

    print("A = (A "+permutation.get_a_operator()+ " B)")
    print("C = A "+permutation.get_b_operator()+ " B\n\n") 





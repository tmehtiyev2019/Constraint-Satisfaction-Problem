# Importing os module to change the working directory
import os

# Setting the new directory path
new_dir = "C:/Users/tmehd/OneDrive/Desktop/AI/Project2"

# Changing the working directory to the new directory path
os.chdir(new_dir)

# Opening the input file 'input.txt' and reading the lines
with open('input.txt') as f:
    inpt = f.readlines()


# Extracting the matrix from the input file lines
inpt_matrix=inpt[2:22]

# Replacing the empty cells with '0' in the matrix
inpt_matrix = [i.replace("  ", " 0 ") for i in inpt_matrix]

# Creating a list to store the sub-matrices
matrix = []

# Dividing the matrix into 5x4 sub-matrices
for j in range(0, len(inpt_matrix[0].split()), 4):
    a, b = 0, 4
    for k in range(5):
        start, end = j, j+4
        subresult = [inpt_matrix[i].strip().split()[start:end] for i in range(a, b) if i < len(inpt_matrix)]
        matrix.append(subresult)
        b += 4
        a += 4

# Creating empty dictionaries to store tile and flower constraints
tile_constraints={}
target_constraints={}

# Extracting tile constraints from the input file
for i in range(3):
    tile_constraints[inpt[23:25][1].strip('{|}|\n|').split(', ')[i].split('=')[0]]=int(inpt[23:25][1].strip('{|}|\n|').split(', ')[i].split('=')[1])

# Extracting target constraints from the input file
for line in inpt[27:31]:
    lines = line.strip('\n').split(':')
    target_constraints[int(lines[0])] = int(lines[1])


# Defining three different constraint functions for full block, outer block, and L-shape tile constraints
def full_block(input):
    count = {}
    count[1] = 0
    count[2] = 0 
    count[3] = 0
    count[4] = 0
    return count

def outer_block(input):
    count = {}
    count[1] = sum(sublist[1:3].count('1') for sublist in input[1:3])
    count[2] = sum(sublist[1:3].count('2') for sublist in input[1:3])
    count[3] = sum(sublist[1:3].count('3') for sublist in input[1:3])
    count[4] = sum(sublist[1:3].count('4') for sublist in input[1:3])
    return count

def l_shape(input):
    count = {}
    count[1] = sum(sublist[1:].count('1') for sublist in input[1:])
    count[2] = sum(sublist[1:].count('2') for sublist in input[1:])
    count[3] = sum(sublist[1:].count('3') for sublist in input[1:])
    count[4] = sum(sublist[1:].count('4') for sublist in input[1:])
    return count


# Creating an empty list to store the solution path
solution_path = []


def apply_function(funct, area):
    return funct(area)


# define a function dfs_csp that takes 4 arguments:
# position_number, cumulative_state, solution_path, and matrix
def dfs_csp(position_number, cumulative_state, solution_path, matrix):
    
    # check if the current position_number is equal to the length of the matrix
    if position_number == len(matrix):
        # if the current state satisfies the target constraints, return True
        if (target_constraints[1] - cumulative_state[1])==0 and (target_constraints[2] - cumulative_state[2])==0 and (target_constraints[3] - cumulative_state[3])==0 and (target_constraints[4] - cumulative_state[4])==0:            
            return True
        # otherwise, return False
        else:
            return False
    else:
        # Listing possible domain functions into domain list
        domain = [l_shape, outer_block, full_block]
        # Sorting the domain in the reverse order
        sorted_domain = sorted(domain, key=lambda f: len([v for v in f(matrix[position_number]).values() if v > 0]), reverse=False)
        # iterate through the possible functions to apply to the current state
        for function in sorted_domain:
            
            # append the name of the current function to the solution_path list
            solution_path.append(function.__name__)
            func=function(matrix[position_number])
            
            # create a temporary dictionary to hold the updated state of the flowers after applying the current function
            temporary_dict = {}
            # iterate through the dictionary returned by the current function applied to the current state
            for key in func:
                # if the current key exists in the cumulative_state dictionary, update the value in the temporary_dict by adding the value of the key in the current function
                if key in cumulative_state:
                    temporary_dict[key] = cumulative_state[key] + func[key]
            
            # check if the number of tiles used exceeds the allowed constraints, and remove the last element from solution_path and continue to the next iteration if so
            if (solution_path.count('l_shape') > int(tile_constraints['EL_SHAPE'])) or (solution_path.count('full_block') > int(tile_constraints['FULL_BLOCK'])) or  (solution_path.count('outer_block') > int(tile_constraints['OUTER_BOUNDARY'])):
                solution_path.pop()
                continue
            
            # check if the current state violates the target constraints, and remove the last element from solution_path and continue to the next iteration if so
            if (target_constraints[1] - cumulative_state[1])<0 or (target_constraints[2] - cumulative_state[2])<0 or (target_constraints[3] - cumulative_state[3])<0 or (target_constraints[4] - cumulative_state[4])<0:
                solution_path.pop()
                continue
            
            # update the current state with the new_generated_state
            new_generated_state = temporary_dict
            
            # recursively call dfs_csp with the next position_number, new_generated_state, solution_path, and matrix
            if dfs_csp(position_number + 1, new_generated_state, solution_path,  matrix):
                # if a solution is found, print the position_number, the state, the solution tile, and the flower color state
                print(' Position of the State :', position_number, 'State :', matrix[position_number], 'Solution Tile :', function.__name__, 'Flower Color state :', new_generated_state, '\n') 
                return True
            else:
                # if a solution is not found, remove the last element from solution_path and continue to the next iteration
                solution_path.pop()

        # if no solution is found for any function, return False
        return False


# Initialize the cumulative state and start the search with dfs_csp
cumulative_state={1:0, 2:0, 3:0, 4:0}
if dfs_csp(0, cumulative_state, solution_path, matrix):
    # If a solution is found, print the solution path
    print("Solution key:", solution_path)
else:
    # If no solution is found, print an error message
    print("No solution key was found ")

# Print the counts of tile usage
print('Tiles Used Counts :', solution_path.count('l_shape'), solution_path.count('full_block'), solution_path.count('outer_block'),'\n')


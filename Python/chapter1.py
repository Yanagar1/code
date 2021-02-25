import math

#-------------------------------------------------------------------------
def swap(lyst, pos1, pos2):
    tmp = lyst[pos1]
    lyst[pos1]=lyst[pos2]
    lyst[pos2]=tmp

#check if chars in the string don't repeat
# time: (N-1)+(N-2)+(N-3)..+ 1 = N(N-1)/2 => O(N^2), where N=len(string)
def isUnique(string):
    i=0
    while i!=(len(string)):
        for k in range(i+1, len(string)):
            if string[i]== string[k]:
                return False
        i+=1
    return True

'''
Hints:
#44: Try a hash table
#117: Could a bit vector be useful?
#132: Can you solve it in O(N log N)time? What might a solution like that look like?
Sol. p.192
'''
#Let's use python dictionaries (hash table) to improve my solution.
# Space: O(N) Time: O(N)?
def isUnique_2(string):
    chars = {}
    for char in string:
        if char in chars:
            return False
        else:
            x={char:1}
            chars.update(x)
            print(x)
    print(chars)
    print("true")
    return True
#I could use a list the same way. However, the question says to solve without additional data structures.


#-------------------------------------------------------------------------
#check if 2 strings are permutations of each other
def checkPermutation(str1, str2):
    if len(str1)==len(str2):
        str2list = list(str2)
        for char in str1:
            str2list.remove(char)
        if len(str2list) == 0:
            return True
    return False

'''
Hints: p.193
#84: There is one solution that is 0(N log N) time.
     Another solution uses some space, but is O(N) time.
#122: Could a hash table be useful?
#131: Two strings that are permutations should have the same characters, but in different orders.
    Can you make the orders the same?
'''
#-------------------------------------------------------------------------
#replace whitespace with %20
def urlify_w_replace(string):
    #requires re-assignment
    string = string.replace(" ", "%20")
    return string


#replace whitespace with %20 without using replace()
def urlify(string):
    output=""
    str_list = list(string)
    for i in range(len(string)):
        if string[i] == " ":
            str_list[i] = "%20"
    output = output.join(str_list)
    return output

'''
Hints: p.194
#53: It's often easiest to modify strings by going from the end of the string to the beginning.
#118: You might find you need to know the number of spaces. Can you just count them?
'''
#-------------------------------------------------------------------------
#find polindromes of a string
#This is what is wrong with my implementation:
#It exhausts all possible options then filters identical permutations: potentially extra work recreating the original string if it is already a palindrome, extra work if the same char occurs 4,6.. times.
#It removes spaces before deciding if a palindrome can exist => extra work
#It is brute-force-like, not an ingenious solution with long functions, many loops, lists, and variables.
#It is case-sensative and only functions for strings up to 7 non-space characters.
def palindrome_permutation(string):
    #remember the space locations
    space_loc = []
    str_list = list(string)
    for i in range(len(str_list)):
        if str_list[i] == " ":
            space_loc.append(i)
    #get rid of spaces
    for i in range(len(space_loc)):
        str_list.remove(" ")
    #check if we could make a polindrome
    # count # of char occur
    chars = []
    num_occur = []
    new_str_size = len(str_list)
    for char in str_list:
        if char not in chars:
            chars.append(char)
            num_occur.append(1)
        else:
            num_occur[chars.index(char)]+=1
    #check if # of occur is div by 2 or ∃ only 1 char not div by 2
    count = 0
    center_index = None #will use to create palindrome of odd length
    for index in range(len(num_occur)):
    	if num_occur[index]%2 != 0:
            count+=1
            center_index = index
    if count > 1:
        print("False")
        return False
    #create palindromes
    palindromes_list = [] #contains output

    for num in range(len(num_occur)):
        num_occur[num]=int(num_occur[num]/2)

    half_chars = []
    for ind in range(len(num_occur)):
        for i in range(num_occur[ind]):
            half_chars.append(chars[ind])

    size = len(half_chars)
    operations=0
    while operations<math.factorial(size):
        for i in range(size-1):
            swap(half_chars, i, i+1)
            operations+=1
            i+=1
            #local output
            palindrome = [None]*new_str_size
            #fill the center for odd length
            if center_index != None:
                palindrome[int((new_str_size)/2)] = chars[center_index]
            #insert permutation in first half of palindrome[] and fill by symmetry
            for charind in range(size):
                palindrome[charind] = half_chars[charind]
                palindrome[new_str_size-charind-1] = palindrome[charind]
        #insert spaces and convert to string
            for s in space_loc:
                palindrome.insert(s, " ")
            palindrome = "".join(palindrome)
            #check if solution already existed
            if palindrome not in palindromes_list:
                palindromes_list.append(palindrome)
    print("True, permutations: ", palindromes_list)
    return True

'''Hints: p.195
#106: You do not have to-and should not-generate all permutations. This would be very inefficient. I AGREE!!!(because I did =(    )
#121: What characteristics would a string that is a permutation of a palindrome have?
#134: Have you tried a hash table? You should be able to get this down to 0(N) time.
#136: Can you reduce the space usage by using a bit vector?
'''
#-------------------------------------------------------------------------
#check if 2 strings are 1 edit away: remove replace or insert
def one_way(str1, str2):
    length_coef = len(str1)-len(str2)
    if abs(length_coef)<=1:
        #make longer string str1
        if length_coef == -1:
            temp = str1
            str1 = str2
            str2 = temp
            length_coef = 1
        mistakes = 0
        j=0
        i=0
        while j < len(str2):
            if str1[i]!=str2[j]:
                mistakes+=1
                j-=length_coef
                if mistakes > 1:
                    return False
            j+=1
            i+=1
    else:
        return False
    return True

'''Hints: p.199
#130: Can you do all three checks in a single pass?
'''

#-------------------------------------------------------------------------
def str_compression(string):
    chars = []
    for char in string:
        if char not in chars:
            chars.append(char)
            chars.append(1)
        else:
            ind = chars.index(char)
            chars[ind+1]+=1
    print(chars)
    out = ""
    for i in chars:
        out += str(i)
    print(out)
    if len(out)<=len(string):
        return out
    print(string)
    return string


'''Hints: p.201
#110: Be careful that you aren't repeatedly concatenating strings together.
This can be very inefficient.
'''

#-------------------------------------------------------------------------
#rotate 90 degrees
def rotate_matrix(matrix):
    n = len(matrix[0])
    for square in range(int(n/2)):
        i=square
        for j in range(square, n-1-square):
            tmp = matrix[i][j]
            print(tmp)
            matrix[i][j]=matrix[j][n-1-i]
            matrix[j][n-1-i] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j]= matrix[n-1-j][i]
            matrix[n-1-j][i]=tmp

    print(matrix[0],'\n',matrix[1],'\n',matrix[2],'\n',matrix[3])
    return matrix

'''
Hints: p.203
#51: Try thinking about it layer by layer. Can you rotate a specific layer?
#100: Rotating a specific layer would just mean swapping the values in four arrays.
If you were asked to swap the values in two arrays, could you do this?
Can you then extend it to four arrays?
'''

#-------------------------------------------------------------------------
#if an element in an MxN matrix is 0, its entire row and column are set to 0.
def zero_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    make_zero_columns = set()
    non_zero_rows = []
	#find all zeros:
    for row in range(rows):
        if 0 in matrix[row]:
            print("row: ", row)
            for i in range(columns):
                if matrix[row][i] == 0:
                    make_zero_columns.add(i)
                    print("zero at: ", i)
                else:
                    matrix[row][i] = 0
        else:
            non_zero_rows.append(row)
    for j in make_zero_columns:
        for i in non_zero_rows:
            matrix[i][j] = 0
    print(matrix)
    return matrix

'''Hints: p.204
#74: Can you use O(N) additional space instead of O(N2)?
What information do you really need from the list of cells that are zero?
#102: You probably need some data storage to maintain a list of the rows and columns that need to be zeroed.
Can you reduce the additional space usage to 0(1)
by using the matrix itself for data storage?
'''

#-------------------------------------------------------------------------
#String Rotation: Assume you have a method isSubstring which
#checks if one word is a substring of another.
#Given two strings, s1 and s2, write code to check if s2 is a rotation
#of s1 using only one call to isSubstring (e.g.,"waterbottle" is a rotation of"erbottlewat").
#def string_rotation(s1, s2):
#    if len(s1)==len(s2) and isSubstring==True:
#        return True
'''String Rotation Hints
p. 206
#34: If a string is a rotation of another, then it's a rotation at a particular point.
For example, a rotation of waterbottle at character 3 means cutting waterbottle
at character 3 and putting the right half (erbottle) before the left half (wat).
#88: We are essentially asking if there's a way of splitting the first string into two parts,
x and y,such that the first string is xy and the second string is yx. Forexample,x = watand y = erbottle.
The first string is xy = waterbottle. The second string is yx = erbottlewat.
#104: Think about the earlier hint. Then think about what happens when you concatenate erbottlewat to itself.
You get erbottlewaterbottlewat.
'''


#-------------------------------------------------------------------------
#zero_matrix([["a",0,"c",0],["e","f","g","h"], ["i","j","k","l"],["m","n","o","p"]])
isUnique_2("abbdefg")

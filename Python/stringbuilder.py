import math
string1 = "abc def"
string2 = "cbafed"
list_of_strings = [string1, string2]

def swap(lyst, pos1, pos2):
    tmp = lyst[pos1]
    lyst[pos1]=lyst[pos2]
    lyst[pos2]=tmp

#practice syntax
def concat1():
    #print(string1+string2)
    #string1 += string2
    print(" ".join(list_of_strings))

#check if chars in the string don't repeat
def isUnique(string):
    i=0
    while i!=(len(string)):
        for k in range(i+1, len(string)):
            if string[i]== string[k]:
                return False
        i+=1
    return True

#check if 2 strings are permutations of each other
def checkPermutation(str1, str2):
    if len(str1)==len(str2):
        str2list = list(str2)
        for char in str1:
            str2list.remove(char)
        if len(str2list) == 0:
            return True
    return False

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

#find polindromes of a string
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

palindrome_permutation("tctc")

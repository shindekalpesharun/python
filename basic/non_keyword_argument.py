# Function definition is here
def printinfo( arg1, *vartuple ):
"This prints a variable passed arguments"
print ("Output is: ")
print (arg1)
for var in vartuple:
print (var)
return
# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )

#An asterisk (*) is placed before the variable name that holds the values of all nonkeyword
#variable arguments. This tuple remains empty if no additional arguments are specified
#during the function call. Following is a simple example-

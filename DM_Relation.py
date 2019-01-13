#Program to check if a relation on a set, satisfies some properties like
#reflexivity,irreflexivity, symmetry, asymmetry, anti-symmetry, transitivity &
#also conclude if it is an equivalence relation.

A=set()		#Create an empty set A so as to add the elements entered by the user into the set A.
b=int(input("Enter the no. of elements you want to enter in the set A:"))
print("Enter the elements of the set A:\n")
for i in range(b):
  c=(input())
  A.add(c)
print("\nThe set is :\n A = {}".format(A))

R=set()		#Create an empty set so as to add the ordered pairs entered by the users into the relation R.
c=int(input("\nHow many ordered pairs you wish to have in the relation R on the set A:"))
print("Enter {} ordered pairs:\n".format(c))
for j in range(c):
  e=(input(),input())	#Each entry of ordered pair in the relation will be a tuple so that we can perform indexing.
  print("\n")	
  if(e[0] in A and e[1] in A):	#condition to ensure that indivisual elements in the relation also belong to the set.
      R.add(e)
  else:
      print("This ordered pair cannot be considered in the relation!")
      print("Atleast one of the element in the ordered pair doesn't belong to the set.")
      exit()      
print("\nThe relation R on A you entered is:\n")
print("R = {}".format(R))

#Function to test for reflexivity
def reflexive(original_set,relation):
  ref = set()
  for x,y in relation:
    if (x == y):
      ref.add(x)
  if (ref == original_set):
    return True
  return False
    
#Function to test for irreflexivity   
def irreflexive(relation):
  count1=0
  for x,y in relation:
    if (x == y):
      count1+=1
  if (count1==0):
    return True
  return False

#Function to test for symmetry
def symmetry(relation):
    count2a=0
    for x1,x2 in relation:
      if (x2,x1) not in relation:
        count2a += 1
    if count2a > 0:
      return False
    return True

#Function to test for asymmetry
def asymmetry(relation):
    count2a=0
    count2b=0
    for x1,x2 in relation:
      count2a +=1
      if (x2,x1) not in relation:
        count2b += 1
    if count2a == count2b:
      return True
    return False

#Function to test for antisymmetry
def antisymmetry(relation):
    count2a=0
    count2c=0
    for x1,x2 in relation:
      count2a +=1
      if (x2,x1) in relation and (x1==x2):
        count2c += 1
    if count2c == count2a:
      return True
    return False


#Function to test for transitivity
def transitive(relation):
  count3 = 0
  for x1,x2 in relation:
    for x3,x4 in relation:
      if x2 == x3 and (x1,x4) not in relation:
        count3 +=1
  if count3 > 0:
    return False
  return True


eq_count=0 #counter used to check for equivalence relation
#Test for Reflexivity
if(reflexive(A,R)== True):
  print("The relation is Reflexive")
  eq_count+=1
else:
  print("The relation is Not Reflexive")


#Test for Irreflexivity
if(irreflexive(R)== True):
  print("The relation is Irreflexive")
else:
  print("The relation is Not Irreflexive")


#Test for Symmetry
if(symmetry(R)==True):
  print("The relation is Symmetric")
  eq_count += 1
else:
  print("The relation is Not Symmetric")

#Test for Asymmetry
if(asymmetry(R)==True):
  print("The relation is Asymmetric")
else:
  print("The relation is Not Asymmetric")


#Test for Antisymmetry
if(antisymmetry(R)==True):
   print("The relation is Antisymmetric")
else:
  print("The relation is Not Antisymmetric")


#Test for Transitivity
if(transitive(R)==False):
  print("The relation is Not Transitive")
else:
  print("The relation is Transitive")
  eq_count += 1


#Test for Equivalence Relation
if eq_count == 3:
  print("\nThe relation is an Equivalence Relation, as the relation is reflexive,symmetric & transitive.")
else:
  print("\nThe relation is Not an Equivalence relation.")
input("Press Enter to close")

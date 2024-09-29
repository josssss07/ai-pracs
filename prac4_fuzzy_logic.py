# make the 3 dicts that will be used for data and storing of the data 
A = dict()
B = dict()
X = dict()

#function for the union of the sets: 
def union(A, B):
    X.clear
    for A_key, B_key in zip(A, B):
        A_value = A[A_key]
        B_value = B[B_key]
    
        if A_value > B_value:
            X[A_key] = A_value
        else:
            X[B_key] = B_value

    return X

#function for the intersection of two fuzzy sets
def intersection(A, B):
    X.clear
    for A_key , B_key in zip(A, B):
        A_value = A[A_key]
        B_value = B[B_key]

        if A_value < B_value: 
            X[B_key] = B_value
        else: 
            X[A_key] = A_value
    return X

#function to compliment 
def compliment(A):
    for A_key in A:
        X[A_key] = 1- A[A_key]
    return X

#difference between two fuzzy sets 
def difference(A, B):
    for A_key, B_key in zip(A, B):
        A_value = A[A_key]
        B_value = B[B_key]
        B_value = 1 - B_value
        
        if A_value < B_value:
            X[A_key] = A_value
        else: 
            X[B_key] = B_value


#load up A and B with data
A = {"a": 0.2, "b": 0.3, "c": 0.6, "d": 0.6}
B = {"a": 0.9, "b": 0.9, "c": 0.4, "d": 0.5}

print(f'the first fuzzy set is: {A}')
print(f'the second fuzzy set is: {B}')


#fuzzy union of set A and B :
print("union set is: " , union(A, B) )


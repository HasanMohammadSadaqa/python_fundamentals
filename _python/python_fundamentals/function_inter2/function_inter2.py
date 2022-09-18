# 1)Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
x[1][0] = 15
students[0]["last_name"] = "Bryant"
sports_directory["soccer"][0] = "Andres"
z[0]["y"] = 30
print(x, students, sports_directory)


# 2)Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(some_list):
    for i in range(len(some_list)):
        for key, val in some_list[i].items():
            print(key, "-", val)
iterateDictionary(students)

# 3) Get Values From a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary2(key_name, some_list):
        for i in range(len(some_list)):
            for key, val in some_list[i].items():
                if key_name == key:
                    print(val)
iterateDictionary2('last_name', students)

# 4) Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def iterateDictionary(some_dic):
    for key in some_dic:
        print (len(some_dic[key]), key)
        for val in range(len (some_dic[key])):
            print(some_dic[key][val])
iterateDictionary(dojo)
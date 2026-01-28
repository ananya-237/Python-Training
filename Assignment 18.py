#1.Write a python program to create and print a dictionary which stores your information. 
d={'Name': 'Ananya', 'Age': 20, 'Gender':'Female'}
print(d)

#2.Write a python program to access the items of a dictionary by referring to its key 
d={'Name': 'Ananya', 'Age': 20 , 'Gender':'Female'}
print(d['Name'])
print(d['Age'])
print(d['Gender'])

#3.Write a python program to get a list of the values from a dictionary. 
for item in d:
    print(item,d[item], sep=' , ')

#4.Write a python program to change the value of a specific item by referring to its key 
d={'Name': 'Ananya', 'Age': 20, 'Gender':'Female'}
d['Name']= 'Ananya Katiyar'
print(d)

#5. Write a python program to print all key names in the dictionary, one by one.
d={'Name': 'Ananya', 'Age': 20, 'Gender':'Female'}
for key in d:
    print(key)

#6.Write a python program to create a dictionary that contains three dictionaries. 
person1 = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

person2 = {
    "name": "Bob",
    "age": 25,
    "city": "Los Angeles"
}

person3 = {
    "name": "Charlie",
    "age": 35,
    "city": "Chicago"
}
print(person1,person2,person3, sep='\n')

#7.Write a python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries.
person1 = {"name": "Alice","age": 30,"city": "New York"}

person2 = {"name": "Bob","age": 25,"city": "Los Angeles"}

person3 = {"name": "Charlie","age": 35,"city": "Chicago"}

person4 = {
    1: {"name": "Alice","age": 30,"city": "New York"},
    2: {"name": "Bob","age": 25,"city": "Los Angeles"},
    3: {"name": "Charlie","age": 35,"city": "Chicago"}

}
print(person1,person2,person3,person4, sep='\n')

#8.Write a python program to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value.
L1 = [100, 101, 102, 103] 
L2 = ['Ananya', 'Ruhi', 'Rahul', 'Raj'] 
d = {} 
x = 0 
while x < len(L1): 
    d[L1[x]] = L2[x] 
    x += 1 
for item in d: 
    print(item, d[item], sep=' = ') 

#9.Write a python program to merge two python dictionaries into one dictionary.
d1= {1:'Ananya',2:'Ruhi',3:'Rahul'}
d2= {4:'Raj',5:'Khushi', 6:'Tina'}
d1.update(d2)
print(d1)

#10.Write a python program to get the key of lowest value from the dictionary.
#sample_dict = { 'C': 92, 'Java': 66, 'Python': 85 }
sample_dict= { 'C': 92, 'Java': 66, 'Python': 85 }
print(min(sample_dict.values()))

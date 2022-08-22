from django.shortcuts import render

# Create your views here.

class Students:
    def __init__(self, name, age, classification, emerg, permanent_record  ):
        self.name = name
        self.age = age
        self.classification = classification
        self.emerg = emerg 

students = [
    Students('N. Johnson', '22', 'Sophmore', '234-665-2233'),
    Students('A. Davis', '21', 'Freshman', '478-593-1298'),
    Students('S. Mars', '20', 'Junior', '678-435-9743'),
    Students('L. Bennett', '24', 'Senior', '706-790-9919')
]
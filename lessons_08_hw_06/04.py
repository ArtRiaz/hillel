"""
list of group
of students by last name"""

def group_by_surname(list_of_enrolles):
   groups = {
       'A-I': 0,
       'J-P': 0,
       'Q-T': 0,
       'U-Z': 0

   }
   for i in list_of_enrolles:
       c = i.split()
       surname = c[-1]
       for group in groups:
           first_litter = group[0]
           second_litter = group[-1]
           if first_litter <= surname[0] <= second_litter:
               groups[group] += 1

   return groups


list_group = group_by_surname(['Will Smith', 'Jay Z', 'Ivan Ivanov', 'Petr Petrov', 'Garcia Marqes Vicario'])
print(list_group)
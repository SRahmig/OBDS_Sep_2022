#create list
participants = ['Dan', 'Felix', 'Judy', 'Ayesha', 'Yu', 'Kinam', 'Emily', 'Christina', 'Matt', 'Susann', 'Nicole', 'Li-Hsin']

#copy list
participants_2 = participants
participants_3 = participants.copy()

#append list
participants.append ('David')
participants.append ('Andrea')

#print all lists
print(participants)
print(participants_2)
print(participants_3)

#select 3rd and 5th name from list
print(participants[2:5:2])

#sort and select 3rd and 5th name from list
participants.sort()
participants[2:5]

#select first 2 letters of string in 3rd value of list
name = participants[2]
print(name[:2])

#Iterate over participants list
dic_participants={}
for name in participants:
    if name == 'David' or name == 'Andrea':
       dic_participants[name] = 'Trainer'
    else:
        dic_participants[name] = 'Trainee'
for name, value in dic_participants.items():
    print (f'{name} is {value}')

#print values of keys only for trainees
for name in dic_participants.keys():
    if dic_participants.get(name,0) == 'Trainee':
        print(name)
    #option 2
for name, value in dic_participants.items():
    if value == 'Trainee':
        print(name, value)

# tuple for participants
participants = ('Dan', 'Felix', 'Judy', 'Ayesha', 'Yu', 'Kinam', 'Emily', 'Christina', 'Matt', 'Susann', 'Nicole', 'Li-Hsin')
participants_2 = participants
participants_3 = participants.copy()
participants.append ('David')
participants.append ('Andrea')
print(participants)
print(participants_2)
print(participants_3)
print(participants[2:5:2])
participants.sort()
participants[2:5]
name = participants[2]
print(name[:2])
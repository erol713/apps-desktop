import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico':
     'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
    'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
for quiznum in range(35):
    quizfile=open('C:\\Users\\HP\\Desktop\\kvizovi\\kviz%s.txt' %(quiznum +1), 'w')
    answerfile=open('C:\\Users\\HP\\Desktop\\kvizovi\\odgovori%s.txt' %(quiznum +1), 'w')
    quizfile.write('Ime: \n\nDatum: \n\nSmjer: \n\n')
    quizfile.write((' ' * 20) + 'Kviz (Forma %s)' % (quiznum + 1))
    quizfile.write('\n\n')
    states=list(capitals.keys())
    random.shuffle(states)
    for questionnum in range(50):
        tacan= capitals[states[questionnum]]
        pogresan = list(capitals.values())
        del pogresan[pogresan.index(tacan)]
        pogresan = random.sample(pogresan, 3)
        opcije = pogresan + [tacan]
        random.shuffle(opcije)
        quizfile.write('%s. Koji je glavi grad %s?\n' %(questionnum +1, states[questionnum]))
        for i in range(4):
            quizfile.write('%s.) %s\n' %('ABCD'[i], opcije[i]))
        quizfile.write('\n')
        answerfile.write('%s.) %s\n' % (questionnum +1, 'ABCD'[opcije.index(tacan)]))
quizfile.close()
answerfile.close()



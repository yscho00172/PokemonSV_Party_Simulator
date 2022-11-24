# Pokemon SV Party Simulator
import sys
input = sys.stdin.readline

Type_Compatiblity = {
    'Normal' : [],
    'Fire' : ['Grass', 'Ice', 'Bug', 'Steel'],
    'Water' : ['Fire', 'Ground', 'Rock'],
    'Grass' : ['Water', 'Ground', 'Rock'],
    'Electric' : ['Water', 'Flying'],
    'Ice' : ['Grass','Ground','Flying','Dragon'],
    'Fighting' : ['Normal','Ice','Rock','Dark','Steel'],
    'Poison' : ['Grass','Fairy'],
    'Ground': ['Fire','Electric','Poison','Rock','Steel'],
    'Flying' : ['Grass','Fighting','Bug'],
    'Psychic' : ['Fighting','Poison'],
    'Bug' : ['Grass','Psychic','Dark'],
    'Rock' : ['Fire','Ice','Flying','Bug'],
    'Ghost' : ['Psychic','Ghost'],
    'Dragon' : ['Dragon'],
    'Dark' : ['Psychic','Ghost'],
    'Steel' : ['Ice','Rock','Fairy'],
    'Fairy' : ['Fighting','Dragon','Dark']
}
Result = {
    'Normal' : 0,
    'Fire' : 0,
    'Water' : 0,
    'Grass' : 0,
    'Electric' : 0,
    'Ice' : 0,
    'Fighting' : 0,
    'Poison' : 0,
    'Ground': 0,
    'Flying' : 0,
    'Psychic' : 0,
    'Bug' : 0,
    'Rock' : 0,
    'Ghost' : 0,
    'Dragon' : 0,
    'Dark' : 0,
    'Steel' : 0,
    'Fairy' : 0
}

Party_list = list(map(int,input().split()))

Party_list.sort()
Party_cnt = len(Party_list)

f = open("PokeDex.txt", "r")
num = 0
while 1:
    line = f.readline()
    if not line or int(line.split()[0]) > int(Party_list[-1]) or num > Party_cnt or int(Party_list[num]) > 400:
        break

    if Party_list[num] == int(line.split()[0]):
        num += 1
        if len(line.split()) == 2:
            for x in Type_Compatiblity[line.split()[1]]:
                Result[x] += 1
        else:
            for x in Type_Compatiblity[line.split()[1]]:
                Result[x] += 1
            for x in Type_Compatiblity[line.split()[2]]:
                Result[x] += 1

    elif Party_list[num] > int(line.split()[0]):
        continue


print(Result)
f.close()
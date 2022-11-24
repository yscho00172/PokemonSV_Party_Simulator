from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

from Pokemon_compare.models import Type_Compatibility, Pokemon_Dictionary

# Create your views here.
def index(request):
    return render(request, 'index.html')

def compare(request, pokemon_num):
    pokemon_dictionary = Pokemon_Dictionary.objects.all()
    compare_db = Type_Compatibility.objects.all()

    pokemon_type = pokemon_dictionary.filter(id=pokemon_num)

    type1 = pokemon_type.values()[0]['Type1']
    type2 = pokemon_type.values()[0]['Type2']

    if(type1 == 'None'):
        print("Error! Pokemon type is not found!")
    elif(type2 == 'None'):
        opposite = compare_db.filter(Type=type1)
        opposite_list_queryset = list(opposite.values())
        opposite_list = [opposite_list_queryset[i]['Opposite'] for i in range(len(opposite_list_queryset))]
        return JsonResponse({'pokemon_type': type1, 'opposite_types': opposite_list})
    else:
        opposite1 = compare_db.filter(Type=type1)
        opposite_list_queryset1 = list(opposite1.values())
        opposite_list1 = [opposite_list_queryset1[i]['Opposite'] for i in range(len(opposite_list_queryset1))]
        opposite2 = compare_db.filter(Type=type2)
        opposite_list_queryset2 = list(opposite2.values())
        opposite_list2 = [opposite_list_queryset2[i]['Opposite'] for i in range(len(opposite_list_queryset2))]
        return JsonResponse({'pokemon_type': type1 + ',' + type2, 'opposite_types': opposite_list1 + opposite_list2})

def pokemon_list(request):
    pokemon_dictionary = Pokemon_Dictionary.objects.all()

    return JsonResponse(list(pokemon_dictionary.values()), safe=False)

class pokemon(View):
    def get(self, request, pokemon_num):
        pokemon_dictionary = Pokemon_Dictionary.objects.all()

        pokemon_type = pokemon_dictionary.filter(id=pokemon_num)

        type1 = pokemon_type.values()[0]['Type1']
        type2 = pokemon_type.values()[0]['Type2']

        return JsonResponse({'type1': type1, 'type2': type2})

    def post(self, request, pokemon_type1, pokemon_type2):
        pokemon_dictionary = Pokemon_Dictionary.objects.all()

        new_pokemon = pokemon_dictionary.create(id=pokemon_dictionary.count() + 1, type1=pokemon_type1, type2=pokemon_type2)

        return JsonResponse({'pokemon_num': new_pokemon.pokemon_num, 'type1': new_pokemon.type1, 'type2': new_pokemon.type2})

    def put(self, request, pokemon_num, pokemon_type1, pokemon_type2):
        pokemon_dictionary = Pokemon_Dictionary.objects.all()

        update_pokemon = pokemon_dictionary.filter(id=pokemon_num).update(type1=pokemon_type1, type2=pokemon_type2)

        return JsonResponse({'pokemon_num': pokemon_num, 'type1': pokemon_type1, 'type2': pokemon_type2})

    def delete(self, request, pokemon_num):
        pokemon_dictionary = Pokemon_Dictionary.objects.all()

        delete_pokemon = pokemon_dictionary.filter(id=pokemon_num).delete()

        return JsonResponse({'pokemon_num': pokemon_num})
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python'] #list comprehention
    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi'] #list comprehention
    
    all_python_devs_name = list(filter(lambda worker: worker['language'] == 'python', DATA)) # Me devuelve los diccionarios con los desarrolladores de python
    all_python_devs_name = list(map(lambda worker: worker['name'], all_python_devs_name)) # se selecciona solo los nombres

    all_platzi_workers_name = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))# Filter, maps
    all_platzi_workers_name = list(map(lambda worker: worker['name'], all_platzi_workers_name))

    adults_name = [worker['name'] for worker in DATA if worker['age'] > 18] # edad con list comprehensions
    old_people_add = [worker | {'old': worker['age'] > 70} for worker in DATA] # old whith list comprehentios



    adults = list(filter(lambda worker: worker['age'] > 18 , DATA)) #High funtions -lambda
    adults = list(map(lambda worker: worker['name'], adults)) #High funtions -lambda, solo se toma el nombre
    
    old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70 }, DATA)) #arega una una key a DATA

    for worker in old_people_add:
        print(worker)
    

    


if __name__ == '__main__':
    run()

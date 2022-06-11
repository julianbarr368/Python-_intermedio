def run():
    my_list = [1, 'hello', True, 4.5 ]
    my_dict = {'firstname': 'Julian', 'lastname': 'Barragan'}

    super_list = [
        {'firstname': 'Julian', 'lastname': 'Barragan'},
        {'firstname': 'Jorge', 'lastname': 'Barragan'},
        {'firstname': 'Manuel', 'lastname': 'Barragan'},
        {'firstname': 'Diego', 'lastname': 'Barragan'},
        {'firstname': 'Myrian', 'lastname': 'Triana'},        
    ]

    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_nums': [-2, -1, 0, 1, 2],
        'floating_nums': [1.2, 2.5, 5.6, 9.8, 5.6]
    }

    for key, value in super_dict.items():
        print(key, '-', value)
    
    for i in super_list:
        for k, v in i.items():
            print(f'{k} = {v}')


if __name__ == '__main__':
    run()

def print_kwargs(**args):
    for key,value in args.items():
        print(f'{key}:{value}')



print_kwargs(name='poorna', power='brave')


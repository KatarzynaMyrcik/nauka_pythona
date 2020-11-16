def print_dict(dict):
    for key in dict:
        print("{0}:{1}".format(key, dict[key]))


# if __name__ == '__main__':
#     print('tu jestem')

samolot = {'n':'mig','przebieg':1220}
kuchnia = {'lodowka':'samsung','piec':'amica','garnki':'gerlach'
           
print(samolot)
print(type(samolot))
print_dict(samolot)
print_dict(kuchnia)

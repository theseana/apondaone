txt_str = 'Apondalakaka One!'
txt_list = list('Apondalakaka One!')
#['A', 'p', 'o', 'n', 'd', 'a', 'l', 'a', 'k', 'a', 'k', 'a', ' ', 'O', 'n', 'e', '!']
while txt_list:
    poped_element = txt_list.pop(0) 
    print(poped_element)
print(f"My list: {txt_list}")
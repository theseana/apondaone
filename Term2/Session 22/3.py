import string

print(string.punctuation)
txt = """
Deserunt, minim! fugiat^$ adipisi*&*cing mollit et proident. Id qui magna ad proident proident elit esse elit amet nostrud irure sit. In anim magna culpa nostrud. Elit qui commodo mollit Lorem nostrud esse labore sunt est officia sint. Enim incididunt anim fugiat tempor nisi culpa dolore est enim est occaecat magna tempor commodo.
"""
for word in txt.split():
    new_word = ''
    for character in word:
        if character in string.punctuatio+'1234567980':
            pass
        else:
            new_word += character 
    print(new_word.lower())
print ('''welcome,,,fill the blancks please''')

# def write_file():
#     with open('madlib_cli/template_Madlib.txt','w') as file:
#         file.write('''Make Me A Video Game!

#        I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}{A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!

#        What are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name's} Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find.''')
# write_file()

def read_template(path):
    try:
       with open(path,'r') as file:
         content=file.read()
         return content
    except FileNotFoundError:
        raise FileNotFoundError('no file found')
    
    


import re
def parse_template(text):
    words=[]
    replaced_word=re.findall(r'\{.*?\}',text)
    for str in replaced_word:
        words.append(str.strip("{}"))
    return (re.sub(r'{[^}]*}','{}',text)),tuple(words)
print(parse_template("It was a {Adjective} and {Adjective} {Noun}."))
    
def merge(text,words):
    return (re.sub(r'{[^}]*}','{}',text)).format(*words)





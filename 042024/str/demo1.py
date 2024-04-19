# Capitalize
text: str = "HELLO"
print(text.capitalize())

#casefold
text0: str = "MARio"
print(text0.casefold())

#count
text1: str = "sa_sat_saty_satya"
print(text1.count("sa"))

#Encode
text2: str = "Abdulkalam"
print(text2.encode(encoding='UTF-8',errors='strict'))

#endswith
text3: str = "banana"
print(text3.endswith('a'))
# we can use mutiple liek tuple
print(text3.endswith(('e','a')))

#Expandtabs
text4: str = 'text\ttext2\ttext3'
print(text4.expandtabs(20))

#find

text5: str = "comment unused values!"
position: int = text5.find('values')
print(position)
print(text5[position:])

text6: str = '-'
print(text6.join(['text1','text2','text3']))

text7: str = 'comment unused values!'
print(text7.replace('comment','uncomment'))
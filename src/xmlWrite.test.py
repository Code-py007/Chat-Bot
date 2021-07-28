# write to xml

number = input('Number: ')

for i in range(int(number)):
    with open('chat.aiml.xml', 'a') as f:

        Question = input('Question: ')
        if Question == 'end':
            quit()
        else:
            ans=input('Answer: ')
            f.write('\n<category>\n<pattern>' + Question +'</pattern>\n<template>'+ans+'</template>\n</category>\n')
            print('Written Succesfully!\n')

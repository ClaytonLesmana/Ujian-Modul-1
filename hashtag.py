def hashtag(string):
    if len(string) >140 or (string==''):
        return False
    else:
        x='#'
        capitalized=string.title() #capitalized every first letter in each word
        no_space=capitalized.replace(' ','') #remove space
        print(x+no_space)
    

hashtag('       Hello      world    ')
hashtag('Hello there how are you doing')
hashtag('')


# x=['Hello there how are you doing']
# hashtag=x.insert(0,'#')
# ''.join(hashtag)
# print(hashtag)
# capitalized=str1.title()
# no_space=capitalized.replace(' ','')
# print(no_space)
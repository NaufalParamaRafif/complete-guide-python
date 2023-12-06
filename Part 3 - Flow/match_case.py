# mood = 'sangkuriang'

# match mood:
#     case 'hungry':
#         print('eat something!')
#     case 'sleepy':
#         print('get some sleep!')
#     case 'thirsty':
#         print('get some water!')
#     case 'mager':
#         print('stop playing social media! or get some sleep!')
#     case _:
#         print('wtf this kind of mood do you have?')

print("====EXERCISE====")
grade = 1

match grade:
    case 1:
        print('very good very well!!!')
    case 2:
        print('good!')
    case 3:
        print('so so...')
    case 4:
        print('bad')
    case 5:
        print('very bad!')
    case _:
        print('wrong grade bruh!!!')
name='松田'

def change_name():
    global name
    name='浅木'
    print(name)

    def hello():
        print('こんにちは'+name+'さん')

        change_name()
        hello()

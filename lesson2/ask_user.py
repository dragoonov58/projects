def ask_user():
    faq = {
        'Как дела?' : 'Хорошо',
        'Что делаешь?' : 'Программироваю',
        'Как погода?' : 'Заебись'
    }
    while True:
        question = input('Введите свой вопрос   ')
        if question in faq:
            print(faq.get(question))
            break
        else:
            print('Давайте попробуем еще раз')

ask_user()

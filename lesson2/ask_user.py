def ask_user():
    faq = {
        'Как дела?' : 'Хорошо',
        'Что делаешь?' : 'Программироваю',
        'Как погода?' : 'Заебись'
    }
    try:
        while True:
            question = input('Введите свой вопрос   ')
            if question in faq:
                print(faq.get(question))
                break
            else:
                print('Давайте попробуем еще раз')
    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем. До свидания!")
ask_user()

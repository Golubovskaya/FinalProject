from main import MoviesLibrary

# Функция для тестирования одного жанра
def test_if_one():
    test_library = MoviesLibrary(['Комедия'])
    test_library.add_movie('Комедия', 'Большой Лебовски')
    result = test_library.recommend('Комедия')
    expected_result = ['Большой Лебовски']
    assert result == expected_result
    print(result)  # Вывод результата




# Функция для тестирования нескольких жанров
def test_if_many():
    test_library = MoviesLibrary(['Комедия', 'Боевик', 'Фентези'])
    test_library.add_movie('Комедия', 'Большой Лебовски')
    test_library.add_movie('Комедия', 'Эйс Вентура')
    test_library.add_movie('Боевик', 'Крепкий орешек')
    test_library.add_movie('Боевик', 'Пятый элемент')


    result = test_library.recommend('Боевик')
    expected_result = ['Крепкий орешек', 'Пятый элемент']
    assert result == expected_result
    print(result)  # Вывод результата


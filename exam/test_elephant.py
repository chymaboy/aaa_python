from exam.elephant import my_elephant


class TestClass:
    def test_attempts_limit(self):
        """
        Проверяем ответ в случае отказа купить слона
        """
        expected = 'Ну ты и жадина говядина. Не мог купить слона.'
        my_elephant.input = lambda x: 'no'
        actual = my_elephant.elephant()
        assert expected == actual

    def test_yes_answer(self):
        """
        Проверяем ответ в случае согласия купить слона
        """
        expected = 'Молодец! Теперь у тебя есть слон!'
        my_elephant.input = lambda x: 'yes'
        actual = my_elephant.elephant()
        assert expected == actual

    def test_output(self, capsys):
        """
        Тестируем вывод в консоль
        :return:
        """
        expected = 'Молодец! Теперь у тебя есть слон!\n'
        my_elephant.input = lambda x: 'yes'
        my_elephant.elephant()
        captured = capsys.readouterr()
        assert captured.out == expected

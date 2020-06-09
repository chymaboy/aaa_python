import click
from random import randint


@click.group()
def cli():
    pass


@cli.command()
@click.argument('attempts_limit', type=int, default=5)
def elephants(attempts_limit: int = 5):
    """
    Функция для запуска из командной строки.
    :param attempts_limit: Сколько раз спрашивает
    :return: Результат, купил или нет.
    """
    elephant(attempts_limit=attempts_limit)


def elephant(attempts_limit: int = 5):
    """
    Просит купить слона несколько раз, пока не получит положительный ответ "yes"
    :param attempts_limit: Сколько раз спрашивает
    :return: Результат, купил или нет.
    """
    questions = ['Все так говорят. А ты купи слона?\n', 'Ну купи слона?\n', 'Слабо купить слона?\n',
                 'Не будь жмотом. Купи слона?\n', 'Ну что, купишь слона?\n', 'Пожааалуйста, купи слона?\n']
    answer = ''
    attempt = 0
    while answer != 'yes' and attempt < attempts_limit:
        attempt += 1
        question = questions[randint(0, len(questions))-1]
        answer = input(question)
    if answer == 'yes':
        message = 'Молодец! Теперь у тебя есть слон!'
    else:
        message = 'Ну ты и жадина говядина. Не мог купить слона.'
    print(message)
    return message


if __name__ == '__main__':
    cli()

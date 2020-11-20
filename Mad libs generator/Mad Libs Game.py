# Mad Libs Random Story Generator

from random import randint
import copy

story = (
        "Today, every student has a computer small enough to fit into his {}." +
        "He can solve any math problem by simply pushing the computer's little {}." +
        "Computers can add, multiply, divide, and {}." +
        "They can also {} better than humans." +
        "Some computers are {}. " +
        "Others have a/an {} screen that shows all kinds of {} and {} figures"
)

words_dict = {
    "noun": ['bag', 'backpack', 'face'],
    "plural noun": ['button', 'pancake', 'pee pee', 'dreams', 'desires', 'people'],
    "verb (present tense)": ['build', 'bite', 'learn', 'search', 'help', 'teach'],
    "part of body (plural)": ['handier', 'brainy', 'stronger'],
    "adjective": ['flat', 'fierce', 'fresh', 'colorful', 'tiny', 'gigantic'],
}


def random_word(type, local_dict):
    words = local_dict[type]
    count = len(words) - 1
    index = randint(0, count)
    return local_dict[type].pop(index)


def create_function():
    local_dict = copy.deepcopy(words_dict)
    return story.format(
        random_word('noun', local_dict),
        random_word('plural noun', local_dict),
        random_word('verb (present tense)', local_dict),
        random_word('verb (present tense)', local_dict),
        random_word('part of body (plural)', local_dict),
        random_word('adjective', local_dict),
        random_word('plural noun', local_dict),
        random_word('adjective', local_dict)
    )


print("MAD LIBS GENERATOR!!!")
print(create_function())

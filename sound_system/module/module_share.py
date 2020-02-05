import os

from . import module_pico
from . import module_beep

import datetime

noise_words = []
file_path = os.path.abspath(__file__)
result_path = file_path.replace(
    'module/module_share.py', 'log/person-feature-{}.txt').format(str(datetime.datetime.now()))

# Speak the feature
def share(name, age, color):

    ###############
    #
    # use this module at find my mate section
    #
    # param >> name age color
    #
    # return >> 1
    #
    ###############

    # 「There is a {woman/man} at {place} in the party room.」
    sentence = "That is {}, {} years old, and hair color is {}.".format(name, age, color)
    module_beep.beep("stop")
    print(sentence)
    module_pico.speak(sentence)
    file = open(result_path, 'a')
    file.write(str(datetime.datetime.now()) + ": " + str(sentence) + "\n")
    file.write("--------------------------------------------------------------------\n")
    file.close()


if __name__ == '__main__':
    share("emma", "18", "red")

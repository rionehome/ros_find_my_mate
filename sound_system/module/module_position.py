import os

from . import module_pico
from . import module_beep

import datetime

file_path = os.path.abspath(__file__)
result_path = file_path.replace(
    'module/module_position.py', 'log/person-feature-{}.txt').format(str(datetime.datetime.now()))

# Speak the feature
def position(position):

    ###############
    #
    # use this module at find my mate section
    #
    # param >> position >> "sex|position"
    #
    # return >> 1
    #
    ###############

    position = position.split("|")
    sentence = "There is a {} at {} in the party room.".format(position[0], position[1])
    module_beep.beep("stop")
    print(sentence)
    module_pico.speak(sentence)
    file = open(result_path, 'a')
    file.write(str(datetime.datetime.now()) + ": " + str(sentence) + "\n")
    file.close()


if __name__ == '__main__':
    position("man|right corner")
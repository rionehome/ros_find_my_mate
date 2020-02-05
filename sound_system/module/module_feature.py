import os
from pocketsphinx import LiveSpeech, get_model_path

from . import module_pico
from . import module_beep

import datetime
from time import sleep

noise_words = []
file_path = os.path.abspath(__file__)

# pocketsphinx path
model_path = get_model_path()

# Define name path
name_dic_path = file_path.replace(
    'module/module_feature.py', 'dictionary/info_name.dict')
name_gram_path = file_path.replace(
    'module/module_feature.py', 'dictionary/info_name.gram')

# Define age path
age_dic_path = file_path.replace(
    'module/module_feature.py', 'dictionary/info_age.dict')
age_gram_path = file_path.replace(
    'module/module_feature.py', 'dictionary/info_age.gram')

# Define hair color path
color_dic_path = file_path.replace(
    'module/module_feature.py', 'dictionary/info_color.dict')
color_gram_path = file_path.replace(
    'module/module_feature.py', 'dictionary/info_color.gram')

# Define yes or no path
yes_no_dic_path = file_path.replace(
    'module/module_feature.py', 'dictionary/yes_no.dict')
yes_no_gram_path = file_path.replace(
    'module/module_feature.py', 'dictionary/yes_no.gram')

# log file
result_path = file_path.replace(
    'module/module_feature.py', 'log/feature-{}.txt').format(str(datetime.datetime.now()))

name = None
age = None
color = None

# Listen question, or speak the number of men and women
def feature(task):

    ###############
    #
    # use this module at find my mate section
    #
    # param >> (name or age or color)
    #
    # return >> name or age or hair color
    #
    ###############

    global noise_words
    global live_speech
    global name
    global age
    global color
    if task == "name":

        answer = "Welcome to our party! Let me know your name."
        print("\n---------------------------------\n", answer, "\n---------------------------------\n")
        module_pico.speak(answer)
        setup_live_speech(False, name_dic_path, name_gram_path, 1e-10)
        module_beep.beep("start")
        for question1 in live_speech:
            print("\n[*] PREASE SAY YOUR NAME ...")
            #print(question1)

            # Noise list
            noise_words = read_noise_word(name_gram_path)
            if str(question1) == "":
                pass
            elif str(question1) not in noise_words:
                file = open(result_path, 'a')
                file.write(str(datetime.datetime.now())+": "+str(question1)+"\n")
                file.close()
                pause()
                module_beep.beep("stop")
                print("\n-----------your name-----------\n",str(question1),"\n---------------------------------\n")
                name = str(question1).replace("my name is ","")
                sentence = "Are you " + str(name) + " ?"
                print("\n---------------------------------\n",sentence,"\n---------------------------------\n")

                # Ask yes-no question
                module_pico.speak(sentence)
                # Detect yes or no
                setup_live_speech(False, yes_no_dic_path, yes_no_gram_path, 1e-10)
                flag = True
                while flag:
                    module_beep.beep("start")
                    for question2 in live_speech:
                        print("\n[*] CONFIRM YOUR NAME ...")
                        #print(question2)

                        # Noise list
                        noise_words = read_noise_word(yes_no_gram_path)

                        if str(question2) not in noise_words:
                            file = open(result_path, 'a')
                            file.write(str(datetime.datetime.now())+": "+str(question2)+"\n")
                            file.close()

                            if str(question2) == "yes":

                                # Deside name
                                pause()
                                module_beep.beep("stop")
                                answer = "Sure, I understand your name is " + str(name) + "."
                                print("\n---------------------------------\n",answer,"\n---------------------------------\n")
                                module_pico.speak(answer)
                                return str(name)

                            elif str(question2) == "no":

                                # Fail, ask name one more time
                                pause()
                                module_beep.beep("stop")
                                answer = "Sorry, please tell me your name, again."
                                print("\n---------------------------------\n",answer,"\n---------------------------------\n")
                                module_pico.speak(answer)
                                module_beep.beep("start")
                                del (live_speech)
                                setup_live_speech(False, name_dic_path, name_gram_path, 1e-10)
                                noise_words = read_noise_word(name_gram_path)
                                flag = False
                                break


                            elif str(question2) == "please say again":

                                pause()
                                module_beep.beep("stop")
                                print("\n---------------------------------\n",sentence,"\n---------------------------------\n")
                                module_pico.speak(sentence)
                                module_beep.beep("start")
                                # Ask yes-no question to barman
                                del(live_speech)
                                setup_live_speech(False, yes_no_dic_path, yes_no_gram_path, 1e-10)
                                noise_words = read_noise_word(yes_no_gram_path)

                        # noise
                        else:
                            print(".*._noise_.*.")
                            print("\n[*] CONFIRM YOUR NAME ...")
                            pass

            # noise
            else:
                print(".*._noise_.*.")
                print("\n[*] PREASE SAY YOUR NAME ...")
                pass

    elif task == "age":
        answer = "How old are you?"
        print("\n---------------------------------\n", answer, "\n---------------------------------\n")
        module_pico.speak(answer)
        setup_live_speech(False, age_dic_path, age_gram_path, 1e-10)
        module_beep.beep("start")
        for question3 in live_speech:
            print("\n[*] PREASE SAY YOUR AGE ...")
            #print(question3)

            # Noise list
            noise_words = read_noise_word(age_gram_path)
            if str(question3) == "":
                pass
            elif str(question3) not in noise_words:
                file = open(result_path, 'a')
                file.write(str(datetime.datetime.now())+": "+str(question3)+"\n")
                file.close()
                pause()
                module_beep.beep("stop")
                print("\n-----------your age-----------\n",str(question3),"\n---------------------------------\n")
                age = str(question3).replace("i am ","").replace("i'm ","")
                sentence = "Are you " + str(age) + " ?"
                print("\n---------------------------------\n",sentence,"\n---------------------------------\n")

                # Ask yes-no question
                module_pico.speak(sentence)
                # Detect yes or no
                setup_live_speech(False, yes_no_dic_path, yes_no_gram_path, 1e-10)
                flag = True
                while flag:
                    module_beep.beep("start")
                    for question4 in live_speech:
                        print("\n[*] CONFIRM YOUR AGE ...")
                        #print(question4)

                        # Noise list
                        noise_words = read_noise_word(yes_no_gram_path)

                        if str(question4) not in noise_words:
                            file = open(result_path, 'a')
                            file.write(str(datetime.datetime.now())+": "+str(question4)+"\n")
                            file.close()

                            if str(question4) == "yes":

                                # Deside age
                                pause()
                                module_beep.beep("stop")
                                answer = "Sure, I understand you are " + str(age) + "."
                                print("\n---------------------------------\n",answer,"\n---------------------------------\n")
                                module_pico.speak(answer)
                                return str(age.replace(" years old",""))

                            elif str(question4) == "no":

                                # Fail, ask age one more time
                                pause()
                                module_beep.beep("stop")
                                answer = "Sorry, please tell me your age, again."
                                print("\n---------------------------------\n",answer,"\n---------------------------------\n")
                                module_pico.speak(answer)
                                module_beep.beep("start")
                                del (live_speech)
                                setup_live_speech(False, age_dic_path, age_gram_path, 1e-10)
                                noise_words = read_noise_word(age_gram_path)
                                flag = False
                                break


                            elif str(question4) == "please say again":

                                pause()
                                module_beep.beep("stop")
                                print("\n---------------------------------\n",sentence,"\n---------------------------------\n")
                                module_pico.speak(sentence)
                                module_beep.beep("start")
                                # Ask yes-no question to barman
                                del (live_speech)
                                setup_live_speech(False, yes_no_dic_path, yes_no_gram_path, 1e-10)
                                noise_words = read_noise_word(yes_no_gram_path)

                        # noise
                        else:
                            print(".*._noise_.*.")
                            print("\n[*] CONFIRM YOUR AGE ...")
                            pass

            # noise
            else:
                print(".*._noise_.*.")
                print("\n[*] PREASE SAY YOUR AGE ...")
                pass

    elif task == "color":
        answer = "Let me know your hair color."
        print("\n---------------------------------\n", answer, "\n---------------------------------\n")
        module_pico.speak(answer)
        setup_live_speech(False, color_dic_path, color_gram_path, 1e-10)
        module_beep.beep("start")
        for question5 in live_speech:
            print("\n[*] PREASE SAY YOUR COLOR ...")
            #print(question5)

            # Noise list
            noise_words = read_noise_word(color_gram_path)
            if str(question5) == "":
                pass
            elif str(question5) not in noise_words:
                file = open(result_path, 'a')
                file.write(str(datetime.datetime.now())+": "+str(question5)+"\n")
                file.close()
                pause()
                module_beep.beep("stop")
                print("\n-----------your color-----------\n",str(question5),"\n---------------------------------\n")
                color = str(question5).replace("my hair color is ","")
                sentence = "Is your hair color " + str(color) + " ?"
                print("\n---------------------------------\n",sentence,"\n---------------------------------\n")

                # Ask yes-no question
                module_pico.speak(sentence)
                # Detect yes or no
                setup_live_speech(False, yes_no_dic_path, yes_no_gram_path, 1e-10)
                flag = True
                while flag:
                    module_beep.beep("start")
                    for question6 in live_speech:
                        print("\n[*] CONFIRM YOUR COLOR ...")
                        #print(question6)

                        # Noise list
                        noise_words = read_noise_word(yes_no_gram_path)

                        if str(question6) not in noise_words:
                            file = open(result_path, 'a')
                            file.write(str(datetime.datetime.now())+": "+str(question6)+"\n")
                            file.close()

                            if str(question6) == "yes":

                                # Deside color
                                pause()
                                module_beep.beep("stop")
                                answer = "Sure, I understand your hair color is " + str(color) + "."
                                print("\n---------------------------------\n",answer,"\n---------------------------------\n")
                                module_pico.speak(answer)
                                return str(color)

                            elif str(question6) == "no":

                                # Fail, ask color one more time
                                pause()
                                module_beep.beep("stop")
                                answer = "Sorry, please tell me your color, again."
                                print("\n---------------------------------\n",answer,"\n---------------------------------\n")
                                module_pico.speak(answer)
                                module_beep.beep("start")
                                del (live_speech)
                                setup_live_speech(False, color_dic_path, color_gram_path, 1e-10)
                                noise_words = read_noise_word(color_gram_path)
                                flag = False
                                break


                            elif str(question6) == "please say again":

                                pause()
                                module_beep.beep("stop")
                                print("\n---------------------------------\n",sentence,"\n---------------------------------\n")
                                module_pico.speak(sentence)
                                module_beep.beep("start")
                                # Ask yes-no question to barman
                                del (live_speech)
                                setup_live_speech(False, yes_no_dic_path, yes_no_gram_path, 1e-10)
                                noise_words = read_noise_word(yes_no_gram_path)

                        # noise
                        else:
                            print(".*._noise_.*.")
                            print("\n[*] CONFIRM YOUR COLOR ...")
                            pass

            # noise
            else:
                print(".*._noise_.*.")
                print("\n[*] PREASE SAY YOUR color ...")
                pass

# Stop lecognition
def pause():

    ###############
    #
    # use this module to stop live speech
    #
    # param >> None
    #
    # return >> None
    #
    ###############

    global live_speech
    live_speech = LiveSpeech(no_search=True)


# Make noise list
def read_noise_word(gram_path):

    ###############
    #
    # use this module to put noise to list
    #
    # param >> gram_path: grammer's path which you want to read noises
    #
    # return >> words: list in noises
    #
    ###############

    words = []
    with open(gram_path) as f:
        for line in f.readlines():
            if "<noise>" not in line:
                continue
            if "<rule>" in line:
                continue
            line = line.replace("<noise>", "").replace(
                    " = ", "").replace("\n", "").replace(";", "")
            words = line.split(" | ")
    return words

# Setup livespeech
def setup_live_speech(lm, dict_path, jsgf_path, kws_threshold):

    ###############
    #
    # use this module to set live espeech parameter
    #
    # param >> lm: False >> means useing own dict and gram
    # param >> dict_path: ~.dict file's path
    # param >> jsgf_path: ~.gram file's path
    # param >> kws_threshold: mean's confidence (1e-○)
    #
    # return >> None
    #
    ###############

    global live_speech
    live_speech = LiveSpeech(lm=lm,
                             hmm=os.path.join(model_path, 'en-us'),
                             dic=dict_path,
                             jsgf=jsgf_path,
                             kws_threshold=kws_threshold)

if __name__ == '__main__':
    feature("name")

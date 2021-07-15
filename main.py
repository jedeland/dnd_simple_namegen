# This is a sample Python script.
import sqlite3

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def print_objective():
    print("This is a simple name generator using precompiled names!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':




    print_objective()
    conn = sqlite3.connect('names_merged_.db')
    try:
        console_running = True
        cur = conn.cursor()
        while console_running is True:
            print("Loading NPC options ...")

            single_culture = None
            while single_culture is None:
                try:
                    culture_arg = input("")
                    if culture_arg.lower() in yes_list:
                        print("Creating NPC's with the same culture")
                        single_culture = True
                    elif culture_arg.lower() in no_list:
                        print("Creating NPC's with different cultures")
                        single_culture = False
                    elif culture_arg.lower() in quit_list:
                        console_running = False
                    else:
                        print("There was an error, please ensure the input corresponds to yes or no")
                except:
                    print("There was an error, please ensure the input corresponds to yes or no")
    except Exception as e:
        print("Error occured {}".format(e))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

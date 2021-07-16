# This is a sample Python script.
import sqlite3

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def print_objective():
    print("This is a simple name generator using precompiled names!")

def get_npc_num():
    print("Type the number of NPC's you wish to create: ")
    npc_num = None
    while npc_num is None:
        try:
            num_arg = int(input(""))
            if str(num_arg).lower() in quit_list:
                npc_num = num_arg
                console_running = False
            elif num_arg >= 501 or num_arg <= 0:
                print(
                    "The program can only create between 1 and 100 npc's, please ensure you type a number between these two values, try again")
            else:
                return num_arg

        except:
            print("There was an error, please ensure the input is a valid whole number")
    return npc_num

def get_regions():
    africa = ["African", "Ethiopia"]
    arb_tag = ['Arabia', 'Armenia', 'Azerbaijan', 'Israel', 'Persian', 'Kazakhstan', 'Turkey']
    arabia = arb_tag
    asia = sorted(
        ['Philippines', 'China', 'India', 'Persian', 'Japan', 'Kazakhstan', 'Korea', 'Pakistani', 'Srilanka', 'Vietnam',
         "Hawaiian"])
    europe = sorted(
        ['Albania', 'Armenia', 'Austria', 'Azerbaijan', 'Balkan', 'Basque', 'Russia', 'Belgium', 'France', 'Bulgaria',
         'Celtic', 'Czech', 'Denmark', 'Dutch', 'East Frisia', 'England',
         'Estonia', 'Norway', 'Finland', 'Georgia', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Italy', 'Latin',
         'Latvia', 'Lithuania',
         'Luxembourg', 'Macedonia', 'Malta', 'Romania', 'Poland', 'Portugal', 'Scandinavian', 'Slavic', 'Slovakia',
         'Slovenia', 'Spain', 'Sweden', 'Swiss', 'Turkey', 'Ukraine'])

    fantasy = sorted(["Tiefling", "Half-Orc", "Halfling", "Gnome", "Elf", "Dwarf", "Dragonborn"])
    regions = {"African": africa, "Europe": europe, "Near East": arabia, "Asia": asia, "Experimental: Fantasy": fantasy}
    return regions
def get_npc(cur, num_npcs, nations):
    print("Taking random value from data, returning {0} NPC names from {1} culture group".format(num_npcs, nations))
    cur.execute("""SELECT name, tag FROM NAMES WHERE origin == ? AND tag != ? and tag == 'F' LIMIT ? """, (str(nations),str('N'), num_npcs/2))
    output_list_female = cur.fetchall()
    cur.execute("""SELECT name, tag FROM NAMES WHERE origin == ? AND tag != ? and tag == 'M' LIMIT ? """,
                (str(nations), str('N'), num_npcs / 2))
    output_list_male = cur.fetchall()
    output = output_list_male + output_list_female
    print(len(output))
    return output



def select_group(origin_list, regions):
    print("Please select the NPC('s) culture region")
    uncompleted = True
    while uncompleted:
        try:
            do_enum(regions)
            choice = int(input("Number: "))  # Ensures input is int
            dict_arg = origin_list[choice - 1]  # Lists start at 0
            regions_refined = regions.get(dict_arg)

            do_enum(regions_refined)
            choice = int(input("Number: "))
            selected_nation = regions_refined[choice - 1]
            uncompleted = False
            return selected_nation
        except:
            print("Please ensure your selection is a valid number")
def do_enum(args):
    for number, origin in enumerate(args, start=1): #cleaner that using enumerate constantly
        print(number, " ", origin)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    yes_list, no_list, quit_list = ["y", "yeh", "yes", "yep", "ye", ""], ["n", "no", "nah", "nope"], ["q", "quit", "exit"]

    region_selections = get_regions()

    print_objective()
    conn = sqlite3.connect('names_merged_.db')

    # conn.row_factory = sqlite3.Row
    try:
        console_running = True
        cur = conn.cursor()
        while console_running is True:
            print("Loading NPC options ...")
            number_npcs = get_npc_num()
            print("Number recieved")
            single_culture = None
            while single_culture is None:
                try:
                    print("Create NPC's with the same culture? [y/n] ")
                    culture_arg = input("")
                    if culture_arg.lower() in yes_list:
                        print("Creating NPC's with the same culture")
                        single_culture = True
                    elif culture_arg.lower() in no_list:
                        print("Creating NPC's with different cultures")
                        single_culture = False
                    elif culture_arg.lower() in quit_list:

                        console_running = False
                        break
                    else:
                        print("There was an error, please ensure the input corresponds to yes or no")
                except:
                    print("There was an error, please ensure the input corresponds to yes or no")
            origins_list = list(region_selections.keys())
            if single_culture is True or int(number_npcs) == 1:
                selected_nation = select_group(origins_list, region_selections)
                npc_group = get_npc(cur, number_npcs, selected_nation)
                print(npc_group)
                break

    except Exception as e:
        print("Error occured {}".format(e))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print("""
Grammar Rule:
 1.   S -> aSB
 2.   S -> b
 3.   B -> a
 4.   B -> bBa
""")

# index to move to next input in the list
i = 0

def match(t):
    """ function checks if an input string matches grammar terminals """
    global i

    if i >= len(rdata): # aba -> len(aba) = 3
        # terminate when moving to last index in the list
        return False

    elif rdata[i] == t:
        # when matching input by a terminal, move to next input and return true
        i += 1
        return True

    else:
        return False

def B():

    if match('a'): # rule 3
        pass
    elif match('b'): # rule 4
        B()
        if match('a'):
            pass
    else:
        pass


def S():
    # S -> aSB
    if match('a'): # rule 1
        S()
        B()
    elif match('b'): # rule 2
        pass
    else:
        pass

def check(data):
    """ function validates if the string is accepted or rejected """

    global i
    global rdata
    # aba ---> ['a', 'b', 'a']
    rdata = list(data)

    #print(rdata)

    S() # non terminal starting

    if i == len(rdata):
        print("\tStatus: Accepted!")
    else:
        print("\tStatus: Rejected!")

    print("No.of matches: ", i)

    # return to first element in next line
    i = 0

def read_from_file():
    """ function reads string per line from a file """

    file = open('read.txt', "r")

    lines = file.readlines()

    for line in lines:
        # remove '\n' from line
        line = line.rstrip('\n')

        print("=" * 30)
        print("String: ", line, end='')
        check(line)

    file.close()

def insert_string():
    """ function takes an input string from the user """
    global idata

    idata = input("Enter a String: ")

    check(idata)

    idata = "" # clear the buffer

def run():
    """ main function of the program """

    flag = True

    while flag:
        try:
            op = int(input("Select an option: \n1- Read_Strings_from_File\n2- Insert_your_String\n"))
        except:
            print("Wrong input..enter number in range 1-3")
            continue
        else:
            if op == 1:
                read_from_file()
            elif op == 2:
                insert_string()
            else:
                print("Program is terminated. . .")
                import sys
                sys.exit()

            answer = input("Want to try another option? Y/N")

            if answer in ['n', 'N', 'No', 'no']:
                flag = False

# program execution
run()




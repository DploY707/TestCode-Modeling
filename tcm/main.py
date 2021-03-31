import sys
from core.parser import tcmDir, tcmParser, tcmMethod
from core.model import tcmModel, tcmModeler, tcmCase
from utils.color import colors

def initialize(target_project) :
    td = tcmDir(target_project)
    td.parse_fileTree()

    tmr = tcmModeler()

    for pyFile in td.pyFileList :
        tp = tcmParser(pyFile)
        tp.read_file()
        tp.generate_tcmMethod_from_pyFile()

        tmr.add_tcmMethods(tp.tcmMethods)

    for i in range(len(tmr.tcmMethods) - 1) :
        method = tmr.tcmMethods[i]
        method.process()

    tmr.generate_testCases()

    return tcmModel(tmr.tcmCases)

def spawn() :
    logo = ""

    # TODO : make logo to spawn
    print(logo)

def print_menu() :
    menu_str = ""

    menu_str += "[1] : print test cases from the target project\n"
    menu_str += "[q] : quit this program\n"

    print(menu_str)

def get_command() :
    cmd = input(colors.BRIGHT_YELLOW + '$: ' + colors.END)
    print('')

    return cmd

def run_cli_interface(model) :
    while True :
        print_menu()

        task = get_command()

        if task == '1' :
            while True :
                model.show()
                
                print('\n=========================================================')
                print('    You can choose the CASE No. that you want to test')
                print('    If you want to go back just use \'q\' cmd')
                print('=========================================================\n')

                sub_task = get_command()
            
                if sub_task.isdigit() and int(sub_task) in range(len(model.tcmCaseList)) :
                    print(str(model.tcmCaseList[int(sub_task)]) + '\n')
                elif sub_task == 'q':
                    break
                else :
                    print(colors.RED + 'Invalid task ... , Please check your cmd\n' + colors.END)

        elif task == 'q' :
            break
        else :
            print(colors.RED + 'Invalid task ... , Please check your cmd\n' + colors.END)

if __name__ == '__main__' :
    spawn()

    TCM_MODEL = initialize(sys.argv[1])

    run_cli_interface(TCM_MODEL)

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

        tmr.add_tcmMethods(tp.get_methods())

    for i in range(len(tmr.tcmMethods) - 1) :
        method = tmr.tcmMethods[i]
        method.process()

    tmr.generate_testCases()

    return tcmModel(tmr.tcmCases)

def spawn() :
    logo = ""

    # TODO : make logo to spawn
    print(logo)

def get_command() :
    cmd = input(colors.BRIGHT_YELLOW + '$: ' + colors.END)
    print('')

    return cmd

def print_input_error_msg() :
    print(colors.RED + 'Invalid task ... , Please check your cmd\n' + colors.END)

def print_user_manual(phase) :
    print("")

    if phase == 0 :
        print("  [1] : print test cases from the target project")
        print("  [q] : quit this program\n")
    elif phase == 1 :
        print("  [1...N] : select the case No. that want to analyze")
        print("  [q] : go to previous phase\n")
    elif phase == 2 :
        print("  [r] : back trace selected testCase")
        print("  [q] : go to previous phase\n")
    else :
        print("")


def run_cli_interface(model) :
    while True :
        print_user_manual(0)
        cmd = get_command()

        if cmd == '1' :
            run_phase1_modelView(model)
        elif cmd == 'q' :
            break
        else :
            print_input_error_msg()

def run_phase1_modelView(model) :
    while True :
        model.show()

        print_user_manual(1)
        cmd = get_command()

        if cmd.isdigit() and int(cmd) in range(len(model.tcmCaseList)) :
            run_phase2_caseView(model.tcmCaseList[int(cmd)])
        elif cmd == 'q' :
            break
        else :
            print_input_error_msg()

def run_phase2_caseView(case) :
    while True :
        print(case)

        print_user_manual(2)
        cmd = get_command()

        if cmd == 'r' :
            run_phase3_traceView(case)
        elif cmd == 'q' :
            break
        else :
            print_input_error_msg()

def run_phase3_traceView(case) :
    print('Reporting . . . \n')

    for target in case.targetList :
        print(target)

    while True :
        cmd = get_command()

        if cmd == 'q' :
            break
        else :
            print_input_error_msg()
        
if __name__ == '__main__' :
    spawn()

    TCM_MODEL = initialize(sys.argv[1])

    run_cli_interface(TCM_MODEL)

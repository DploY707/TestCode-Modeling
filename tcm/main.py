import sys
from core.parser import tcmDir, tcmParser, tcmMethod
from core.model import tcmModel, tcmModeler, tcmCase

def main() :
    TARGET_PROJECT = sys.argv[1]

    td = tcmDir(TARGET_PROJECT)
    td.parse_fileTree()

    tmr = tcmModeler()

    for pyFile in td.pyFileList :
        tp = tcmParser(pyFile)
        tp.read_file()
        tp.generate_tcmMethod_from_pyFile()

        tmr.add_tcmMethods(tp.tcmMethods)

    for i in range(len(tmr.tcmMethods) - 1) :
        method = tmr.tcmMethods[i]
        print(str(i) + ” : ” + method.code)

if __name__ == ‘__main__’ :
    main()

from utils.color import colors

class tcmModel :
    def __init__(self, testCases) :
        self.tcmCaseList = testCases

    def show(self) :
        for i, tc in enumerate(self.tcmCaseList) :
            print('CASE ' + str(i) + ' : ' +  tc.name)

class tcmModeler :
    def __init__(self) :
        self.tcmMethods = list()
        self.tcmCases = list()
        self.banFilter = list()

        self.banFilter.append(' (')
        self.banFilter.append('print(')

    def add_tcmMethods(self, tmList) :
        self.tcmMethods += tmList

    def generate_testCases(self) :
        for method in self.tcmMethods :
            if method.name == 'main' :
                tc = tcmCase()

                tc.set_entrypoint(method)
                self.mediate_entrypoint_of_testCase(tc)

                tc.set_name()
                tc.set_description()

                tc.set_targetList(self.find_test_target(tc))

                self.tcmCases.append(tc)

    def mediate_entrypoint_of_testCase(self, testCase) :
        codes = testCase.entrypoint.code

        entryFlag = True

        callList = list()

        for line in codes :
            if '(' in line and 'print(' not in line :
                callList.append(line)

        if len(callList) == 1 :
            for call in callList :
                if '.' in call :
                    singleFlag = False
                    break

            if entryFlag :
                for method in self.tcmMethods :
                    if testCase.entrypoint.file == method.file :
                        if method.name == callList[0].split('(')[0].split(' ')[-1] :
                            testCase.set_entrypoint(method)

    def find_test_target(self, testCase) :
        codes = testCase.entrypoint.code
        
        targetList = list()

        for i, line in enumerate(codes) :
            # This condition is only for ROS
            if i == 0 :
                pass
            else :
                if '(' in line :
                    niLine = line.replace('  ','')

                    if ' (' in niLine or 'print(' in niLine or list(niLine)[0] == '#' or '()' in niLine :
                        pass
                    else :
                        target = 'line ' + str(i).zfill(2) + ' : ' + niLine
                        targetList.append(target)

        return targetList

class tcmCase :
    def __init__(self) :
        self.entrypoint = None
        self.name = ""
        self.description = ""
        self.targetList = list()

    def set_entrypoint(self, method) :
        self.entrypoint = method

    def set_name(self) :
        tm = self.entrypoint

        hi = tm.file.split('/')

        self.name = hi[len(hi) - 1].split('.')[0]

    def set_description(self) :
        # This works on only for ROS1
        f = open(self.entrypoint.file, 'r')

        for line in f.readlines() :
            if "## " in line :
                self.description += line.split('## ')[1].replace('\n', '').replace('. ', '.\n')

    def set_targetList(self, targetList) :
        self.targetList = targetList

    def __repr__(self) :
        case_info = ""

        case_info += colors.BRIGHT_GREEN + 'CASE NAME : ' + self.name + '\n' + colors.END
        
        if self.description :
            case_info += colors.BRIGHT_GREEN + 'Description : ' + self.description + '\n' + colors.END
        else :
            case_info += 'Description : -NULL-\n'

        if self.entrypoint is not None :
            case_info += '\n' + str(self.entrypoint)

        return case_info

    def __str__(self) :
        return self.__repr__()

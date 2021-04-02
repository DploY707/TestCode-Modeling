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

    def __repr__(self) :
        case_info = ""

        case_info += 'CASE NAME : ' + self.name + '\n'
        
        if self.description :
            case_info += 'Description : ' + self.description + '\n'
        else :
            case_info += 'Description : -NULL-\n'

        if self.entrypoint is not None :
            case_info += '\n' + str(self.entrypoint)

        return case_info

    def __str__(self) :
        return self.__repr__()

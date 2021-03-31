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
                tc.set_name()

                self.tcmCases.append(tc)

class tcmCase :
    def __init__(self) :
        self.entrypoint = None
        self.name = ""
        self.description = ""

    def set_entrypoint(self, method) :
        self.entrypoint = method

    def set_name(self) :
        tm = self.entrypoint

        hi = tm.file.split('/')

        self.name = hi[len(hi) - 1].split('.')[0]

    def __repr__(self) :
        case_info = ""

        case_info += 'CASE NAME : ' + self.name + '\n'

        if self.entrypoint is not None :
            case_info += '\n' + str(self.entrypoint)

        return case_info

    def __str__(self) :
        return self.__repr__()

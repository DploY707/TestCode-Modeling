class tcmModel :
    def __init__(self) :
        self.tcmCaseList = list()

class tcmModeler :
    def __init__(self) :
        self.tcmMethods = list()

    def add_tcmMethods(self, tmList) :
        self.tcmMethods += tmList

class tcmCase :
    def __init__(self) :
        self.source = None
        self.description = None

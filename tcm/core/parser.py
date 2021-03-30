import os

class tcmDir() :
    """
    Class that manage file tree
    """
    def __init__(self, root) :
        self.dirRoot = root
        self.pyFileList = list()

    def parse_fileTree(self) :
        for dirPath, dirNames, fileNames in os.walk(self.dirRoot) :
            for filename in fileNames :
                if ".py" in filename :
                    self.pyFileList.append(dirPath + "/" + filename)

    def __str__(self) :
        return "FileTree : " + self.dirRoot

    def __repr__(self) :
        print("TODO : print what?")

class tcmParser() :
    def __init__(self, pyFile) :
        self.file = pyFile
        self.contents = None
        self.tcmMethods = list()

    def read_file(self) :
        py = open(self.file, 'r')
        self.contents = py.readlines()

    def generate_tcmMethod_from_pyFile(self) :
        code = ""
        indent = ""
        methodFlag = False

        for line in self.contents :
            if len(line.split('def ')) > 1 :
                methodFlag = True
                indent = line.split('def ')[0]

                if code != "" :
                    self.tcmMethods.append(tcmMethod(self.file, code))
                    code = ""
                    indent = ""

            elif 'if __name__' in line :
                methodFlag = True
                indent = ""

                if code != "" :
                    self.tcmMethods.append(tcmMethod(self.file, code))
                    code = ""
                    indent = ""

            if methodFlag and indent in line :
                if indent != "" :
                    code += line.split(indent)[0]
                else :
                    code += line
        
        self.tcmMethods.append(tcmMethod(self.file, code + "\n"))

class tcmMethod :
    def __init__(self, pyfile, code) :
        self.file = pyfile
        self.code = code
        self.name = None
        self.args = list()
        self.comments = None
        self.description = None

    def set_name(self, name) :
        self.name = name

    def set_description(self, description) :
        self.description = description

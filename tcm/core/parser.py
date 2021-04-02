import os
from utils.color import colors

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

    def __repr__(self) :
        return "FileTree : " + self.dirRoot

    def __str__(self) :
        return self.__repr__()

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

                if code :
                    self.tcmMethods.append(tcmMethod(self.file, code))
                    code = ""
                    indent = ""

            elif 'if __name__' in line :
                methodFlag = True
                indent = ""

                if code :
                    self.tcmMethods.append(tcmMethod(self.file, code))
                    code = ""
                    indent = ""

            if methodFlag and indent in line :
                if indent != "" :
                    code += line.split(indent)[0]
                else :
                    code += line
        
        if code :
            self.tcmMethods.append(tcmMethod(self.file, code))

class tcmMethod :
    # TODO : have to remove the overlapping codes

    def __init__(self, pyfile, code) :
        self.file = pyfile
        self.code = code.split('\n')
        self.name = None
        self.args = list()
        self.comments = list()
        self.description = ""

    def set_name(self) :
        funcProto = self.code[0]

        if '__main__' in funcProto :
            self.name = "main"
        else :
            self.name = funcProto.split('def ')[1].split('(')[0]

    def set_args(self) :
        funcProto = self.code[0]

        if '__main__' in funcProto :
            self.args.append("void")
        else :
            self.args = funcProto.split('(')[1].split(')')[0].split(', ')
    
    def set_comments(self) :
        # TODO : Have to handle not only single line comment but also multi line comment
        for line in self.code :
            if '# ' in line :
                self.comments.append(line)

    def set_description(self, description) :
        self.description = description

    def process(self) :
        self.set_name()
        self.set_args()
        self.set_comments()

        # TODO : Make a logic to make description
        self.set_description('-NULL-')

    def __repr__(self) :
        meth_info = ""

        meth_info += '====================================================================================================\n'
        meth_info += 'file : ' + self.file + '\n'
        meth_info += 'name : ' + self.name + '\n'
        meth_info += 'args : ' + ' '.join(self.args) + '\n'
        meth_info += 'description : ' + self.description + '\n'

        if not self.comments :
            meth_info += "comments : -NULL-\n"
        else :
            meth_info += '\n[comments]\n' + '\n'.join(self.comments) + '\n'

        meth_info += '\n[code]\n' + '\n'.join(    self.code) + '\n'
        meth_info += '===================================================================================================='

        return meth_info
    
    def __str__(self) :
        return self.__repr__()

# TODO : have to implement to manage class info & dependencies between .py files and classes
class tcmClass :
    def __init__(self) :
        pass

class tcmDependency :
    def __init__(self) :
        pass

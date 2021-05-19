class Pycharm:
    def compile(self):
        print("compile using pycharm")
    def execute(self):
        print("execution using pycharm")
class Vscode:
    def compile(self):
        print("compile using Vscode")
    def execute(self):
        print("execution using Vscode")
class Programmer:
    def coding(self,ide):
        ide.compile()
        ide.execute()
pr=Programmer()
vsc=Vscode()
pr.coding(vsc)
py=Pycharm()
pr.coding(py)
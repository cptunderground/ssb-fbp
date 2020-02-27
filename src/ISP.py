from node import node

class ISP(node):
    def __init__(self, ID, log):
        super().__init__(ID, log)
        self.type = 'ISP'


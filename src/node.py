class node:
    def __init__(self, ID, log):
        self.ID = ID
        self.log = log
        self.peers = list()


class ISP(node):
    def __init__(self, ID, log):
        super().__init__(ID, log)
        self.type = 'ISP'

    def print(self):
        print(self.ID, self.log, self.peers, self.type)


class butt(node):
    def __init__(self, ID, log):
        super().__init__(ID, log)
        self.peers = None
        self.type = 'Butt'

    def print(self):
        print(self.ID, self.log, self.peers, self.type)

    def connect(self, ISP):
        if (self.peers != None):
            self.peers.remove(self.ID)
        self.peers = ISP.ID
        ISP.peers.append(self.ID)
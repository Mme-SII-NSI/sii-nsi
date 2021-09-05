class ActiviteDic:
    
    def __init__(self):
        self.devoirs = []
        self.autres = []

    def add(self, activite):
        if activite.estDevoir():
            if activite not in self.devoirs:
                self.devoirs.append(activite)
                self.devoirs.sort(key=str, reverse= True)
        else:
            if activite not in self.autres:
                self.autres.append(activite)
                self.autres.sort(key=str)

from .Check import Check

class Range:
    def __init__(self, points):
        self.checks = [Check(i) for i in range(0, points + 1)]

    def setNote(self, note):
        for check in self.checks:
            if check.index == note:
                check.checked = 'checked'
            else:
                check.checked = ''
class project(object):
    'A project, contains timesheets'

    version = '0.1'

    def __init__(self, sheets=[]):
        self.sheets = sheets

    def sheets(self):
        return self.sheets

    def add_tSheet(self, tSheet):
        self.sheets.append(tSheet)
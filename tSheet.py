class tSheet(object):
    'A time sheet for recording time worked on projects'

    version = '0.1'

    def __init__(self, name, project, start_date = None, end_date = None, hours = []):
        self.name = name
        self.project = project
        self.start_date = start_date
        self.end_date = end_date
        self.hours = hours

    def total_hours(self):
        return sum(self.hours)

    def add_hour(self, hour):
        self.hours.append(hour)

    def print_hours(self):
        for x in self.hours:
            print(str(x.date) + ": " + str(x.time_worked) + "\n")
import datetime

class StudySchedulePlanner:
    def __init__(self):
        self.schedule = []

    def add_subject(self, name, date, time, location):
        self.schedule.append({
            "name": name,
            "date": datetime.datetime.strptime(date, "%Y-%m-%d"),
            "time": time,
            "location": location
        })

    def display_schedule(self, start_date, end_date):
        for event in self.schedule:
            if start_date <= event["date"] <= end_date:
                print(f'{event["name"]} - {event["date"].strftime("%Y-%m-%d")} {event["time"]} at {event["location"]}')

    def filter_subjects_by_day(self, day):
        for event in self.schedule:
            if event["date"].strftime("%A") == day:
                print(f'{event["name"]} - {event["date"].strftime("%Y-%m-%d")} {event["time"]} at {event["location"]}')

    def filter_subjects_by_time(self, start_time, end_time):
        for event in self.schedule:
            event_time = datetime.datetime.strptime(event["time"], "%H:%M:%S").time()
            if start_time <= event_time <= end_time:
                print(f'{event["name"]} - {event["date"].strftime("%Y-%m-%d")} {event["time"]} at {event["location"]}')

    def update_subject(self, name, date, time, location):
        for event in self.schedule:
            if event["name"] == name and event["date"] == datetime.datetime.strptime(date, "%Y-%m-%d"):
                event["time"] = time
                event["location"] = location

    def remove_subject(self, name):
        self.schedule = [event for event in self.schedule if event["name"] != name]

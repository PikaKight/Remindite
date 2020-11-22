
from typing import List

class Remind:
    
    def add_category(self, reminder:dict, category):

        if category not in list(reminder.keys()):
            reminder[category] = []
            return reminder
        else: return f"{category} already exists"

    def add_reminder(self, reminder, category, remind, date):
       
        if remind not in reminder[category]:
            reminder[category].append({remind: date})
            return reminder
        else: return f"{remind} already exists"
    
    def rm_category(self, reminder, category):
        
        if category in list(reminder.keys()):
            reminder.pop(category)
            return reminder
        else: return f"{category} doesn't exists"

    def rm_reminder(self, reminder, category, remind, date):
        if remind in reminder[category]:
            for i in range(len(reminder[category])):
                if reminder[category][remind] ==  date:
                    del reminder[category][remind]
            return reminder
        else: return f"{remind} already exists"

    def change_date(self, reminder, category, remind, date):
        pass

    def sort_by_date(self):
        pass
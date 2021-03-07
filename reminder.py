
from typing import List
import datetime

class Remind:

    def add_category(self, reminder:dict, category):
        """This function will check if the category is there. If not, it will save the category of the reminder

        Args:
            reminder (dict): Stores the overall reminder
            category (string): The type of reminder

        Returns:
            The overall reminder or a string to tell user that it already exists
        """
        if category not in list(reminder.keys()):
            reminder[category] = []
            return reminder
        else: return f"{category} already exists"

    def add_reminder(self, reminder, category, remind, date):
        """Checks if the reminder exists. If not, it will save it in the appropriate category.

        Args:
            reminder (dict): Stores the overall reminder
            category (string): The type of reminder
            remind (string): What user wants to be reminded of
            date (datetime): the due date or date that will be reminded of

        Returns:
            The overall reminder or a string to tell user that it already exists
        """
        if remind not in reminder[category]:
            reminder[category].append({"remind": remind, "date":date})
            return reminder
        else: return f"{remind} already exists"
    
    def rm_category(self, reminder, category):
        """Checks if the category exists. If not, it will remove the category

        Args:
            reminder (dict): Stores the overall reminder
            category (string): The type of reminder that will be remove

        Returns:
            The overall reminder or a string to tell user that it doesn't exists
        """
        if category in list(reminder.keys()):
            reminder.pop(category)
            return reminder
        else: return f"{category} doesn't exists"

    def rm_reminder(self, reminder, category, remind, ):
        """Checks if the reminder exists. If not, it will remove the reminder

        Args:
            reminder (dict): Stores the overall reminder
            category (string): The type of reminder that will be remove
            remind (string): What reminder will be removed

        Returns:
            The overall reminder or a string to tell user that it doesn't exists
        """
        for i in range(len(reminder[category])):
            if reminder[category][i]["remind"] ==  remind:
                del reminder[category][i]
                return reminder
        return f"{remind} don't exists"

    def change_date(self, reminder, category, remind, new):
        """Will change the date of the given reminder

        Args:
            reminder (dict): Stores the overall reminder
            category (string): The type of reminder
            remind (string): What user wants to be reminded of
            new (datetime): new date

        Returns:
            The overall reminder
        """
        for i in range(len(reminder[category])):
            if reminder[category][i]["remind"] ==  remind:
                reminder[category][i]["date"] = new 
                return reminder






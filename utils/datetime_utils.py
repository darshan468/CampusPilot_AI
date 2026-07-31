from datetime import datetime


class DateTimeUtils:

    @staticmethod
    def get_today():
        return datetime.now().date()

    @staticmethod
    def get_current_datetime():
        return datetime.now()

    @staticmethod
    def get_current_time():
        return datetime.now().time()

    @staticmethod
    def get_greeting():

        hour = datetime.now().hour

        if hour < 12:
            return "☀️ Good Morning"

        elif hour < 17:
            return "🌤️ Good Afternoon"

        else:
            return "🌙 Good Evening"

    @staticmethod
    def days_remaining(exam_date):

        today = datetime.now().date()

        return (exam_date - today).days

    @staticmethod
    def format_date(date_value):

        return date_value.strftime("%d %B %Y")
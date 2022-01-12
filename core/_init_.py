import datetime

class SystemInfo:
    def _init_(self):
        pass
    
    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = "The time now is {} {}".format(now.hour, now.minute)
        return answer
    

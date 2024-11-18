'''
Factory Design pattern is used when we have defined hierarchy of classes and we want to delegate the tasks of object creation.
We can use this pattern when there is situation where based on some conditionals we want to generate objects.
Now in a large project this if condition can add complexity as well code duplication.
Example: We design a notification service where based on type of notification we generate object i.e. email, sms etc
'''

from abc import ABC, abstractmethod

class Notifications(ABC):
    @abstractmethod
    def sendNotification(self):
        pass

class SMSNotification(Notifications):
    def sendNotification(self):
        print(f"sending an SMS notification")

class EmailNotification(Notifications):
    def sendNotification(self):
        print(f"sending an Email notification")


class NotificationFactory:
    def getNotificationConn(channel):
        if channel == "sms":
            return SMSNotification()
        elif channel == "email":
            return EmailNotification()
        else:
            "unknown"
    

smsNotification = NotificationFactory.getNotificationConn("sms").sendNotification()
emailNotification = NotificationFactory.getNotificationConn("email").sendNotification()
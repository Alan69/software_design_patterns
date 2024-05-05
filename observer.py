# Subject class
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

# Observer interface
class Observer:
    def update(self, message):
        pass

# Concrete Observer classes
class EmailObserver(Observer):
    def update(self, message):
        print(f"Sending email notification: {message}")

class SMSObserver(Observer):
    def update(self, message):
        print(f"Sending SMS notification: {message}")

# Client code
if __name__ == "__main__":
    # Create subject
    subject = Subject()

    # Create observers
    email_observer = EmailObserver()
    sms_observer = SMSObserver()

    # Attach observers to the subject
    subject.attach(email_observer)
    subject.attach(sms_observer)

    # Notify observers
    subject.notify("State change in the system!")

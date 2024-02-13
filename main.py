import time 
from plyer import notification 
if __name__ == "__main__":
    notification.notify(
        title= "Drink Water",
        message="Make sure to stay hydrated and take a sip",
        app_icon="E:\\Python\\Water reminder\\icon.ico",
        timeout=10
    )
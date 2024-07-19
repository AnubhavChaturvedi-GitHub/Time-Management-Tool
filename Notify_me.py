import os
from winotify import Notification, audio
from os import getcwd

def Alert(Text):
    icon_path = fr"{getcwd()}\file (3).png"

    toast = Notification(
        app_id="Time Management Assistant Ai",
        title=Text,
        duration="long",
        icon=icon_path
    )

    toast.set_audio(audio.LoopingAlarm, loop=False)

    toast.show()

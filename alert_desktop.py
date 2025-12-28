from plyer import notification
from datetime import datetime

def send_desktop_alert(message, title="Smart Visitor Alert"):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notification.notify(
    title=title,
    message=f"{message}\nTime: {current_time}",
    timeout=15
)


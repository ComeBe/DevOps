import psutil


def monitor():

        cpu_percent = psutil.cpu_percent()
        mem_percent = psutil.virtual_memory().percent
        disk_percent = psutil.disk_usage('/').percent
        print(f"Your CPU is used in: {cpu_percent}%")
        print(f"Your RAM is used in: {mem_percent}%")
        print(f"Your DISK is used in: {disk_percent}%")
        if cpu_percent > 90:
            send_alert("High CPU usage!")

        if mem_percent > 90:
            send_alert("High memory usage!")

        if disk_percent > 80:
            send_alert("Low disk space!")




def send_alert(message):
    print("Alert:", message)


if __name__ == "__main__":
    monitor()

import psutil
import time
from time import sleep
import json


# or maybe https://docs.python.org/2/library/configparser.html
class Settings:
    def __init__(self):
        try:
            with open('config.json') as json_file:
                cfg = json.loads(json_file.read())
                self.scan_interval = cfg["scan_interval"]
                self.cpu_interval_threshold = cfg["cpu_interval_threshold"]
                self.cpu_load_threshold = cfg["cpu_load_threshold"]
                self.net_interval_threshold = cfg["net_interval_threshold"]
                self.net_load_threshold = cfg["net_load_threshold"]
        except ValueError as e:
            print('failure to read config.json')
            print(e)
            exit()


settings = Settings()


def net_usage(interval=1):  # change the inf variable according to the interface
    net_in, net_out = 0, 0

    ret = psutil.net_io_counters(pernic=True, nowrap=True)
    for key, value in ret.items():
        print(value)
        net_in -= value.bytes_recv
        net_out -= value.bytes_sent

    time.sleep(interval)
    ret = psutil.net_io_counters(pernic=True, nowrap=True)
    for key, value in ret.items():
        net_in += value.bytes_recv
        net_out += value.bytes_sent

    net_in = round(net_in / 1024 / 1024 / interval, 3)
    net_out = round(net_out / 1024 / 1024 / interval, 3)

    print(f"Current net-usage:\nIN: {net_in} MB/s, OUT: {net_out} MB/s")


def main():
    net_usage()

    low_cpu_intervals = low_net_intervals = 0
    cpu_load_threshold = 5
    cpu_interval_threshold = 10
    net_interval_threshold = 3
    net_load_threshold = 3

    #  When interval is 0.0 or None compares system CPU times elapsed since last call or module import, returning immediately.
    print(psutil.cpu_percent())

    # https://stackoverflow.com/questions/911856/detecting-idle-time-using-python

    while low_cpu_intervals < cpu_interval_threshold and low_net_intervals < net_interval_threshold:
        if psutil.cpu_percent() > cpu_load_threshold:
            low_cpu_intervals += 1
        else:
            low_cpu_intervals = 0
        print(low_cpu_intervals)
        sleep(1)

        # cpu_usage()
        # net_usage()

    print("shutdown")
    # os.system("shutdown /s /t 1")


if __name__ == '__main__':
    main()

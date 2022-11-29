import psutil
import time
from time import sleep
import json
import os


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
        except ValueError as e:
            print('failure to read config.json')
            print(e)
            exit()


settings = Settings()


def get_net_usage(interval=1):  # change the inf variable according to the interface
    net_in, net_out = 0, 0

    ret = psutil.net_io_counters(pernic=True, nowrap=True)
    for key, value in ret.items():
        net_in -= value.bytes_recv
        net_out -= value.bytes_sent

    time.sleep(interval)
    ret = psutil.net_io_counters(pernic=True, nowrap=True)
    for key, value in ret.items():
        net_in += value.bytes_recv
        net_out += value.bytes_sent

    net_in = round(net_in / 1024 / 1024 / interval, 3)
    net_out = round(net_out / 1024 / 1024 / interval, 3)

    # print(f"Current net-usage:\nIN: {net_in} MB/s, OUT: {net_out} MB/s")
    return net_in, net_out


def main():

    low_cpu_intervals = low_net_intervals = 0
    cpu_load_threshold = 5
    cpu_interval_threshold = 10
    net_load_threshold = 3
    # 0.61 MB/s
    # 0.01

    #  When interval is 0.0 or None compares system CPU times elapsed since last call or module import
    psutil.cpu_percent()

    while True:
        net_in, net_out = get_net_usage(1)
        if net_in < 0.02 or net_out < 0.01:
            low_net_intervals += 1
        else:
            low_net_intervals = 0
        print(psutil.cpu_percent())
        if psutil.cpu_percent() < cpu_load_threshold:
            low_cpu_intervals += 1
        else:
            low_cpu_intervals = 0

        if low_net_intervals > net_load_threshold and low_cpu_intervals > cpu_interval_threshold:
            # maybe make a popup prompts here
            os.system("shutdown /s /t 1")

        print(f"low_cpu_intervals {low_cpu_intervals} \n low_network {low_net_intervals}")
        sleep(1)


if __name__ == '__main__':
    main()

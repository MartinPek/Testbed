import psutil
import time
from time import sleep
from datetime import datetime as dt
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
                self.net_in_threshold = cfg["net_in_threshold"]
                self.net_out_threshold = cfg["net_out_threshold"]
                self.update_interval = cfg["update_interval"]
                # during this timeframe there is a sleep instead of a shutdown
                self.sleep_timefames = cfg["sleep_timeframes"]
        except ValueError as e:
            print('failure to read config.json')
            print(e)
            exit()
        if type(self.sleep_timefames) is not list:
            raise ValueError("sleep_timeframes must be a list of timeframes")


setts = Settings()


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

    net_in = round(net_in / 1024 / interval, 3)
    net_out = round(net_out / 1024 / interval, 3)

    print(f"Current net-usage:\nIN: {net_in} Kb/s, OUT: {net_out} Kb/s")
    return net_in, net_out


def main():

    low_cpu_intervals = low_net_intervals = 0
    # 0.61 MB/s
    # 0.01

    # When interval is 0.0 or None compares system CPU times elapsed since last call or module import
    psutil.cpu_percent()

    while True:
        net_in, net_out = get_net_usage(setts.update_interval)
        if net_in < setts.net_in_threshold or net_out < setts.net_out_threshold:
            low_net_intervals += 1
        else:
            low_net_intervals = 0
        print(psutil.cpu_percent())
        if psutil.cpu_percent() < setts.cpu_load_threshold:
            low_cpu_intervals += 1
        else:
            low_cpu_intervals = 0

        if True or low_net_intervals > setts.net_interval_threshold and low_cpu_intervals > setts.cpu_interval_threshold:
            # maybe make a popup prompts here
            now = dt.now()
            day_hour = now.hour + now.minute / 60

            for timeframe in setts.sleep_timefames:
                if timeframe[0] < day_hour < timeframe[1]:
                    os.system("timeout /t 1")
            os.system("shutdown /s /t 1")
            sleep(5)

        print(f"low_cpu_intervals {low_cpu_intervals} \n low_network_intervals {low_net_intervals}")


if __name__ == '__main__':
    main()
    sleep(5)

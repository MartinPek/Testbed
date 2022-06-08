import psutil
import time
from time import sleep


def net_usage(inf="Ethernet", interval=15):   #change the inf variable according to the interface
    net_stat = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
    net_in_1 = net_stat.bytes_recv
    net_out_1 = net_stat.bytes_sent
    time.sleep(interval)
    net_stat = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
    net_in_2 = net_stat.bytes_recv
    net_out_2 = net_stat.bytes_sent

    net_in = round((net_in_2 - net_in_1) / 1024 / 1024, 3)
    net_out = round((net_out_2 - net_out_1) / 1024 / 1024, 3)

    print(f"Current net-usage:\nIN: {net_in} MB/s, OUT: {net_out} MB/s")


def main():

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
        print( low_cpu_intervals )
        sleep(1)


        # cpu_usage()
        # net_usage()

    print("shutdown")


if __name__ == '__main__':
    main()
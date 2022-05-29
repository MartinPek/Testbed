import psutil
import time


#  When interval is 0.0 or None compares system CPU times elapsed since last call or module import, returning immediately.
print(psutil.cpu_percent(interval=1))


def net_usage(inf = "Ethernet"):   #change the inf variable according to the interface
    net_stat = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
    net_in_1 = net_stat.bytes_recv
    net_out_1 = net_stat.bytes_sent
    time.sleep(1)
    net_stat = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
    net_in_2 = net_stat.bytes_recv
    net_out_2 = net_stat.bytes_sent

    net_in = round((net_in_2 - net_in_1) / 1024 / 1024, 3)
    net_out = round((net_out_2 - net_out_1) / 1024 / 1024, 3)

    print(f"Current net-usage:\nIN: {net_in} MB/s, OUT: {net_out} MB/s")


def main():
    net_usage()


if __name__ == '__main__':
    main()
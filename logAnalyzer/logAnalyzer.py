from pathlib import Path
import re
import matplotlib.pyplot as plt
import numpy as np
import statistics
logDir = Path("/home/martin/ST arb eventlogs")

files = logDir.glob("*.log")

max = 0
min = 0


def main():
    file_count = 0
    attempts = 0
    results = []
    for file in files:
        print(file.name)
        f = open(file, "r")
        lines = f.readlines()
        attempts = 1
        for line in lines:
            if re.search('airlock_wrong', line):
                attempts += 1

        file_count += 1
        print(attempts)
        results.append(attempts)
        f.close()

    med = statistics.median(results)


    bin = 20
    plt.hist(results, histtype='barstacked', bins=bin, rwidth=0.7, range=(0, 20))
    plt.axvline(med, color='r')  # vertical
    plt.gca().set(title='Pod airlock riddle', xlabel='Attempts', ylabel="number of groups");
    plt.show()




if __name__ == '__main__':
    main()


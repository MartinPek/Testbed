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
    bins = []
    for file in files:
        print(file.name)
        f = open(file, "r")
        lines = f.readlines()
        attempts = 1
        for line in lines:
            if re.search('airlock_wrong', line):
                attempts += 1

        file_count += 1
        if attempts not in bins:
            bins.append(attempts)
        print(attempts)
        results.append(attempts)
        f.close()

    med = statistics.median(results)
    results, counts = np.unique(results, return_counts=True)
    print(results)
    print(counts)
    print(file_count)

    fig, ax = plt.subplots(gridspec_kw={})
    # plt.hist(results, histtype='barstacked', bins=bins, rwidth=0.7)
    # plt.axvline(med, color='r')  # vertical
    ax.bar(results, counts, width=0.7, linewidth=0.7)
    ax.set(xlim=(0 ,21), xticks=range(0,21),
           ylim=(0, 12))
    plt.axvline(x=med, color='r', label="median")
    plt.grid()
    plt.gca().set(title=f'Pod airlock riddle from {file_count} games', xlabel='Attempts', ylabel="number of groups")
    plt.show()


if __name__ == '__main__':
    main()


#!/bin/python3.9

import sys
import matplotlib.pyplot as plot


def parse(filename, fieldNum):
    time = []
    field = []
    with open(filename) as file:
        for line in file:
            fields = line.split(",")
            time.append(float(fields[0]))
            field.append(float(fields[fieldNum]))
    return time, field


def main(args):
    # cpu metrics
    for i in range(6):
        ip1 = i + 1
        time, cpu = parse(f"./metrics/APM{ip1}_metrics.csv", 1)
        print(f"[!] Parsed APM {ip1} cpu utilization")
        color = ""
        match ip1:
            case 1:
                color = "blue"
            case 2:
                color = "black"
            case 3:
                color = "red"
            case 4:
                color = "green"
            case 5:
                color = "yellow"
            case 6:
                color = "cyan"
        plot.plot(time, cpu, label=f"APM {ip1}", color=color)
    plot.legend(loc="upper right")
    plot.title("APM CPU Utilization")
    plot.xlabel("Time (seconds)")
    plot.ylabel("CPU Utilization (%)")
    plot.savefig("./graphs/cpu.png")
    print(f"[!] Saved plot as \"cpu.png\"\n")
    plot.clf()

    # mem metrics
    for i in range(6):
        ip1 = i + 1
        time, mem = parse(f"./metrics/APM{ip1}_metrics.csv", 2)
        print(f"[!] Parsed APM {ip1} memory utilization")
        color = ""
        match ip1:
            case 1:
                color = "blue"
            case 2:
                color = "black"
            case 3:
                color = "red"
            case 4:
                color = "green"
            case 5:
                color = "yellow"
            case 6:
                color = "cyan"
        plot.plot(time, mem, label=f"APM {ip1}", color=color)
    plot.legend(loc="upper right")
    plot.title(f"APM Memory Utilization")
    plot.xlabel("Time (seconds)")
    plot.ylabel("Memory Utilization (%)")
    plot.savefig("./graphs/memory.png")
    print(f"[!] Saved plot as \"memory.png\"\n")
    plot.clf()

    # bandwidth
    time, data = parse("./metrics/system_metrics.csv", 1)
    time2, data2 = parse("./metrics/system_metrics.csv", 2)
    plot.plot(time, data, label="Rx Data Rate")
    print("[!] Parsed system Rx data")
    plot.plot(time2, data2, label="Tx Data Rate")
    print("[!] Parsed system Tx data")
    plot.title("Network Bandwidth Utilization")
    plot.xlabel("Time (seconds)")
    plot.ylabel("Data Rate (KB/s)")
    plot.legend(loc="upper right")
    plot.savefig("./graphs/bandwidth.png")
    print("[!] Saved plot as \"bandwidth.png\"\n")
    plot.clf()

    # disk access
    time, data = parse("./metrics/system_metrics.csv", 3)
    print("[!] Parsed system disk access rate data")
    plot.plot(time, data)
    plot.title("Hard Disk Access Rate")
    plot.xlabel("Time (seconds)")
    plot.ylabel("Disk Writes (KB/s)")
    plot.savefig("./graphs/disk_access.png")
    print("[!] Saved plot as \"disk_access.png\"\n")
    plot.clf()

    # disk util
    time, data = parse("./metrics/system_metrics.csv", 4)
    print("[!] Parsed system disk utilization data")
    plot.plot(time, data)
    plot.title("Hard Disk Utilization")
    plot.xlabel("Time (seconds)")
    plot.ylabel("Disk Capacity (MB)")
    plot.savefig("./graphs/disk_util.png")
    print("[!] Saved plot as \"disk_util.png\"\n")
    plot.clf()


if __name__ == "__main__":
    main(sys.argv)

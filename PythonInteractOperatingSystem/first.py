import shutil
import psutil

def chech_disk_usage(disk):
    du=shutil.disk_usage(disk)
    free=du.free / du.total * 100
    return free >20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75




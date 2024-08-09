#!/usr/bin/env python3
#Author: Jemark Amon
#Author ID: jamon@myseneca.ca

import argparse
import os

def parse_command_args() -> object:
    "Set up argparse here. Call this function inside main."

    parser = argparse.ArgumentParser(description="Memory Visualiser -- See Memory Usage Report with bar charts", epilog="Copyright 2023")
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")
    parser.add_argument("-H", "--human-readable", action="store_true", help="Display memory usage in human-readable format.")
    parser.add_argument("program", type=str, nargs='?', help="If a program is specified, show memory use of all associated processes. Show only total use if not.")
    args = parser.parse_args()
    return args

def percent_to_graph(percent: float, length: int=20) -> str:
    "Turns a percent 0.0 - 1.0 into a bar graph"
    num_hashes = int(percent * length)
    num_spaces = length - num_hashes
    return f"{'#' * num_hashes}{' ' * num_spaces}"

def get_sys_mem() -> int:
    "Return total system memory in kB"
    with open('/proc/meminfo', 'r') as f:
        for line in f:
            if 'MemTotal:' in line:
                return int(line.split()[1])
    return 0

def get_avail_mem() -> int:
    "Return available memory in kB"
    with open('/proc/meminfo', 'r') as f:
        mem_free = 0
        mem_available = 0
        swap_free = 0
        for line in f:
            if 'MemAvailable:' in line:
                mem_available = int(line.split()[1])
            elif 'MemFree:' in line:
                mem_free = int(line.split()[1])
            elif 'SwapFree:' in line:
                swap_free = int(line.split()[1])
        
        if mem_available:
            return mem_available
        return mem_free + swap_free

def pids_of_prog(app_name: str) -> list:
    "Given an app name, return all PIDs associated with app"
    pids = os.popen(f'pidof {app_name}').read().strip()
    return pids.split() if pids else []

def rss_mem_of_pid(proc_id: str) -> int:
    "Given a process ID, return the Resident memory used"
    try:
        with open(f'/proc/{proc_id}/smaps', 'r') as f:
            rss = 0
            for line in f:
                if 'Rss:' in line:
                    rss += int(line.split()[1])
            return rss
    except FileNotFoundError:
        return 0

def bytes_to_human_r(kibibytes: int, decimal_places: int=2) -> str:
    "Turn 1,024 into 1 MiB, for example"
    suffixes = ['KiB', 'MiB', 'GiB', 'TiB', 'PiB'] # iB indicates 1024
    suf_count = 0
    result = kibibytes 
    while result > 1024 and suf_count < len(suffixes):
      result /= 1024
      suf_count += 1
    str_result = f'{result:.{decimal_places}f} '
    str_result += suffixes[suf_count]
    return str_result

def parse_command_args() -> object:
    "Set up argparse here. Call this function inside main."

    parser = argparse.ArgumentParser(description="Memory Visualiser -- See Memory Usage Report with bar charts", epilog="Copyright 2023")
    parser.add_argument("-H", "--human-readable", action="store_true", help="Prints sizes in human readable format")
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")
    parser.add_argument("program", type=str, nargs='?', help="If a program is specified, show memory use of all associated processes. Show only total use if not.")
    
    args = parser.parse_args()
    return args

def pids_of_prog(app_name: str) -> list:
    "Given an app name, return all PIDs associated with app"
    pids = os.popen(f'pidof {app_name}').read().strip()
    return pids.split() if pids else []

def rss_mem_of_pid(proc_id: str) -> int:
    "Given a process ID, return the Resident memory used"
    try:
        with open(f'/proc/{proc_id}/smaps', 'r') as f:
            rss = 0
            for line in f:
                if 'Rss:' in line:
                    rss += int(line.split()[1])
            return rss
    except FileNotFoundError:
        return 0
    
if __name__ == "__main__":
    args = parse_command_args()

    total_mem = get_sys_mem()
    avail_mem = get_avail_mem()
    used_mem = total_mem - avail_mem
    used_percent = used_mem / total_mem

    if not args.program:  # No program name specified.
        human_total = bytes_to_human_r(total_mem) if args.human_readable else f"{total_mem}"
        human_used = bytes_to_human_r(used_mem) if args.human_readable else f"{used_mem}"
        percent = int(used_percent * 100)
        graph = percent_to_graph(used_percent, args.length)
        print(f"Memory         [{graph}| {percent}%] {human_used}/{human_total}")

    else:  # Program name specified.
        pids = pids_of_prog(args.program)
        if not pids:
            print(f"{args.program} not found.")
        else:
            total_program_mem = 0
            for pid in pids:
                rss = rss_mem_of_pid(pid)
                total_program_mem += rss
                percent = rss / total_mem
                human_rss = bytes_to_human_r(rss) if args.human_readable else f"{rss}"
                human_total_mem = bytes_to_human_r(total_mem) if args.human_readable else f"{total_mem}"
                graph = percent_to_graph(percent, args.length)
                print(f"{pid:<10} [{graph}| {int(percent * 100)}%] {human_rss}/{human_total_mem}")
            
            if args.human_readable:
                human_total_program_mem = bytes_to_human_r(total_program_mem)
            else:
                human_total_program_mem = f"{total_program_mem}"
            print(f"{args.program:<10} [{percent_to_graph(total_program_mem / total_mem, args.length)}| {int((total_program_mem / total_mem) * 100)}%] {human_total_program_mem}/{total_mem}")

#!/usr/bin/env python3
#Author: Jemark Amon
#Author ID: jamon@myseneca.ca

import argparse
import os

def parse_command_args() -> object:
    "Set up argparse here. Call this function inside main."

    parser = argparse.ArgumentParser(description="Memory Visualiser -- See Memory Usage Report with bar charts", epilog="Copyright 2023")
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")

    # Add an optional flag for displaying memory usage in a human-readable format
    parser.add_argument("-H", "--human-readable", action="store_true", help="Display memory usage in human-readable format.")

    parser.add_argument("program", type=str, nargs='?', help="If a program is specified, show memory use of all associated processes. Show only total use if not.")
    args = parser.parse_args()
    return args

def percent_to_graph(percent: float, length: int=20) -> str:
    "turns a percent 0.0 - 1.0 into a bar graph"  

    # Calculate the number of '#' characters to represent the filled portion of the bar graph
    num_hashes = int(percent * length)
    
    # Calculate the number of spaces to represent the unfilled portion of the bar graph
    num_spaces = length - num_hashes
    
    # Construct the bar graph string with '#' for the filled part and spaces for the unfilled part
    return f"{'#' * num_hashes}{' ' * num_spaces}"

def get_sys_mem() -> int:
    "Return total system memory in kB"
    """
    This function reads the '/proc/meminfo' file and looks for the line that starts with 'MemTotal:'.
    The total memory is extracted and returned as an integer representing the number of kibibytes (kB).
    """
    # Open the /proc/meminfo file in read mode
    with open('/proc/meminfo', 'r') as f:
        # Iterate through each line in the file
        for line in f:
            # Check if the line contains 'MemTotal:'
            if 'MemTotal:' in line:
                # Split the line into components and return the second component (the number) as an integer
                return int(line.split()[1])
    # If 'MemTotal:' is not found, return 0 as a fallback
    return 0

def get_avail_mem() -> int:
    "Return available memory in kB"
    """
    This function reads the '/proc/meminfo' file and extracts the available memory based on the 'MemAvailable:',
    'MemFree:', and 'SwapFree:' fields. It prioritizes 'MemAvailable:' but falls back to 'MemFree:' + 'SwapFree:'
    if 'MemAvailable:' is not present.
    """
    # Initialize memory variables to 0
    mem_free = 0
    mem_available = 0
    swap_free = 0

    # Open the /proc/meminfo file in read mode
    with open('/proc/meminfo', 'r') as f:
        # Iterate through each line in the file
        for line in f:
            # Check if the line contains 'MemAvailable:'
            if 'MemAvailable:' in line:
                # Extract the value as an integer
                mem_available = int(line.split()[1])
            # Check if the line contains 'MemFree:'
            elif 'MemFree:' in line:
                # Extract the value as an integer
                mem_free = int(line.split()[1])
            # Check if the line contains 'SwapFree:'
            elif 'SwapFree:' in line:
                # Extract the value as an integer
                swap_free = int(line.split()[1])

        # If 'MemAvailable:' was found, return its value
        if mem_available:
            return mem_available
        # Otherwise, return the sum of 'MemFree:' and 'SwapFree:'
        return mem_free + swap_free

def pids_of_prog(app_name: str) -> list:
    "Given an app name, return all PIDs associated with app"
    # Execute the 'pidof' command to find the PIDs associated with the app name
    pids = os.popen(f'pidof {app_name}').read().strip()
    
    # If PIDs are found, split them into a list; if not, return an empty list
    return pids.split() if pids else []

def rss_mem_of_pid(proc_id: str) -> int:
    "Given a process ID, return the Resident memory used"
    try:
        # Open the smaps file for the given process ID
        with open(f'/proc/{proc_id}/smaps', 'r') as f:
            rss = 0  # Initialize the total RSS memory counter
            
            # Iterate through each line in the smaps file
            for line in f:
                # Check if the line contains 'Rss:'
                if 'Rss:' in line:
                    # Extract the value (in kB) and add it to the rss counter
                    rss += int(line.split()[1])
            
            # Return the total RSS memory used by the process
            return rss

    except FileNotFoundError:
        # If the process does not exist (e.g., the PID is invalid), return 0
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

if __name__ == "__main__":
    # Parse command-line arguments
    args = parse_command_args()

    # Get total and available system memory
    total_mem = get_sys_mem()
    avail_mem = get_avail_mem()
    used_mem = total_mem - avail_mem
    used_percent = used_mem / total_mem

    if not args.program:  # No program name specified.
        # Convert memory values to human-readable format if required
        human_total = bytes_to_human_r(total_mem) if args.human_readable else f"{total_mem}"
        human_used = bytes_to_human_r(used_mem) if args.human_readable else f"{used_mem}"
        percent = int(used_percent * 100)

        # Generate the bar graph for memory usage
        graph = percent_to_graph(used_percent, args.length)

        # Print the memory usage summary for the entire system
        print(f"Memory         [{graph}| {percent}%] {human_used}/{human_total}")

    else:  # Program name specified.

        # Get PIDs associated with the specified program
        pids = pids_of_prog(args.program)
        if not pids:
            # Print a message if no PIDs are found for the specified program
            print(f"{args.program} not found.")
        else:
            total_program_mem = 0

            # Iterate through each PID and calculate memory usage
            for pid in pids:
                rss = rss_mem_of_pid(pid)
                total_program_mem += rss
                percent = rss / total_mem

                # Convert RSS memory value to human-readable format if required
                human_rss = bytes_to_human_r(rss) if args.human_readable else f"{rss}"
                human_total_mem = bytes_to_human_r(total_mem) if args.human_readable else f"{total_mem}"

                # Generate the bar graph for each PID's memory usage
                graph = percent_to_graph(percent, args.length)
                # Print the memory usage for each PID
                print(f"{pid:<10} [{graph}| {int(percent * 100)}%] {human_rss}/{human_total_mem}")

            # Convert total program memory value to human-readable format if required
            if args.human_readable:
                human_total_program_mem = bytes_to_human_r(total_program_mem)
            else:
                human_total_program_mem = f"{total_program_mem}"
            # Print the total memory usage for the program
            print(f"{args.program:<10} [{percent_to_graph(total_program_mem / total_mem, args.length)}| {int((total_program_mem / total_mem) * 100)}%] {human_total_program_mem}/{total_mem}")


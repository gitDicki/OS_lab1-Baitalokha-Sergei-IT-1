#!/bin/bash

get_os_info() {
    echo "OS: $(lsb_release -d | cut -f2-)"
    echo "Kernel: $(uname -r)"
    echo "Architecture: $(uname -m)"
}

get_user_info() {
    echo "Hostname: $(hostname)"
    echo "User: $SUDO_USER"
}

get_memory_info() {
    free_ram=$(free -m | awk '/Mem:/ {print $4}')
    total_ram=$(free -m | awk '/Mem:/ {print $2}')
    total_swap=$(free -m | awk '/Swap:/ {print $2}')
    free_swap=$(free -m | awk '/Swap:/ {print $4}')

    echo "RAM: ${free_ram}MB free / ${total_ram}MB total"
    echo "Swap: ${total_swap}MB total / ${free_swap}MB free"
}

get_cpu_info() {
    cpu_count=$(nproc)
    load_avg=$(cat /proc/loadavg | awk '{print $1, $2, $3}')

    echo "Processors: ${cpu_count}"
    echo "Load average: ${load_avg}"
}

get_disk_info() {
    echo "Drives:"
    df -h
}

get_virtual_memory() {
    vmalloc_total=$(grep -i 'vmalloctotal' /proc/meminfo | awk '{print $2}')

    echo "Virtual memory: ${vmalloc_total} kB"
}

get_os_info
get_user_info
get_memory_info
get_virtual_memory
get_cpu_info
get_disk_info

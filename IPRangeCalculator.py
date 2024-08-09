import ipaddress

def ip_to_int(ip):
    return int(ipaddress.IPv4Address(ip))

def int_to_ip(ip_int):
    return str(ipaddress.IPv4Address(ip_int))

def calculate_ip_range(start_ip, end_ip, excluded_ips=[]):
    start_int = ip_to_int(start_ip)
    end_int = ip_to_int(end_ip)
    
    if start_int > end_int:
        raise ValueError("Start IP should be less than or equal to End IP")

    # Exclude IPs
    excluded_ints = set(ip_to_int(ip) for ip in excluded_ips)
    
    # Calculate total number of IPs in range, excluding static IPs
    total_ips = 0
    ip_range = []
    for ip_int in range(start_int, end_int + 1):
        if ip_int not in excluded_ints:
            total_ips += 1
            ip_range.append(int_to_ip(ip_int))

    return total_ips, ip_range

def main():
    # Example input
    start_ip = "192.168.1.10"
    end_ip = "192.168.2.20"
    excluded_ips = ["192.168.1.15", "192.168.1.16"]

    # Calculate IP range
    total_ips, ip_range = calculate_ip_range(start_ip, end_ip, excluded_ips)

    print(f"Total IP addresses (excluding static IPs): {total_ips}")
    print("IP Addresses in the range (excluding static IPs):")
    for ip in ip_range:
        print(ip)

if __name__ == "__main__":
    main()

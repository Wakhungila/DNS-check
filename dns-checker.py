import dns.resolver
import sys
from colorama import Fore, Style, init
import re

# Initialize colorama
init()

# GitHub Pages IP addresses (as of the last known data, may need to update if GitHub changes)
GITHUB_IPS = {
    '185.199.108.153',
    '185.199.109.153',
    '185.199.110.153',
    '185.199.111.153'
}

def extract_domain(url):
    # Remove http://, https://, and trailing slashes
    domain = re.sub(r'^https?://', '', url)
    domain = re.sub(r'/.*$', '', domain)
    return domain

def check_a_records(domain):
    try:
        answers = dns.resolver.resolve(domain, 'A')
        for rdata in answers:
            if rdata.address in GITHUB_IPS:
                print(f"{Fore.GREEN}{domain} points to GitHub IP address: {rdata.address}{Style.RESET_ALL}")
                return
        print(f"{Fore.YELLOW}{domain} does not point to any known GitHub IP addresses.{Style.RESET_ALL}")
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        print(f"{Fore.RED}{domain} does not have an A record or does not exist.{Style.RESET_ALL}")
    except dns.exception.Timeout:
        print(f"{Fore.RED}{domain} timed out while querying DNS.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred for {domain}: {e}{Style.RESET_ALL}")

def main(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                url = line.strip()
                if url:
                    domain = extract_domain(url)
                    check_a_records(domain)
    except FileNotFoundError:
        print(f"{Fore.RED}File {filename} not found.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Usage: python check_a_records.py <filename>{Style.RESET_ALL}")
        sys.exit(1)
    
    filename = sys.argv[1]
    main(filename)

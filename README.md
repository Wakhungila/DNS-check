This script will read a file containing subdomains, query the DNS for A records, and check if any of these records point to GitHub’s IP addresses.

To use this script, ensure Dependencies Are Installed:
    `pip install dnspython colorama`

To run the script:
    `python3 dns-checker.py filename.txt` #Replace <filename> with the name of your file containing subdomains.

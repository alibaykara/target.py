import os
import argparse

def run_tool(command):
    print(f"Running: {command}")
    os.system(command)

def main(target):
    tools = {
        "Amass": f"amass enum -d {target} > amass_output.txt 2>&1",
        "Assetfinder": f"assetfinder --subs-only {target} > assetfinder_output.txt 2>&1",
        "Findomain": f"findomain -t {target} -o findomain_output.txt",
        "Subfinder": f"subfinder -d {target} -o subfinder_output.txt",
        "FFUF": f"ffuf -u https://{target}/FUZZ -w wordlist.txt > ffuf_output.txt 2>&1",
        "LinkFinder": f"python3 linkfinder.py -i https://{target} -o linkfinder_output.html > linkfinder_output.txt 2>&1",
        "S3Scanner": f"s3scanner -d {target} > s3scanner_output.txt 2>&1",
        "BucketLoot": f"bucketloot -d {target} > bucketloot_output.txt 2>&1",
        "dnsx": f"dnsx -d {target} -o dnsx_output.txt",
        "Censys ASN Lookup": f"censys search {target} > censys_output.txt 2>&1",
        "Aquatone": f"cat subdomains.txt | aquatone > aquatone_output.txt 2>&1",
        "gau": f"gau {target} > gau_output.txt 2>&1",
        "urlhunter": f"urlhunter -d {target} -o urlhunter_output.txt",
        "httpx": f"cat subdomains.txt | httpx -o httpx_output.txt",
        "katana": f"katana -u https://{target} -o katana_output.txt",
        "BBOT": f"bbot -t {target} --no-interactive -o bbot_output.txt"
    }
    
    for tool, command in tools.items():
        print(f"[+] Running {tool}...")
        run_tool(command)
        print(f"[+] {tool} completed!\n")
    
    print("[+] Merging outputs into all.txt...")
    merge_command = "cat amass_output.txt assetfinder_output.txt findomain_output.txt subfinder_output.txt > all.txt"
    os.system(f"sh -c '[ -s amass_output.txt ] && [ -s assetfinder_output.txt ] && [ -s findomain_output.txt ] && [ -s subfinder_output.txt ] && {merge_command} || echo \"No valid data to merge\"'")
    print("[+] Merging completed!\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run security tools against a target domain.")
    parser.add_argument("-t", "--target", required=True, help="Target domain")
    args = parser.parse_args()
    main(args.target)

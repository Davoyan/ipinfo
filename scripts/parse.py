import csv
import gzip
import ipaddress
from collections import defaultdict
from pathlib import Path

INPUT_FILE = "ipinfo_lite.csv.gz"

OUTPUT_DIR = Path("geo/geoip")
CONTINENT_DIR = OUTPUT_DIR / "continent"
CDN_DIR = Path("CDN")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
CONTINENT_DIR.mkdir(parents=True, exist_ok=True)
CDN_DIR.mkdir(parents=True, exist_ok=True)

countries = defaultdict(list)
continents = defaultdict(list)

cdn_patterns = {
    "cloudflare": ["cloudflare"],
    "fastly": ["fastly"],
    "amazon": ["amazon"],
    "datacamp": ["datacamp"],
    "akamai": ["akamai"],
    "oracle": ["oracle"],
}

cdn_providers = {name: [] for name in cdn_patterns}
cdn_all = []

with gzip.open(INPUT_FILE, "rt", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        country_code = row.get("country_code", "").strip()
        continent = row.get("continent", "").strip()
        network = row.get("network", "").strip()
        as_name = row.get("as_name", "").strip().lower()

        if not network:
            continue

        try:
            net_obj = ipaddress.ip_network(network, strict=False)
        except ValueError:
            continue

        if country_code:
            countries[country_code].append(str(net_obj))
        if continent:
            continents[continent].append(str(net_obj))

        for provider, patterns in cdn_patterns.items():
            if any(p in as_name for p in patterns):
                cdn_providers[provider].append(str(net_obj))
                cdn_all.append(str(net_obj))
                
for code, networks in countries.items():
    lst_file = OUTPUT_DIR / f"{code.lower().replace(' ', '_')}.lst"
    with open(lst_file, "w", encoding="utf-8") as f:
        f.write("\n".join(networks))

    yaml_file = OUTPUT_DIR / f"{code.lower().replace(' ', '_')}.yaml"
    with open(yaml_file, "w", encoding="utf-8") as f:
        f.write("payload:\n")
        for net in networks:
            f.write(f"    - {net}\n")
            
for code, networks in continents.items():
    lst_file = CONTINENT_DIR / f"{code.lower().replace(' ', '_')}.lst"
    with open(lst_file, "w", encoding="utf-8") as f:
        f.write("\n".join(networks))

    yaml_file = CONTINENT_DIR / f"{code.lower().replace(' ', '_')}.yaml"
    with open(yaml_file, "w", encoding="utf-8") as f:
        f.write("payload:\n")
        for net in networks:
            f.write(f"    - {net}\n")
            
for provider, networks in cdn_providers.items():
    if not networks:
        continue

    lst_file = CDN_DIR / f"{provider.replace(' ', '_')}.lst"
    with open(lst_file, "w", encoding="utf-8") as f:
        f.write("\n".join(networks))

    yaml_file = CDN_DIR / f"{provider.replace(' ', '_')}.yaml"
    with open(yaml_file, "w", encoding="utf-8") as f:
        f.write("payload:\n")
        for net in networks:
            f.write(f"    - {net}\n")
            
if cdn_all:
    all_lst = CDN_DIR / "all.lst"
    with open(all_lst, "w", encoding="utf-8") as f:
        f.write("\n".join(cdn_all))

    all_yaml = CDN_DIR / "all.yaml"
    with open(all_yaml, "w", encoding="utf-8") as f:
        f.write("payload:\n")
        for net in cdn_all:
            f.write(f"    - {net}\n")
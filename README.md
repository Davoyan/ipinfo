# IPInfo GeoIP Lists by Country

This repository contains **IP address ranges organized by country**, generated from [IPinfo Lite](https://ipinfo.io/) data. Each file corresponds to a country and contains a list of networks in CIDR notation.

---


- Each `.lst` file contains **one network per line**.
- File names are **two-letter ISO 3166-1 alpha-2 country codes** in lowercase.


## Source

Data is downloaded from [IPinfo Lite](https://ipinfo.io/data) automatically using a GitHub Actions workflow:

- The workflow downloads the latest CSV file.
- Parses it into `.lst` files per country.
- Commits and pushes the updated files back to the repository.


## Usage

You can use these lists for:

- Firewall rules
- GeoIP-based routing
- IP filtering and analytics

Example: reading RU networks in Clash Mihomo:

```
  geoip-ru:
    type: http
    behavior: ipcidr
    format: text
    url: https://raw.githubusercontent.com/Davoyan/ipinfo/main/geo/geoip/ru.lst
    path: ./rule-sets/geoip-ru.lst
    interval: 86400
```

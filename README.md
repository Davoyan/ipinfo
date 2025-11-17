# IPInfo GeoIP Lists by Country

This repository contains **IP address ranges organized by country**, generated from [IPinfo Lite](https://ipinfo.io/) data ***daily***. Each file corresponds to a country and contains a list of networks in CIDR notation.

---


## Source

Data is downloaded from [IPinfo Lite](https://ipinfo.io/data) :

- Automaticly downloads the latest CSV file.
- Parses it into `.lst`, `.yaml`, `.mrs` files per country.
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
    format: mrs
    url: https://raw.githubusercontent.com/Davoyan/ipinfo/main/geo/geoip/ru.mrs
    path: ./rule-sets/geoip-ru.mrs
    interval: 86400
```

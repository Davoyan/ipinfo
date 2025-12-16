## Установка для сервера (Marzban)

Создаем папку 
```bash
mkdir -p /var/lib/marzban/assets/
```
Скачиваем 
```bash
wget -O /var/lib/marzban/assets/geoipinfo.dat https://github.com/Davoyan/ipinfo/releases/latest/download/geoipinfo.dat
```
Устанавливаем значение в .env файле

```XRAY_ASSETS_PATH = "/var/lib/marzban/assets/"```

Редактируем xray_config.json
```json
    "routing": {
        "domainStrategy": "IPIfNonMatch",
        "rules": [
            {
                "outboundTag": "RU-OUTBOUND",
                "domain": [
                    "ext:geoipinfo.dat:ru",
                    "ext:geoipinfo.dat:by"
                ],
                "type": "field"
            }
        ]
    }
```

#!/bin/bash

echo "[*] Cleaning nifi.properties duplicates..."
CONFIG_FILE=/opt/nifi/nifi-current/conf/nifi.properties

# Remove duplicates of nifi.web.http.port and nifi.web.http.host keeping the first occurrence
awk '!seen[$0]++' "$CONFIG_FILE" > /tmp/nifi_cleaned.properties && mv /tmp/nifi_cleaned.properties "$CONFIG_FILE"

echo "[*] Starting NiFi..."
exec /opt/nifi/nifi-current/bin/nifi.sh run

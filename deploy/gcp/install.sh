#!/bin/bash
# Run as root after uploading the allowlisted application and private snapshot.
set -euo pipefail
: "${IAP_AUDIENCE:?Set the backend-service audience}"
: "${RELEASE_DIR:?Set uploaded release directory}"
apt-get update -qq
DEBIAN_FRONTEND=noninteractive apt-get install -y -qq python3-venv python3-pip
id bumpp >/dev/null 2>&1 || useradd --system --home-dir /var/lib/bumpp-intelligence --shell /usr/sbin/nologin bumpp
DISK=/dev/disk/by-id/google-intelligence-data
if ! blkid "$DISK" >/dev/null 2>&1; then mkfs.ext4 -F "$DISK"; fi
mkdir -p /var/lib/bumpp-intelligence
if ! grep -q 'google-intelligence-data' /etc/fstab; then
  echo "$DISK /var/lib/bumpp-intelligence ext4 defaults 0 2" >> /etc/fstab
fi
mountpoint -q /var/lib/bumpp-intelligence || mount /var/lib/bumpp-intelligence
mkdir -p /opt/bumpp-intelligence/current /var/lib/bumpp-intelligence/data
tar -xzf "$RELEASE_DIR/application.tgz" -C /opt/bumpp-intelligence/current
if [ ! -f /var/lib/bumpp-intelligence/data/intelligence.sqlite3 ] && [ -f "$RELEASE_DIR/private-data.tgz" ]; then
  tar -xzf "$RELEASE_DIR/private-data.tgz" -C /var/lib/bumpp-intelligence/data
fi
chown -R bumpp:bumpp /var/lib/bumpp-intelligence
chmod 700 /var/lib/bumpp-intelligence/data
find /var/lib/bumpp-intelligence/data -type f -exec chmod 600 {} +
python3 -m venv /opt/bumpp-intelligence/venv
/opt/bumpp-intelligence/venv/bin/pip install --quiet -r /opt/bumpp-intelligence/current/deploy/gcp/requirements.txt
printf 'BUMPP_PUBLIC_ORIGIN=https://intelligence.bumpp.gg\nBUMPP_IAP_AUDIENCE=%s\n' "$IAP_AUDIENCE" > /etc/bumpp-intelligence.env
chmod 600 /etc/bumpp-intelligence.env
cp /opt/bumpp-intelligence/current/deploy/gcp/bumpp-intelligence.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable --now bumpp-intelligence
sleep 2
systemctl is-active bumpp-intelligence
curl --fail --silent http://127.0.0.1:8080/healthz
# Source retention cleanup runs even when nobody opens the dashboard.
cat > /etc/cron.d/bumpp-purge <<'CRON'
17 3 * * * bumpp cd /opt/bumpp-intelligence/current && PYTHONDONTWRITEBYTECODE=1 /opt/bumpp-intelligence/venv/bin/python -m intelligence --data-dir /var/lib/bumpp-intelligence/data purge >/dev/null 2>&1
CRON
chmod 644 /etc/cron.d/bumpp-purge
rm -f "$RELEASE_DIR/private-data.tgz"

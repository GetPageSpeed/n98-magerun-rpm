#!/bin/bash
set -x
RHEL=$(rpm -E %{rhel})

yum -y install http://rpms.remirepo.net/enterprise/remi-release-${RHEL}.rpm

# Remi: PHP version older than 7.2 are not available for RHEL 8
if [[ "${RHEL}" -ge "8" ]]; then
  dnf -y install yum-utils
  dnf -y module reset php
  dnf -y module install php:remi-7.2
else
  REPO=remi-php56
  yum -y install yum-utils
  yum-config-manager --enable ${REPO}
fi

yum -y install php-cli
echo "phar.readonly=0" >> /etc/php.d/zzz.ini


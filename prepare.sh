#!/bin/bash

RHEL=$(rpm -E %{rhel})

if [[ ${RHEL} -eq 6 ]]; then
  yum -y install http://rpms.remirepo.net/enterprise/remi-release-6.rpm
elif [[ ${RHEL} -eq 7 ]]; then
  yum -y install http://rpms.remirepo.net/enterprise/remi-release-7.rpm
elif [[ ${RHEL} -eq 8 ]]; then
  yum -y install http://rpms.remirepo.net/enterprise/remi-release-8.rpm
fi

if test -f /usr/bin/dnf; then
  dnf config-manager --set-enabled remi
  dnf config-manager --set-enabled remi-php56
else
  yum -y install yum-utils
  yum-config-manager --enable remi
  yum-config-manager --enable remi-php56
fi

# php-pear-phing in remi is no good
yum -y install --disablerepo=remi* php-pear-phing

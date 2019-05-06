#!/bin/bash

if grep -q -i "release 6" /etc/redhat-release; then
  yum -y install http://rpms.remirepo.net/enterprise/remi-release-6.rpm
  # composer is there for EL6:
  yum-config-manager --enable remi
fi
if grep -q -i "release 7" /etc/redhat-release; then
  yum -y install http://rpms.remirepo.net/enterprise/remi-release-7.rpm yum-utils
fi
yum-config-manager --enable remi-php56

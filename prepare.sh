#!/bin/bash

yum -y install http://rpms.remirepo.net/enterprise/remi-release-7.rpm yum-utils
yum-config-manager --enable remi-php56

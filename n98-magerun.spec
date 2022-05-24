%global upstream_github netz98
%global upstream_name n98-magerun

# License: MIT
# http://opensource.org/licenses/MIT

Name: n98-magerun
Version: 2.3.0
Release: 1%{?dist}
Summary: n98-magerun. The swiss army knife for Magento developers

License: GPLv2+ and MIT and BSD
URL: https://magerun.net/
#Source0: https://files.magerun.net/n98-magerun-%{version}.phar
Source0: https://github.com/%{upstream_github}/%{upstream_name}/archive/%{version}/%{upstream_name}-%{version}.tar.gz

BuildRequires: php-cli php-pear-phing composer

BuildArch: noarch

Requires:  php(language) >= 5.4
Requires:  php-mbstring
Requires:  php-openssl
Requires:  php-xml

# TODO: Get info from phpcompatinfo reports for 2.1.2


%description
The swiss army knife for Magento developers, sysadmins and devops.
The tool provides a huge set of well tested command line commands which 
save hours of work time. All commands are extendable by a module API.

%prep
%autosetup
# load modules from /usr/share/n98-magerun/modules:
sed -i 's@- /usr/local/share/n98-magerun/modules@- /usr/share/n98-magerun/modules\n    - /usr/local/share/n98-magerun/modules@' config.yaml

%build
ulimit -Sn "$(ulimit -Hn)"
PHP_COMMAND="/usr/bin/php -d phar.readonly=0" /usr/bin/phing dist_clean

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT%{_bindir}
%{__install} -m 755 -p n98-magerun.phar $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%defattr(-,root,root)
%{_bindir}/%{name}

%changelog
* Tue May 24 2022 Danila Vershinin <info@getpagespeed.com> 2.3.0-1
- release 2.3.0

* Mon Jun 14 2021 Danila Vershinin <info@getpagespeed.com> 2.2.0-1
- release 2.2.0

* Wed Dec 23 2020 Danila Vershinin <info@getpagespeed.com> 2.1.0-1
- release 2.1.0

* Sun Jul 26 2020 Danila Vershinin <info@getpagespeed.com> 2.0.0-1
- release 2.0.0

* Fri Apr 03 2020 Danila Vershinin <info@getpagespeed.com> 1.103.3-1
- upstream version auto-updated to 1.103.3

* Sun Mar 01 2020 Danila Vershinin <info@getpagespeed.com> 1.103.2-1
- upstream version auto-updated to 1.103.2

* Sat Jul 20 2019 Danila Vershinin <info@getpagespeed.com> 1.103.1-1
- upstream version auto-updated to 1.103.1

* Mon Jun 10 2019 Danila Vershinin <info@getpagespeed.com> 1.103.0-1
- upstream version auto-updated to 1.103.0

* Sun May 05 2019 Danila Vershinin <info@getpagespeed.com> 1.102.0-2
- load modules from /usr/share/n98-magerun/modules in addition to /usr/local/share/...
- build insted of phar fetch from upstream

* Mon Oct 08 2018 Danila Vershinin <info@getpagespeed.com> 1.102.0-1
- upstream version auto-updated to 1.102.0

* Sat May 12 2018 Danila Vershinin <info@getpagespeed.com> 1.101.1-1
- upstream version auto-updated to 1.101.1



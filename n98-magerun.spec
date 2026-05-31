# License: MIT
# http://opensource.org/licenses/MIT

Name: n98-magerun
Version: 3.0.1
Release: 2%{?dist}
Summary: n98-magerun. The swiss army knife for Magento developers

License: GPLv2+ and MIT and BSD
URL: https://magerun.net/
Source0: https://files.magerun.net/n98-magerun-%{version}.phar

BuildArch: noarch

Requires: php(language) >= 7.4
Requires: php-mbstring
Requires: php-openssl
Requires: php-xml

%description
The swiss army knife for Magento developers, sysadmins and devops.
The tool provides a huge set of well tested command line commands which
save hours of work time. All commands are extendable by a module API.

%prep
# Nothing to do — Source0 is the prebuilt phar.

%build
# Nothing to do.

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT%{_bindir}
%{__install} -m 755 -p %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%defattr(-,root,root)
%{_bindir}/%{name}

%changelog
* Sun May 31 2026 Danila Vershinin <info@getpagespeed.com> 3.0.1-2
- switch back to upstream-prebuilt phar from files.magerun.net
- upstream 3.x ships an out-of-sync composer.lock and a require-dev set that pins
  rector ^2 / phpstan ^2 with strict PHP upper bounds, so building via composer+phing
  no longer resolves on newer distros' PHP; the upstream-blessed phar is the artifact
- bump Requires php(language) >= 7.4 to match upstream's actual platform req

* Sun May 31 2026 Danila Vershinin <info@getpagespeed.com> 3.0.1-1
- release 3.0.1

* Wed Sep 07 2022 Danila Vershinin <info@getpagespeed.com> 2.3.0-1
- release 2.3.0

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

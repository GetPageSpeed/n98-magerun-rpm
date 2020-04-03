Summary: A bash completion helper for n98-magerun
Name: n98-magerun-completion-bash
Version: 1.103.3
Release: 1%{?dist}
License: GPL
Group: System Environment/Shells
URL: http://magerun.net/

Source0: https://github.com/netz98/n98-magerun/archive/%{version}/n98-magerun-%{version}.tar.gz


BuildArch: noarch
Requires: bash-completion

%description
Install this package to enable tab-completion of functions and installed
modules with the n98-magerun command.

%prep
%setup -n n98-magerun-%{version}


%build
# Nothing to do

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -d -m0755 $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/
%{__install} -Dp -m0755 res/autocompletion/bash/n98-magerun.phar.bash $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/

%post
. /etc/profile.d/bash_completion.sh

%postun
. /etc/profile.d/bash_completion.sh

%files
%defattr(-, root, root, 0755)
%config %{_sysconfdir}/bash_completion.d/*

%changelog
* Fri Apr 03 2020 Danila Vershinin <info@getpagespeed.com> 1.103.3-1
- upstream version auto-updated to 1.103.3

* Sun Mar 01 2020 Danila Vershinin <info@getpagespeed.com> 1.103.2-1
- upstream version auto-updated to 1.103.2

* Sat Jul 20 2019 Danila Vershinin <info@getpagespeed.com> 1.103.1-1
- upstream version auto-updated to 1.103.1

* Mon Jun 10 2019 Danila Vershinin <info@getpagespeed.com> 1.103.0-1
- upstream version auto-updated to 1.103.0

* Mon Oct 08 2018 Danila Vershinin <info@getpagespeed.com> 1.102.0-1
- upstream version auto-updated to 1.102.0

* Sat May 12 2018 Danila Vershinin <info@getpagespeed.com> 1.101.1-1
- upstream version auto-updated to 1.101.1


%{!?python_ver: %global python_ver %(%{__python} -c "import sys ; print sys.version[:3]")}
%global libname vdsm-arch-dependencies

Name:       %{libname}
Version:    1.0
Release:    2%{?dist}
Summary:    Meta-package for handling architecture-specific details of VDSM
Group:      Applications/System
License:    GPLv2+
URL:        http://bronhaim.fedorapeople.org

%ifarch x86_64
Requires: python-dmidecode
Requires: dmidecode
%endif

%description
This package maintains architecture specific dependencies of VDSM. On different
architectures, VDSM requires different packages. This package provides a
transparent way to handle this.

%prep

%build

%install

%files

%changelog
* Mon Oct 20 2014 Yaniv Bronhaim <ybronhei@redhat.com> - 1.0-2
- Adding URL and fix semantic issues for official fedora-review

* Sun Aug 10 2014 Yoav Kleinberger <ykleinbe@redhat.com> - 1.0-1
- this is the first version of this package, so no changes

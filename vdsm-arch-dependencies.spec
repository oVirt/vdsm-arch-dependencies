Name:       vdsm-arch-dependencies
Version:    1.0
Release:    1%{?dist}
Summary:    meta-package for handling architecture-specific details of VDSM
Group:      Applications/System
License:    GPLv2+

%ifarch x86_64
Requires: python-dmidecode
Requires: dmidecode
%endif

%description
This package maintains architecture specific dependencies of VDSM. On different
architectures, VDSM requires different packages. This package provides a
transparent way to handle this.

%install

%files

%changelog
* Sun Aug 10 2014 Yoav Kleinberger <ykleinbe@redhat.com> - 1.0-1
- this is the first version of this package, so no changes

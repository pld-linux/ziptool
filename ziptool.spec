Summary:	Tools for Iomega JAZ and ZIP drives
Name:		ziptool
Version:	1.3
Release:	1
License:	GPL
Group:		Utilities/System
Group(pl):   	Narzêdzia/System
Source:		%{name}-%{version}.tar.bz2
# ziptool-1.3 - n
#Source:	ftp://sunsite.unc.edu/pub/Linux/utils/disk-management/%{name}-%{version}.tar.bz2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Medium protection is done by software for Iomega's JAZ and ZIP drives,
jaztool and ziptool make this features available for Linux.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS" 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -s ziptool $RPM_BUILD_ROOT%{_bindir}
ln -sf ziptool $RPM_BUILD_ROOT%{_bindir}/jaztool

install ziptool.1.gz $RPM_BUILD_ROOT%{_mandir}/man1
ln -sf ziptool.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/jaztool.1.gz
gzip -9nf README

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(644,root,root,755)
%doc README.gz 
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

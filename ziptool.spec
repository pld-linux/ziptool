Summary:	Tools for Iomega JAZ and ZIP drives
Name:		ziptool
Version:	1.3
Release:	1
License:	GPL
Group:		Utilities/System
Group(pl):   	Narzêdzia/System
Source:		http://www.novia.net/~segura/ziptool/%{name}-%{version}.tar.gz
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

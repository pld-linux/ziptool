Summary:	Tools for Iomega JAZ and ZIP drives
Summary(pl):	Narzêdzia do napêdów Iomega JAZ i ZIP
Name:		ziptool
Version:	1.3
Release:	3
License:	GPL
Group:		Applications/System
Source0:	http://www.novia.net/~segura/ziptool/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Medium protection is done by software for Iomega's JAZ and ZIP drives,
jaztool and ziptool make this features available for Linux.

%description -l pl
Oprogramowanie dla napêdów Iomega JAZ i ZIP pozwala na zabezpieczenie
no¶nika; jaztool i ziptool pozwalaj± zrobiæ to pod Linuksem.

%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags}" 
gzip -d ziptool.1.gz

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install ziptool $RPM_BUILD_ROOT%{_bindir}
ln -sf ziptool $RPM_BUILD_ROOT%{_bindir}/jaztool

install ziptool.1 $RPM_BUILD_ROOT%{_mandir}/man1
echo ".so ziptool.1" > $RPM_BUILD_ROOT%{_mandir}/man1/jaztool.1

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz 
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

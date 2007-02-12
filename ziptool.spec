Summary:	Tools for Iomega JAZ and ZIP drives
Summary(pl.UTF-8):	Narzędzia do napędów Iomega JAZ i ZIP
Name:		ziptool
Version:	1.4.0
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://wolfpack.twu.net/users/wolfpack/%{name}-%{version}.tar.bz2
# Source0-md5:	e873a323c4cfdca95cb109a704dd34ee
Patch0:		%{name}-llh.patch
URL:		http://wolfpack.twu.net/utilities.html#ziptool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Medium protection is done by software for Iomega's JAZ and ZIP drives,
jaztool and ziptool make this features available for Linux.

%description -l pl.UTF-8
Oprogramowanie dla napędów Iomega JAZ i ZIP pozwala na zabezpieczenie
nośnika; jaztool i ziptool pozwalają zrobić to pod Linuksem.

%prep
%setup -q
%patch0 -p1

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

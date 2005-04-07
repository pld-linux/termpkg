Summary:	Terminal server daemon and simple telnet-like client
Summary(pl):	Serwer terminalowy i klient podobny do telneta
Name:		termpkg
Version:	3.3
Release:	2
License:	GPL v1+
Group:		Networking
Source0:	ftp://ftp.croftj.net/usr/termpkg/%{name}-%{version}.tar.gz
# Source0-md5:	cf773eb9cc3cbbf57cb0d3c39287370f
Patch0:		%{name}-glibc.patch
Patch1:		%{name}-alpha.patch
URL:		http://www.croftj.net/~termpkg/
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Terminal server daemon and simple telnet like client. Allows access to
one or more serial ports through the telnet protocol. Can be
configured to connect in a one to one relation of telnet ports to
serial ports or in a round-robin fashion where one telnet port serves
many serial ports.

%description -l pl
Serwer terminalowy i prosty klient podobny do telneta. Pakiet pozwala
na dostêp do jednego lub wiêcej portów szeregowych poprzez protokó³
telnet. Mo¿e byæ skonfigurowany do ³±czenia portów szeregowych i
telnet jeden do jednego lub w stylu round-robin, gdzie jeden port
telnet s³u¿y wielu portom szeregowym.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
./configure
cd linux
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DLINUX -I../libtn"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}}

install linux/bin/* $RPM_BUILD_ROOT%{_bindir}
install doc/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install termnetd/termnetd.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/termnetd.conf

Summary:	CPhone - cross-platform VoIP client using the H323 protocol
Summary(pl):	CPhone - wieloplatformowy klient VoIP u¿ywaj±cy protoko³u H323
Name:		cphone
Version:	0.3.0
Release:	0.1
License:	MPL v1
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	a5b85ede474768b5c03f1d47aec5f07c
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-comp_fix.patch
URL:		http://cphone.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	openh323-devel >= 1.12.0
BuildRequires:	pwlib-devel >= 1.5.0
BuildRequires:	qt-devel >= 3.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CPhone is a cross platform VoIP client which uses the H323 protocol.
It compiles and runs on Linux, BSD, Windows and MacOS X boxes. It
is based on the libraries from http://www.openh323.org/ and Trolltech.

%description -l pl
CPhone to wieloplatformowy klient VoIP u¿ywaj±cy protoko³u H323.
Kompiluje siê i dzia³a pod Linuksem, BSD, Windows i MacOS X. Jest
oparty na bibliotekach z http://www.openh323.org/ i Trolltecha.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} opt \
	QTDIR="%{_prefix}" \
	OPENH323DIR="/usr" \
	CFLAGS="-I%{_prefix}/include"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install obj_linux_x86_r/%{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

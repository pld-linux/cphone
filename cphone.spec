Summary:	CPhone - cross-platform VoIP client using the H323 protocol
Summary(pl.UTF-8):   CPhone - wieloplatformowy klient VoIP używający protokołu H323
Name:		cphone
Version:	0.3.1
Release:	0.1
License:	MPL v1
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/cphone/%{name}-%{version}.tar.bz2
# Source0-md5:	7574cc0aae961561792bd0b8d17ae933
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

%description -l pl.UTF-8
CPhone to wieloplatformowy klient VoIP używający protokołu H323.
Kompiluje się i działa pod Linuksem, BSD, Windows i MacOS X. Jest
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
%doc README
%attr(755,root,root) %{_bindir}/*

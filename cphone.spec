Summary:	cphone
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
BuildRequires:	pwlib-devel >= 1.5.0
BuildRequires:	openh323-devel >= 1.12.0
BuildRequires:	qt-devel >= 3.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description

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

Summary:	LinuxGazette - common files
Summary(pl):	Wspólne pliki dla LinuxGazette
Name:		lg-base
Version:	100
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://linuxgazette.net/ftpfiles/%{name}.tar.gz
# Source0-md5:	4831b9a2871fe8e7bd61db5cfab4eac2
URL:		http://www.linuxgazette.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
This package contains common files of LinuxGazette.

%description -l pl
Ten pakiet zawiera pliki wspólne dla wszystkich wydañ LinuxGazette.

%prep
%setup -q -n lg

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_defaultdocdir}/LinuxGazette
cp -ar * $RPM_BUILD_ROOT%{_defaultdocdir}/LinuxGazette

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_defaultdocdir}/LinuxGazette

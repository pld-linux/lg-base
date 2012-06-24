Summary:	LinuxGazette - common files
Summary(pl):	Wsp�lne pliki dla LinuxGazette
Name:		lg-base
Version:	105
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://linuxgazette.net/ftpfiles/%{name}.tar.gz
# Source0-md5:	abcdc5442e14471017a6c6a681ca1ff2
URL:		http://www.linuxgazette.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
This package contains common files of LinuxGazette.

%description -l pl
Ten pakiet zawiera pliki wsp�lne dla wszystkich wyda� LinuxGazette.

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

Summary:	LinuxGazette - common files
Summary(pl):	Wspólne pliki dla LinuxGazette
Name:		lg-base
Version:	106
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://linuxgazette.net/ftpfiles/%{name}.tar.gz
# Source0-md5:	2ad3d8320c96f4d858e9965ebecfd36c
URL:		http://www.linuxgazette.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
This package contains common files of LinuxGazette.

%description -l pl
Ten pakiet zawiera pliki wspólne dla wszystkich wydañ LinuxGazette.

%prep
%setup -q -n lg

%build
%{__sed} -i -e 's,href="10,href="issue10,g' *.html 
ln -sf issue%{version} current

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_defaultdocdir}/LinuxGazette
cp -ar * $RPM_BUILD_ROOT%{_defaultdocdir}/LinuxGazette

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_defaultdocdir}/LinuxGazette

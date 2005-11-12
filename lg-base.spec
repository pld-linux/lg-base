Summary:	LinuxGazette - common files
Summary(pl):	Wspólne pliki dla LinuxGazette
Name:		lg-base
Version:	120
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://linuxgazette.net/ftpfiles/%{name}.tar.gz
# Source0-md5:	24850ce06fb77d4fe05cb20fbbfbca1b
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
%{__sed} -i -e 's,href="10,href="issue10,g' \
            -e 's,href="11,href="issue11,g' \
            -e 's,href="12,href="issue12,g' *.html 
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

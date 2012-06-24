Summary:	LinuxGazette - common files
Summary(pl):	Wsp�lne pliki dla LinuxGazette
Name:		lg-base
Version:	129
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://linuxgazette.net/ftpfiles/%{name}.tar.gz
# Source0-md5:	7ce172f57de684aaa4027d173c7bbb90
URL:		http://www.linuxgazette.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains common files of LinuxGazette.

%description -l pl
Ten pakiet zawiera pliki wsp�lne dla wszystkich wyda� LinuxGazette.

%prep
%setup -q -n lg

%build
%{__sed} -i -e 's,href="10,href="issue10,g' \
	-e 's,href="11,href="issue11,g' \
	-e 's,href="12,href="issue12,g' *.html
ln -sf issue%{version} current

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/LinuxGazette
cp -a * $RPM_BUILD_ROOT%{_docdir}/LinuxGazette

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/LinuxGazette

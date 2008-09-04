Summary:	LinuxGazette - common files
Summary(pl.UTF-8):	Wspólne pliki dla LinuxGazette
Name:		lg-base
Version:	154
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://linuxgazette.net/ftpfiles/%{name}.tar.gz
# Source0-md5:	a46fa1e17aad8fe655a282b2044db583
URL:		http://www.linuxgazette.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains common files of LinuxGazette.

%description -l pl.UTF-8
Ten pakiet zawiera pliki wspólne dla wszystkich wydań LinuxGazette.

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

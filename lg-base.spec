Summary:	LinuxGazette - common files.
Summary(pl):	Wspólne pliki dla LinuxGazette.
Name:		lg-base
Version:	88
Release:	1
URL:		http://www.linuxgazette.org/
License:	distributable
Group:		Documentation
Source0:	ftp://ftp.ssc.com/pub/lg/%{name}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
This package contains common files of LinuxGazette.

%description -l pl
Ten pakiet zawiera pliki wspólne dla wszystkich wydañ LinuxGazette.

%prep
%setup -q -n lg

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_defaultdocdir}/LinuxGazette
cp -ar * $RPM_BUILD_ROOT%{_defaultdocdir}/LinuxGazette

%clean
test "$RPM_BUILD_ROOT" != "/" && rm -rf ${RPM_BUILD_ROOT}

%post

%files 
%defattr(644,root,root,755)
%{_defaultdocdir}/LinuxGazette/authors
%{_defaultdocdir}/LinuxGazette/faq
%{_defaultdocdir}/LinuxGazette/gx
%{_defaultdocdir}/LinuxGazette/tag
%{_defaultdocdir}/LinuxGazette/404.html
%{_defaultdocdir}/LinuxGazette/copying.html
%{_defaultdocdir}/LinuxGazette/index.html
%{_defaultdocdir}/LinuxGazette/lg_index.html
%{_defaultdocdir}/LinuxGazette/mirrors.html
%{_defaultdocdir}/LinuxGazette/search.html

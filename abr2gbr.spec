Summary:	abr2gbr
Name:		abr2gbr
Version:	1.0.2
Release:	1
License:	GPL v2
Group:		Applications/Graphics
Source0:	http://the.sunnyspot.org/gimp/tools/%{name}-%{version}.tgz
# Source0-md5:	edecc74a3df1ce858ec641de9a098cdf
URL:		http://the.sunnyspot.org/gimp/tools.html
BuildRequires:	glib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Converts PhotoShop .ABR and Paint Shop Pro .JBR brushes to GIMP .GBR. 

ABR files can hold many bushes within a single file and GIMP's GBR format was
build only for single brushes. This tool simply extract each brush and save it
into a separate GBR file. 

Actually abr2gbr can decode only ABR files with format version less or equal to
1, format version 2 is undocumented

%prep
%setup -qc

%build
%{__make} -C src

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install src/abr2gbr $RPM_BUILD_ROOT%{_bindir}
ln -s abr2gbr $RPM_BUILD_ROOT%{_bindir}/jbr2gbr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc src/TODO
%attr(755,root,root) %{_bindir}/abr2gbr
%attr(755,root,root) %{_bindir}/jbr2gbr

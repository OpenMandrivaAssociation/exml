%define _missing_doc_files_terminate_build 0
%define version 0.1.1
%define release %mkrel 7

%define major 1
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Summary: XML Library for EFL
Name: exml
Version: %{version}
Release: %{release}
License: BSD
Group:   System/Libraries
URL: http://www.enlightenment.org/
Source: ftp://ftp.enlightenment.org/pub/exml/%{name}-%{version}.tar.bz2
BuildRequires: libxml2-devel, ecore-devel >= 0.9.9.038
Buildrequires: libxslt-proc, %{mklibname xslt1}-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
XML library for EFL

%package -n %libname
Summary: Exml libraries
Group:   System/Libraries
Requires: libxml2-devel, ecore >= 0.9.9.038
Provides: %name = %version-%release

%description -n %libname
Exml libraries

%package -n %libnamedev
Summary: Exml headers, static libraries, documentation and test programs
Group:   System/Libraries
Requires: libxml2-devel,  ecore-devel >= 0.9.9.038
Requires: %libname = %version
Provides: lib%{name}-devel = %version-%release
Provides: %{name}-devel = %version-%release

%description -n %libnamedev
Headers, static libraries, test programs and documentation for EXML

%prep
rm -rf $RPM_BUILD_ROOT
%setup -n %name-%version

%build
%configure2_5x
%make

%install
%makeinstall

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %libname
%defattr(-, root, root)
%doc AUTHORS COPYING INSTALL NEWS README
%{_libdir}/*.so.%{major}*

%files -n %libnamedev
%defattr(-, root, root)
%doc doc/html
%{_libdir}/*a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_bindir}/exml-config
%{_includedir}/*

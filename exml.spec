%define _missing_doc_files_terminate_build 0

%define	name exml
%define version 0.1.1
%define	svn 20090227
%define release %mkrel 2.svn%{svn}.4

%define major	0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} -d

Summary:	XML Library for EFL
Name:		%{name}
Version:	%{version}
Release:	%{release}
Epoch:		1
License:	BSD
Group:		System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.enlightenment.org/
Source:		%{name}-%version.tar.bz2
BuildRequires:	libxml2-devel
BuildRequires:	ecore-devel >= 0.9.9.050
Buildrequires:	libxslt-proc, libxslt-devel

%description
XML library for EFL.

%package -n %libname
Summary:	Enlightenment XML libraries
Group:		System/Libraries
Provides:	%name = %version-%release

%description -n %libname
Exml libraries.

%package -n %libnamedev
Summary:  Exml headers, static libraries, documentation and test programs
Group:    System/Libraries
Requires: %libname = %epoch:%version
Provides: lib%{name}-devel = %epoch:%version-%release
Provides: %{name}-devel = %epoch:%version-%release

%description -n %libnamedev
Headers, static libraries, test programs and documentation for EXML.

%prep
%setup -q -n %name-%version

%build
./autogen.sh
%configure2_5x
%make

%install
rm -fr $RPM_BUILD_ROOT
%makeinstall

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

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
%{_includedir}/*

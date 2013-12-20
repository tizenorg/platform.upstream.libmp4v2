Name:       libmp4v2
Summary:    MPEG-4 library
Version:    2.0.0
Release:    0
Group:      Multimedia/Libraries
License:    LGPL-2.1
Source:	    %{name}-%{version}.tar.gz
Url:	    http://code.google.com/p/mp4v2/

%description
Description: %{summary}

%package devel
Summary: MP4v2 headers, static libraries, and documentation
Requires: %{name} = %{version}

%description devel
Headers, static libraries, and documentation for libmp4v2

%prep
%setup -q -n %{name}-%{version}

%build
%configure

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root)
%doc README
%license COPYING
%{_libdir}/*.so.*
%{_bindir}/*
%{_prefix}/share/man/man1/*

%files devel
%defattr(-, root, root)
%{_includedir}/*
%{_libdir}/*.so

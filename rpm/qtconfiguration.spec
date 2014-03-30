Name:           qtconfiguration
Summary:        Qt Configuration library
Version:        0.2.1
Release:        1

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License:        LGPLv2 with exceptions or GPLv3 with exceptions

URL:            https://github.com/mauios/qtconfiguration
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(dconf)
BuildRequires:  cmake
Requires:       dconf
Requires:       libdconf1
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig


%description
Settings API with change notifications.


%package devel
Summary:    Development files for %{name}
Group:      Development/System
Requires:   %{name} = %{version}-%{release}
Requires:   dconf-devel

%description devel
%{summary}


%prep
%setup -q -n %{name}-%{version}/upstream


%build
%cmake . \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo
make %{?jobs:-j%jobs}


%install
rm -rf %{buildroot}
%make_install
rm -f %{buildroot}/%{_libdir}/*.la


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%{_libdir}/libqtconfiguration.so.0*
%{_libdir}/hawaii/qml/Hawaii/Configuration/
%doc LICENSE.FDL
%doc LICENSE.GPL
%doc LICENSE.LGPL
%doc README.md


%files devel
%defattr(-,root,root,-)
%{_includedir}/QtConfiguration/
%{_libdir}/libqtconfiguration.so
%{_libdir}/cmake/QtConfiguration/

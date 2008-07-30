%define name	oorexx
%define version	3.1.2
%define release %mkrel 3
%define major 3
%define libname %mklibname %name %major
%define develname %mklibname %name -d

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Open Object Rexx

Group:          Development/Other
License:        CPL
URL:            http://www.oorexx.org
Source0:        http://switch.dl.sourceforge.net/sourceforge/oorexx/ooRexx-%{version}.tar.bz2
Source1:        http://switch.dl.sourceforge.net/sourceforge/oorexx/ooRexx-docs-%{version}-pdf.tar.bz2
Patch0:         oorexx-paths.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
ExcludeArch:    x86_64
Provides:	rexx

%description
Open Object Rexx is an object-oriented scripting language. The
language is designed for "non-programmer" type users, so it is easy to
learn and easy to use, and provides an excellent vehicle to enter the
world of object-oriented programming without much effort.

It extends the procedural way of programming with object-oriented
features that allow you to gradually change your programming style as
you learn more about objects.

%package docs
Summary:        Documentation for ooRexx
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description docs
Open Object Rexx is an object-oriented scripting language. The
language is designed for "non-programmer" type users, so it is easy to
learn and easy to use, and provides an excellent vehicle to enter the
world of object-oriented programming without much effort.

It extends the procedural way of programming with object-oriented
features that allow you to gradually change your programming style as
you learn more about objects.

This package contains most of the documentation for ooRexx. It is
separate from the main package due to its large size.

%package -n %libname
Group: System/Libraries
Summary: Shared libraries for oorexx
Provides: librexx%major = %version-%release

%description -n %libname
Open Object Rexx is an object-oriented scripting language. The
language is designed for "non-programmer" type users, so it is easy to
learn and easy to use, and provides an excellent vehicle to enter the
world of object-oriented programming without much effort.

It extends the procedural way of programming with object-oriented
features that allow you to gradually change your programming style as
you learn more about objects.

%package -n %develname
Group: Development/C
Summary: Development libraries for oorexx
Requires: %libname = %version
Provides: %name-devel = %version-%release
Provides: rexx-devel = %version-%release

%description -n %develname
Open Object Rexx is an object-oriented scripting language. The
language is designed for "non-programmer" type users, so it is easy to
learn and easy to use, and provides an excellent vehicle to enter the
world of object-oriented programming without much effort.

It extends the procedural way of programming with object-oriented
features that allow you to gradually change your programming style as
you learn more about objects.

%prep
%setup -q -n ooRexx-%{version}
%setup -q -D -T -a 1 -n ooRexx-%{version}
%patch0 -p1 -b .paths

%build
%configure --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f '{}' ';'
rm -fr samples/**/.deps
rm -f $RPM_BUILD_ROOT%{_datadir}/ooRexx/rexx.csh
rm -f $RPM_BUILD_ROOT%{_datadir}/ooRexx/rexx.sh
mv $RPM_BUILD_ROOT%{_bindir}/rxftp.cls $RPM_BUILD_ROOT%{_datadir}/ooRexx
mv $RPM_BUILD_ROOT%{_bindir}/rxregexp.cls $RPM_BUILD_ROOT%{_datadir}/ooRexx
chmod 0644 $RPM_BUILD_ROOT%{_datadir}/ooRexx/*

# remove cruft
rm -f $RPM_BUILD_ROOT%{_datadir}/ooRexx/{*.rex,readme}
find . -name .deps | xargs rm -fr
rm -fr samples/windows

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root,-)
%doc CPLv1.0.txt readme.pdf
%{_bindir}/rexx
%{_bindir}/rexxc
%{_bindir}/rxdelipc
%{_bindir}/rxmigrate
%{_bindir}/rxqueue
%{_bindir}/rxsubcom
%{_datadir}/ooRexx
%{_mandir}/man*/*

%files docs
%defattr(-,root,root,-)
%doc rexxpg.pdf rexxref.pdf rxftp.pdf rxmath.pdf rxsock.pdf
%doc samples README.txt

%files -n %develname
%defattr(-,root,root,-)
%{_includedir}/rexx.h
%{_libdir}/lib*.so
%{_bindir}/oorexx-config

%files -n %libname
%defattr(-,root,root,-)
%doc CPLv1.0.txt
%{_libdir}/lib*.so.*


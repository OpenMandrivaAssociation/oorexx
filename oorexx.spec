%define _disable_ld_no_undefined 1

%define major 4
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:		oorexx
Version:	4.1.0
Release:	1
Summary:	Open Object Rexx

Group:		Development/Other
License:	CPL
URL:		http://www.oorexx.org
Source0:	http://switch.dl.sourceforge.net/sourceforge/oorexx/ooRexx-%{version}-source.tar.gz
Source1:	http://switch.dl.sourceforge.net/sourceforge/oorexx/ooRexx-%{version}-pdf.zip
Patch0:		oorexx-4.1.0-paths.patch
Patch1:		oorexx-4.1.0-sfmt.patch
BuildRequires:	byacc
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
Summary:	Documentation for ooRexx
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

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

%package -n %{libname}
Group:		System/Libraries
Summary:	Shared libraries for oorexx

%description -n %{libname}
Open Object Rexx is an object-oriented scripting language. The
language is designed for "non-programmer" type users, so it is easy to
learn and easy to use, and provides an excellent vehicle to enter the
world of object-oriented programming without much effort.

It extends the procedural way of programming with object-oriented
features that allow you to gradually change your programming style as
you learn more about objects.

%package -n %{develname}
Group:		Development/C
Summary:	Development libraries for oorexx
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	rexx-devel = %{version}-%{release}

%description -n %{develname}
Open Object Rexx is an object-oriented scripting language. The
language is designed for "non-programmer" type users, so it is easy to
learn and easy to use, and provides an excellent vehicle to enter the
world of object-oriented programming without much effort.

It extends the procedural way of programming with object-oriented
features that allow you to gradually change your programming style as
you learn more about objects.

%prep
%setup -q -c -n ooRexx-%{version}
%setup -q -D -T -a 1 -n ooRexx-%{version}
%patch0 -p1 -b .paths
%patch1 -p1

%build
%configure2_5x --disable-static
%make LIBS="-lpthread -ldl"

%install
%makeinstall_std

rm -fr samples/**/.deps
rm -f %{buildroot}%{_datadir}/ooRexx/rexx.csh
rm -f %{buildroot}%{_datadir}/ooRexx/rexx.sh
chmod 0644 %{buildroot}%{_datadir}/ooRexx/*

# remove cruft
rm -f %{buildroot}%{_datadir}/ooRexx/{*.rex,readme}
find . -name .deps | xargs rm -fr
rm -fr samples/windows

%files
%doc CPLv1.0.txt ReleaseNotes
%{_bindir}/rexx
%{_bindir}/rexxc
%{_bindir}/rexximage
%{_bindir}/rxapi
%{_bindir}/rxapid
%{_bindir}/rxqueue
%{_bindir}/rxsubcom
%{_datadir}/ooRexx
%{_mandir}/man*/*

%files docs
%doc readme.pdf rexxpg.pdf rexxref.pdf rxftp.pdf rxmath.pdf rxsock.pdf

%files -n %{develname}
%{_bindir}/oorexx-config
%{_libdir}/lib*.so
%{_includedir}/*.h

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*


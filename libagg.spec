Summary:	Anti-Grain Geometry (AGG) library
Name:		libagg
Version:	2.5
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://www.antigrain.com/agg-%{version}.tar.gz
# Source0-md5:	0229a488bc47be10a2fee6cf0b2febd6
Patch0:		%{name}-libs.patch
Patch1:		%{name}-am.patch
URL:		http://www.antigrain.com/
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		skip_post_check_so	libaggplatformsdl.so.*.*.* libaggplatformX11.so.*.*.*

%description
Anti-Grain Geometry (AGG) is a general purpose graphical toolkit
written completely in standard and platform independent C++. It can be
used in many areas of computer programming where high quality 2D
graphics is an essential part of the project.

%package devel
Summary:	Support files necessary to compile applications with agg
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header and support files necessary to compile applications using agg.

%prep
%setup -qn agg-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-gpc \
	--disable-static
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc authors copying readme
%attr(755,root,root) %ghost %{_libdir}/libagg.so.2
%attr(755,root,root) %ghost %{_libdir}/libaggfontfreetype.so.2
%attr(755,root,root) %ghost %{_libdir}/libaggplatformX11.so.2
%attr(755,root,root) %ghost %{_libdir}/libaggplatformsdl.so.2
%attr(755,root,root) %{_libdir}/libagg.so.*.*.*
%attr(755,root,root) %{_libdir}/libaggfontfreetype.so.*.*.*
%attr(755,root,root) %{_libdir}/libaggplatformX11.so.*.*.*
%attr(755,root,root) %{_libdir}/libaggplatformsdl.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/agg2
%{_pkgconfigdir}/libagg.pc
%{_aclocaldir}/libagg.m4


Summary:	Thread pool for libdispatch
Summary(pl.UTF-8):	Pula wątkow dla libdispatch
Name:		libpthread_workqueue
Version:	0.9
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libpwq/%{name}-%{version}.tar.gz
# Source0-md5:	57910365f4741aaac533aa4344a21497
Patch0:		%{name}-link.patch
URL:		http://sourceforge.net/projects/libpwq/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libpthread_workqueue is a portable implementation of the
pthread_workqueue API first introduced in Mac OS X. It is primarily
intended for use with libdispatch but can be used as a general purpose
thread pool library for C programs.

%description -l pl.UTF-8
libpthread_workqueue to przenośna implementacja API pthread_workqueue,
które pojawiło się po raz pierwszy w systemie Mac OS X. Głównym celem
jest użycie w libdispatch, ale może być używana jako ogólna biblioteka
wątków dla programów w języku C.

%package devel
Summary:	Header files for libpthread_workqueue library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libpthread_workqueue
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libpthread_workqueue library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libpthread_workqueue.

%package static
Summary:	Static libpthread_workqueue library
Summary(pl.UTF-8):	Statyczna biblioteka libpthread_workqueue
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libpthread_workqueue library.

%description static -l pl.UTF-8
Statyczna biblioteka libpthread_workqueue.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libpthread_workqueue.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libpthread_workqueue.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpthread_workqueue.so
%{_libdir}/libpthread_workqueue.la
%{_includedir}/pthread_workqueue.h
%{_mandir}/man3/pthread_workqueue.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libpthread_workqueue.a

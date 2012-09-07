Summary:	Python bindings for E_Dbus library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki E_Dbus
Name:		python-e_dbus
Version:	1.7.0
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Python
Source0:	http://download.enlightenment.org/releases/BINDINGS/python/%{name}-%{version}.tar.bz2
# Source0-md5:	40b479444bb06147429a276127981890
URL:		http://trac.enlightenment.org/e/wiki/Python
BuildRequires:	e_dbus-devel >= 1.7.0
BuildRequires:	epydoc
BuildRequires:	python-Cython >= 0.13
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-dbus-devel >= 0.83
BuildRequires:	rpm-pythonprov
BuildRequires:	pkgconfig >= 1:0.22
Requires:	e_dbus >= 1.7.0
Requires:	python-dbus >= 0.83
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for E_Dbus library.

%description -l pl.UTF-8
Wiązania Pythona do biblioteki E_Dbus.

%package devel
Summary:	Python bindings for E_Dbus library - development files
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki E_Dbus - pliki programistyczne
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	e_dbus-devel >= 1.7.0
Requires:	python-dbus-devel >= 0.83

%description devel
Python bindings for E_Dbus library - development files.

%description devel -l pl.UTF-8
Wiązania Pythona do biblioteki E_Dbus - pliki programistyczne.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/e_dbus.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{py_sitedir}/e_dbus.so

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/python-edbus.pc

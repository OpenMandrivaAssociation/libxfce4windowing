%define api		0
%define major		0
%define libname		%mklibname xfce4windowing
%define libnameui	%mklibname xfce4windowingui
%define girname		%mklibname xfce4windowing-gir
%define girnameui	%mklibname xfce4windowingui-gir
%define devname		%mklibname xfce4windowing -d

%define url_ver %(echo %{version} | cut -d. -f1,2)

Name:		libxfce4windowing
Summary:	Windowing concept abstraction library for X11 and Wayland
Version:	4.19.3
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/Xfce
Url:		https://gitlab.xfce.org/xfce/libxfce4windowing
Source0:	https://archive.xfce.org/src/xfce/libxfce4windowing/%{url_ver}/libxfce4windowing-%{version}.tar.bz2
BuildRequires:	xfce4-dev-tools
BuildRequires:	pkgconfig(gdk-3.0)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gdk-wayland-3.0)
BuildRequires:	pkgconfig(gdk-x11-3.0)
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libwnck-3.0)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-scanner)

%description
Libxfce4windowing is an abstraction library that attempts to present windowing
concepts (screens, toplevel windows, workspaces, etc.) in a
windowing-system-independent manner.

Currently, X11 is fully supported, via libwnck. Wayland is partially supported,
through various Wayland protocol extensions. However, the full range of
operations available on X11 is not available on Wayland, due to missing
features in these protocol extensions.

%package -n %{libname}
Summary:	X11/Wayland windowing utility library for Xfce
Group:		System/Libraries

%description -n %{libname}
Libxfce4windowing is an abstraction library that attempts to present windowing
concepts (screens, toplevel windows, workspaces, etc.) in a
windowing-system-independent manner.

%package -n %{libnameui}
Summary:	X11/Wayland windowing utility library for Xfce - extra widgets
Group:		System/Libraries

%description -n %{libnameui}
Libxfce4windowingui is a UI widget utility library that makes use of
libxfce4windowing primitives.

%package -n %{girname}
Summary:	GObject Introspection interface description for Libxfce4windowing
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for Libxfce4windowing.

%package -n %{girnameui}
Summary:	GObject Introspection interface description for Libxfce4windowingui
Group:		System/Libraries
Requires:	%{libnameui} = %{version}-%{release}

%description -n %{girnameui}
GObject Introspection interface description for Libxfce4windowingui.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libnameui} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Requires:	%{girnameui} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	xfce4windowing-devel = %{version}-%{release}

%description -n %{devname}
Libxfce4windowing is an abstraction library that attempts to present windowing
concepts (screens, toplevel windows, workspaces, etc.) in a
windowing-system-independent manner.

Currently, X11 is fully supported, via libwnck. Wayland is partially supported,
through various Wayland protocol extensions. However, the full range of
operations available on X11 is not available on Wayland, due to missing
features in these protocol extensions.

%prep
%autosetup -p1

%build
#xdt_autogen
%configure
%make_build

%install
%make_install

%find_lang %{name}

%files -n %{libname} -f %{name}.lang
%license COPYING
%{_libdir}/libxfce4windowing-%{api}.so.%{major}{,.*}

%files -n %{libnameui}
%license COPYING
%{_libdir}/libxfce4windowingui-%{api}.so.%{major}{,.*}

%files -n %{girname}
%license COPYING
%{_libdir}/girepository-1.0/Libxfce4windowing-%{api}.%{major}.typelib

%files -n %{girnameui}
%license COPYING
%{_libdir}/girepository-1.0/Libxfce4windowingui-%{api}.%{major}.typelib

%files -n %{devname}
%doc NEWS README*
%doc %{_datadir}/gtk-doc/html/libxfce4windowing{,ui}/
%dir %{_includedir}/xfce4/
%{_includedir}/xfce4/libxfce4windowing{,ui}/
%{_libdir}/libxfce4windowing{,ui}-%{api}.so
%{_libdir}/pkgconfig/libxfce4windowing{,ui}-%{api}.pc
%{_libdir}/pkgconfig/libxfce4windowing-x11-0.pc
%{_datadir}/gir-1.0/Libxfce4windowing-%{api}.%{major}.gir
%{_datadir}/gir-1.0/Libxfce4windowingui-%{api}.%{major}.gir

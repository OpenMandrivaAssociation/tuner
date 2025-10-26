%define _unpackaged_files_terminate_build 1
%define app_id org.altlinux.Tuner
%define namespace Tuner
%define api_ver 1

%define libname %mklibname tuner
%define devname %mklibname -d tuner
%define girname %mklibname tuner-gir

#def_enable docs

Name: tuner
Version: 0.5.0
Release: 1
Summary: Extensible control center
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://altlinux.space/alt-gnome/Tuner
# fetch from git
Source0:  Tuner-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(blueprint-compiler)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(libpeas-2)
#BuildRequires: gir(Peas) = 2
#BuildRequires: gir(Gee) = 0.8
#BuildRequires: gir(Adw) = 1
BuildRequires: pkgconfig(gobject-introspection-1.0)

Requires: libadwaita-common
Requires: %{_lib}peas2-gir
Requires: %{_lib}gee-gir0.8

%description
Tuner is the home for your additional system settings, components,
applications, and whatever else you want!

Extended control over the interface and functions using plugins.
The interface is adapted to different device sizes.
Easy installation from the repository.
You can create your own plugins without affecting the main program code.
Easy creation of plugins working with dconf and unlimited plugin functionality
thanks to libpeas.

%package -n %{libname}
Summary: Versatile library for creating extensible apps and plugins for them
Group: System/Libraries
Requires: %{_lib}peas2

%description -n %{libname}
lib%name is a library designed to support both core application development
and plugin integration. It provides several build-in widgets and API to
create and extend pages. It also provides API to add plugins to your own app.

%package -n %{devname}
Summary: Development files for lib%name
Group: Development/C
Requires:	%{libname} = %{EVRD}
Requires:	%{girname} = %{EVRD}

%description -n %{devname}
This package contains development libraries and header files
that are needed to write applications that use lib%name.

%package -n %{girname}
Summary: GObject introspection data for the lib%name
Group: System/Libraries
Requires:	%{libname} = %{EVRD}

%description -n %{girname}
GObject introspection data for the lib%name.

%prep
%autosetup -n Tuner-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang tuner

%files -f tuner.lang
%{_bindir}/%name
%{_datadir}/applications/org.altlinux.Tuner.desktop
%{_datadir}/metainfo/%app_id.metainfo.xml
%{_iconsdir}/hicolor/*/apps/%{app_id}*.svg
%{_datadir}/glib-2.0/schemas/%app_id.gschema.xml
%doc README.md

%files -n %{libname}
%{_libdir}/lib%name-%api_ver.so.*

%files -n %{devname}
%doc %{_datadir}/doc/%{name}/*
%{_libdir}/lib%name-%api_ver.so
%{_includedir}/%name-%api_ver.h
%{_libdir}/pkgconfig/tuner-1.pc
%{_datadir}/vala/vapi/tuner-1.deps
%{_datadir}/vala/vapi/tuner-1.vapi
%{_datadir}/gir-1.0/Tuner-1.gir

%files -n %{girname}
%{_libdir}/girepository-1.0/Tuner-1.typelib


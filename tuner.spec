%define _unpackaged_files_terminate_build 1
%define app_id org.altlinux.Tuner
%define namespace Tuner
%define api_ver 1

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

%description
Tuner is the home for your additional system settings, components,
applications, and whatever else you want!

Extended control over the interface and functions using plugins.
The interface is adapted to different device sizes.
Easy installation from the repository.
You can create your own plugins without affecting the main program code.
Easy creation of plugins working with dconf and unlimited plugin functionality
thanks to libpeas.

%package -n lib%name
Summary: Versatile library for creating extensible apps and plugins for them
Group: System/Libraries
Requires: libpeas2-python3-loader

%description -n lib%name
lib%name is a library designed to support both core application development
and plugin integration. It provides several build-in widgets and API to
create and extend pages. It also provides API to add plugins to your own app.

%package -n lib%name-devel
Summary: Development files for lib%name
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
This package contains development libraries and header files
that are needed to write applications that use lib%name.

%package -n lib%name-devel-doc
Summary: Development documentation for lib%name
Group: Development/Documentation
Conflicts: lib%name < %version-%release
BuildArch: noarch

%description -n lib%name-devel-doc
This package contains development documentation for the lib%name.

%package -n lib%name-gir
Summary: GObject introspection data for the lib%name
Group: System/Libraries
Requires: lib%name = %EVR

%description -n lib%name-gir
GObject introspection data for the lib%name.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the lib%name
Group: Development/Other
BuildArch: noarch
Requires: lib%name-devel = %EVR
Requires: lib%name-gir = %EVR

%description -n lib%name-gir-devel
GObject introspection devel data for the lib%name.

%prep
%autosetup -n Tuner-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%app_id.desktop
%_datadir/metainfo/%app_id.metainfo.xml
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%doc README.md

%files -n lib%name
%_libdir/lib%name-%api_ver.so.*

%files -n lib%name-devel
%_libdir/lib%name-%api_ver.so
%_includedir/%name-%api_ver.h
%_pkgconfigdir/%name-%api_ver.pc
%_vapidir/%name-%api_ver.deps
%_vapidir/%name-%api_ver.vapi

%files -n lib%name-gir
%_typelibdir/%namespace-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/%namespace-%api_ver.gir

%files -n lib%name-devel-doc
%_datadir/doc/%name/*

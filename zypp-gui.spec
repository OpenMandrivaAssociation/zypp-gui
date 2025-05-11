Name:           zypp-gui
Version:        0.4.1
Release:        1
Summary:        Update the system, search, install and remove the package, configure the repos.
License:        GPL-2.0-or-later
Group:          System/GUI
URL:            https://github.com/sunwxg/zypp-gui
Source0:        https://github.com/sunwxg/zypp-gui/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        additional.json

BuildRequires:  pkgconfig(blueprint-compiler)
BuildRequires:  rust-packaging
BuildRequires:  meson
BuildRequires:  rust
BuildRequires:  zstd
BuildRequires:  gettext
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 3.11.5
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20.0
BuildRequires:  pkgconfig(gtk4) >= 4.8
BuildRequires:  pkgconfig(libadwaita-1) >= 1.2.alpha
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(packagekit-glib2) >= 1.1.0
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  python-gobject3
BuildRequires:  python-gi
Requires:       packagekit
Requires:       pkexec

%description
Application can update the system, search, install and remove the package, configure the repos. It achieves some functions of command zypper.

%prep
%autosetup -a1 -p1
%cargo_prep -v vendor
cat >>.cargo/config.toml <<EOF

[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

EOF

%build
%meson
%meson_build

%install
%meson_install
install -D -m 644 %{SOURCE2} %{buildroot}%{_prefix}/share/%{name}/additional.json

%check
%meson_test

%files
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/mod-repo
%{_datadir}/%{name}/
%{_datadir}/applications/zypp.gui.desktop
%{_datadir}/glib-2.0/schemas/zypp.gui.gschema.xml
%{_datadir}/dbus-1/services/zypp.gui.service
%{_datadir}/icons/hicolor/scalable/apps/zypp.gui.svg
%{_datadir}/icons/hicolor/symbolic/apps/zypp.gui-symbolic.svg
%{_datadir}/icons/hicolor/16x16/places/
%{_datadir}/polkit-1/actions/zypp.gui.policy
%{_sysconfdir}/xdg/autostart/zypp-gui-service.desktop
%{_datadir}/metainfo/zypp.gui.metainfo.xml

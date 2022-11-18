%define		_snapid H8ZpNgIoPyvmkgxOWw5MSzsXK1wRZiHn
%define		_snaprev 11

Name:           authy
Version:        2.2.1
Release:        2%{?dist}
Summary:        Two factor authentication desktop application
ExclusiveArch:  x86_64
License:        Proprietary
URL:            https://authy.com/
Source0:        https://api.snapcraft.io/api/v1/snaps/download/%{_snapid}_%{_snaprev}.snap
NoSource:       0
BuildRequires:  squashfs-tools
Requires:       nss
Requires:       gtk3

%description
Two factor authentication desktop application

%prep
%{_sbindir}/unsquashfs -q -f -d %{_builddir}/authy %{SOURCE0}

%build

%install
install -d %{buildroot}/opt/authy
cp -r %{_builddir}/authy/. %{buildroot}/opt/authy

# Desktop Entry
sed -i 's|${SNAP}/meta/gui/icon.png|authy|g' %{buildroot}/opt/authy/meta/gui/authy.desktop
install -Dm644 %{buildroot}/opt/authy/meta/gui/authy.desktop -t %{buildroot}/usr/share/applications
install -Dm644 %{buildroot}/opt/authy/meta/gui/icon.png %{buildroot}/usr/share/pixmaps/authy.png

# Clean up unnecessary files
rm -rf %{buildroot}/opt/authy/{data-dir,gnome-platform,lib,meta,scripts,usr,*.sh}

# Symlink binary to /usr/bin
install -d %{buildroot}%{_bindir}

# Fixes build error
rm -f %{buildroot}%{_bindir}/authy
ln -s /opt/authy/authy %{buildroot}%{_bindir}

%files
/opt/authy/*
%{_bindir}/authy
%{_datarootdir}/*

%changelog
* Fri Nov 18 2022 th1nhhdk <th1nhhdk@tutanota.com>
- Bump version for Fedora Linux 37

* Tue Oct 04 2022 th1nhhdk <th1nhhdk@tutanota.com>
- Spec file cleanup

* Thu Jul 28 2022 th1nhhdk <th1nhhdk@tutanota.com>
- Initial release

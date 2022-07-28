%define		_snapid H8ZpNgIoPyvmkgxOWw5MSzsXK1wRZiHn
%define		_snaprev 11

Name:		authy
Version:	2.2.1
Release:	1%{?dist}
Summary:	Two factor authentication desktop application
ExclusiveArch:	x86_64
License:	Proprietary
URL:		https://authy.com/
Source0:	https://api.snapcraft.io/api/v1/snaps/download/%{_snapid}_%{_snaprev}.snap
NoSource:	0
BuildRequires:	squashfs-tools
Requires:	nss
Requires:	gtk3

%description
Two factor authentication desktop application

%prep
echo "Extracting snap file..."
%{_sbindir}/unsquashfs -q -f -d "%{_builddir}/%{name}" "%{SOURCE0}"

%build
# Nothing to build

%install
%{__install} -d "%{buildroot}/opt/%{name}"
%{__cp} -r "%{_builddir}/%{name}/." "%{buildroot}/opt/%{name}"

# Desktop Entry
%{__sed} -i 's|${SNAP}/meta/gui/icon.png|authy|g' "%{buildroot}/opt/%{name}/meta/gui/authy.desktop"
%{__install} -Dm644 "%{buildroot}/opt/%{name}/meta/gui/authy.desktop" -t "%{buildroot}/usr/share/applications"
%{__install} -Dm644 "%{buildroot}/opt/%{name}/meta/gui/icon.png" "%{buildroot}/usr/share/pixmaps/authy.png"

# Clean up unnecessary files
%{__rm} -rf "%{buildroot}/opt/%{name}"/{data-dir,gnome-platform,lib,meta,scripts,usr,*.sh}

# Symlink binary to /usr/bin
%{__install} -d "%{buildroot}%{_bindir}"
# ???
%{__rm} -f "%{buildroot}%{_bindir}/authy"
%{__ln_s} "/opt/%{name}/authy" "%{buildroot}%{_bindir}"

%files
/opt/authy/*
%{_bindir}/authy
%{_datarootdir}/*

%changelog
* Thu Jul 28 2022 th1nhhdk <th1nhhdk@tutanota.com>
- Initial release

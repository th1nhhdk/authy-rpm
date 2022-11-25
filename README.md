# authy-rpm
Authy Desktop rpm spec file, ported from https://aur.archlinux.org/packages/authy

## How to install

- Download `authy-2.2.1-2.fc37.nosrc.rpm` from Releases page

```
# dnf install rpm-build
$ rpm -Uvh authy-2.2.1-2.fc37.nosrc.rpm
$ wget -vP ~/rpmbuild/SOURCES https://api.snapcraft.io/api/v1/snaps/download/H8ZpNgIoPyvmkgxOWw5MSzsXK1wRZiHn_11.snap
# dnf builddep authy.spec
$ rpmbuild --clean -ba ~/rpmbuild/SPECS/authy.spec
# rpm -iv ~/rpmbuild/RPMS/x86_64/authy-2.2.1-2.fc37.x86_64.rpm
```

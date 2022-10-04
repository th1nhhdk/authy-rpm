# authy-spec
Authy rpm spec file, ported from https://aur.archlinux.org/packages/authy

## How to install
```
# dnf install rpmdevtools
$ rpmdev-setuptree
$ rpm -Uvh authy-2.2.1-1.fc36.nosrc.rpm
$ wget -vP ~/rpmbuild/SOURCES https://api.snapcraft.io/api/v1/snaps/download/H8ZpNgIoPyvmkgxOWw5MSzsXK1wRZiHn_11.snap
$ rpmbuild -ba --clean ~/rpmbuild/SPECS/authy.spec
# rpm -iv ~/rpmbuild/RPMS/x86_64/authy-2.2.1-1.*.x86_64.rpm
```

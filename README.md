# authy-spec
Authy rpm spec file, ported from https://aur.archlinux.org/packages/authy

## How to install package:
```
dnf install rpmdevtools
rpmdev-setuptree
rpm -Uvh authy-2.2.1-1.fc36.nosrc.rpm
rpmbuild -ba --clean ~/rpmbuild/SPECS/authy.spec
```

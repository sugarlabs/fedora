# fedora build spec files
## install
https://copr.fedorainfracloud.org/coprs/ignacio/sugar0.110/
```
dnf copr enable ignacio/sugar0.110`
dnf install sugar
dnf update
```
## update
```
# Force the metadata to expire and refresh
sudo sh -c 'echo [\"ignacio-sugar0.110\"] > /var/cache/dnf/expired_repos.json'
sudo dnf update
```

Extracted from [sam's copr](https://copr.fedorainfracloud.org/coprs/samtoday/sugar/)


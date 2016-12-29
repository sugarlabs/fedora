Name:          sugar-runner
Version:       0.110.0
Release:       1%{?dist}
Summary:       Sugar runner emulator for development
Group:         User Interface/Desktops
License:       GPLv2+
URL:           http://sugarlabs.org/
Source0:       http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: glib2-devel
BuildRequires: gobject-introspection-devel
BuildRequires: libX11-devel
BuildRequires: libXrandr-devel
Requires: sugar
Requires: xorg-x11-server-Xephyr

%description
sugar-runner allows to run sugar without using a display manager as usually
required by X desktops. You can run it either from a text console
or from inside another X session. By default it runs fullscreen but when inside
X you can specify the window size using the --resolution option.

%package devel
Summary: Development package for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%prep
%setup -q

# Fix desktop file
sed -i 's/Teaching/X-Teaching/' data/sugar-runner.desktop

%build
%configure --disable-static

make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'

#Remove libtool archives.
find %{buildroot} -type f -name "*.la" -delete

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%post
/sbin/ldconfig
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
/sbin/ldconfig
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_bindir}/sugar-runner
%{_libexecdir}/sugar-runner
%{_libdir}/girepository-1.0/SugarRunner-1.0.typelib
%{_libdir}/libsugarrunner.so.*
%{_datadir}/applications/sugar-runner.desktop
%{_datadir}/icons/hicolor/scalable/apps/sugar-xo.svg

%files devel
%{_libdir}/*.so
%{_datadir}/gir-1.0/SugarRunner-1.0.gir

%changelog
* Wed Dec 28 2016 Ignacio Rodríguez <ignacio@fedoraproject.org> 0.110.0-1
- Sugar 0.110.0 stable release

* Sun Mar  6 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.108.1-1
- Sugar 0.108.1 stable release

* Sat Feb 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.108.0-1
- Sugar 0.108.0 stable release

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.107.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.107.2-1
- Sugar 0.107.2 devel release

* Mon Jan 4  2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.107.1-1
- Sugar 0.107.1 devel release

* Fri Nov 27 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.107.0-1
- Sugar 0.107.0 devel release

* Tue Jul  7 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.106.0-1
- Sugar 0.106.0 stable release

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.105.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.105.2-1
- Sugar 0.105.2 development release

* Tue May 19 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.105.1-1
- Sugar 0.105.1 development release

* Tue Mar 10 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.104.1-1
- Sugar 0.104.1 stable release

* Sat Feb 14 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.104.0-1
- Sugar 0.104.0 stable release

* Sat Jan 17 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.103.2-1
- New upstream 0.103.2 development release

* Thu Dec 11 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.103.1-1
- New upstream 0.103.1 development release

* Thu Nov 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.103.0-1
- New upstream 0.103.0 development release

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.102.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.102.0-2
- Rebuilt for gobject-introspection 1.41.4

* Wed Jul  2 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.102.0-1
- Sugar 0.102.0 stable release

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.101.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb 15 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.2-1
- 0.101.2 devel release

* Sun Dec  8 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.1-1
- 0.101.1 devel release

* Wed Nov 27 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.100.1-2
- Add Requires on xorg-x11-server-Xephyr

* Fri Nov 22 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.100.1-1
- Sugar 0.100.1 stable release

* Fri Nov  1 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.100.0-1
- Sugar 0.100.0 stable release

* Mon Sep  2 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.3-2
- Initial review updates

* Thu Aug 15 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.3-1
- Initial Packaging

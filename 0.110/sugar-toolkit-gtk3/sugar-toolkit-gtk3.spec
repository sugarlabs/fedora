%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

%undefine _hardened_build

Summary: Sugar toolkit GTK+ 3
Name:    sugar-toolkit-gtk3
Version: 0.110.0
Release: 1%{?dist}
URL:     http://wiki.laptop.org/go/Sugar
Source0: http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.xz
Source1: macros.sugar
License: LGPLv2+
Group:   System Environment/Libraries

BuildRequires: alsa-lib-devel
BuildRequires: gettext-devel
BuildRequires: gtk3-devel
BuildRequires: gobject-introspection-devel
BuildRequires: intltool
BuildRequires: librsvg2-devel
BuildRequires: libSM-devel
BuildRequires: perl-XML-Parser
BuildRequires: pkgconfig
BuildRequires: python-devel
BuildRequires: pygtk2-codegen
BuildRequires: pygobject2-devel

Requires: dbus-python
Requires: gettext
Requires: pygobject3
Requires: python-dateutil
Requires: sugar-datastore
Requires: unzip
Requires: libwebkit2gtk

%description
Sugar is the core of the OLPC Human Interface. The toolkit provides
a set of widgets to build HIG compliant applications and interfaces
to interact with system services like presence and the datastore.
This is the toolkit depending on GTK3.

%package devel
Summary: Invokation information for accessing SugarExt-1.0
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the invocation information for accessing
the SugarExt-1.0 library through gobject-introspection.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}/%{_rpmconfigdir}/macros.d/
install -pm 644 %{SOURCE1} %{buildroot}/%{_rpmconfigdir}/macros.d/macros.sugar

%find_lang %name

#Remove libtool archives.
find %{buildroot} -type f -name "*.la" -delete

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%doc COPYING README
%{python_sitelib}/*
%{_bindir}/sugar-activity-web
%{_rpmconfigdir}/macros.d/macros.sugar
%{_libdir}/girepository-1.0/*.typelib
%{_libdir}/lib*.so.*
%{_bindir}/sugar-activity

%files devel
%{_libdir}/*.so
%{_datadir}/gir-1.0/*.gir

%changelog
* Wed Dec 28 2016 Ignacio Rodríguez <ignacio@fedoraproject.org> 0.110.0-1
- Sugar 0.110.0 stable release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.108.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Mar  6 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.108.1-2
- upload proper tar ball

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

* Tue Sep  8 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.106.0-2
- Disable hardened build until fixed upstream

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

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.101.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.5-1
- 0.101.5 devel release

* Sun Apr 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.4-1
- 0.101.4 devel release

* Sun Mar  9 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.3-1
- 0.101.3 devel release

* Tue Feb 18 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.101.2-2
- Install macros non-executable to %%{_rpmconfigdir}/macros.d.

* Sat Feb 15 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.2-1
- 0.101.2 devel release

* Sun Dec  8 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.1-1
- 0.101.1 devel release
- Drop GConf2 as we're using gsettings now

* Fri Nov  1 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.100.0-1
- Sugar 0.100.0 stable release

* Tue Oct 8  2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.4-1
- 0.99.4 devel release

* Sat Aug 10 2013 Daniel Drake <dsd@laptop.org> 0.99.1-2
- Add missing dependency on WebKit2, needed for web activities

* Wed Jul 31 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.1-1
- 0.99.1 devel release

* Sat Jul 13 2013 Daniel Drake <dsd@laptop.org> 0.99.0-2
- Remove dependency on simplejson, no longer required.

* Fri Jun 28 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.0-1
- 0.99.0 devel release

* Thu May 30 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.7-1
- Sugar 0.98.7 stable release

* Fri May 24 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.6-1
- Sugar 0.98.6 stable release

* Sat Feb 16 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.5-1
- Sugar 0.98.5 stable release

* Thu Jan 24 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.4-1
- Sugar 0.98.4 stable release

* Fri Dec 21 2012 Simon Schampijer <simon@laptop.org> - 0.98.3-1
- Sugar 0.98.3 stable release

* Tue Dec 18 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.2-1
- Sugar 0.98.2 stable release

* Mon Dec 10 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.1-1
- Sugar 0.98.1 stable release

* Thu Nov 29 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.0-1
- Sugar 0.98.0 stable release

* Tue Nov 27 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.13-1
- 0.97.13 devel release

* Sat Nov 24 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.12-1
- 0.97.12 devel release 

* Thu Nov 22 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.11-1
- 0.97.11 devel release

* Sat Nov 10 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.10-1
- 0.97.10 devel release

* Wed Nov  7 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.9-1
- 0.97.9 devel release

* Thu Oct 25 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.8-1
- 0.97.8 devel release

* Tue Oct 16 2012 Daniel Drake <dsd@laptop.org> 0.97.7-1
- 0.97.7 devel release

* Thu Oct 11 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.6-1
- 0.97.6 devel release

* Fri Oct  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.5-1
- 0.97.5 devel release

* Wed Sep 26 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.4-1
- 0.97.4 devel release

* Thu Sep 20 2012 Daniel Drake <dsd@laptop.org> - 0.97.3-1
- New development release

* Thu Sep 13 2012 Daniel Drake <dsd@laptop.org> - 0.97.2-1
- New development release

* Tue Aug 28 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.1-1
- 0.97.1 devel release

* Wed Aug 15 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.0-1
- 0.97.0 devel release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun  6 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.4-1
- 0.96.4 stable release

* Tue Jun  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.3-1
- 0.96.3 stable release

* Sat Jun  2 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.2-1
- 0.96.2 stable release

* Sun May 27 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.1-2
- Add gettext to Requires

* Sat May  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.1-1
- 0.96.1 stable release

* Tue Apr 24 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.0-1
- 0.96.0 stable release

* Thu Apr 19 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.6-1
- devel release 0.95.6

* Fri Mar 23 2012 Simon Schampijer <simon@laptop.org> - 0.95.5-1
- devel release 0.95.5

* Wed Mar 14 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.4-1
- devel release 0.95.4

* Mon Feb  6 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.3-1
- devel release 0.95.3

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 24 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.2-2
- Fix devel dependencies

* Thu Dec 22 2011 Simon Schampijer <simon@laptop.org> - 0.95.2-1
- devel release 0.95.2
- incorporated review comments

* Sun Dec 11 2011 Simon Schampijer <simon@laptop.org> - 0.95.1-1
- devel release 0.95.1

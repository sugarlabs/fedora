%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Summary: Sugar toolkit
Name: sugar-toolkit
Version: 0.110.0
Release: 1%{?dist}
URL: http://wiki.laptop.org/go/Sugar
Source0: http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.bz2
Source1: macros.sugar
License: LGPLv2+
Group: System Environment/Libraries

BuildRequires: alsa-lib-devel
BuildRequires: gettext-devel
BuildRequires: gtk2-devel
BuildRequires: intltool
BuildRequires: libSM-devel
BuildRequires: perl-XML-Parser
BuildRequires: pkgconfig
BuildRequires: pygtk2-devel

Requires: dbus-python
Requires: gettext
Requires: gnome-python2-gconf
Requires: gnome-python2-rsvg
Requires: hippo-canvas-python
Requires: pygtk2
Requires: python-simplejson
Requires: python-dateutil
Requires: sugar-base
Requires: sugar-datastore
Requires: unzip

%description
Sugar is the core of the OLPC Human Interface. The toolkit provides
a set of widgets to build HIG compliant applications and interfaces
to interact with system services like presence and the datastore.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}/%{_rpmconfigdir}/macros.d
install -pm 644 %{SOURCE1} %{buildroot}/%{_rpmconfigdir}/macros.d/macros.sugar

%find_lang %name

#Remove libtool archives.
find %{buildroot} -type f -name "*.la" -delete

%files -f %{name}.lang
%doc COPYING README
%{python_sitelib}/*
%{_rpmconfigdir}/macros.d/macros.sugar

%changelog
* Wed Dec 28 2016 Ignacio Rodríguez <ignacio@fedoraproject.org> 0.110.0-1
- Sugar 0.110.0 stable release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98.1-11
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.98.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 24 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.1-8
- Drop dep on sugar-presence-service

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 16 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.1-6
- Fix rpm macro install permissions

* Thu Jun 12 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.98.1-5
- Fix rpm macro location (#1074286)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.1-3
- Update rpm macro location (RHBZ 1074286)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 16 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.1-1
- Sugar 0.98.1 stable release

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 29 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.0-1
- Sugar 0.98 stable release

* Tue Nov 27 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.2-1
- 0.97.2 devel release

* Sat Oct  6 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.1-2
- Add gnome-python2-gconf dependency

* Fri Oct  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.1-1
- 0.97.1 devel release

* Tue Aug 21 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.0-1
- 0.97.0 devel release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

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

* Wed Mar  7 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.4-1
- devel release 0.95.4

* Fri Mar  2 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.3-1
- devel release 0.95.3

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 21 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.2-1
- devel release 0.95.2

* Tue Oct 25 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.1-1
- devel release 0.95.1

* Thu Sep 29 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.94.0-1
- 0.94.0 stable release

* Tue Sep 20 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.93.4-1
- 0.93.4 dev release

* Wed Sep  7 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.93.3-1
- 0.93.3 dev release

* Fri Aug 19 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.93.2-1
- 0.93.2 dev release

* Mon Jul 25 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.92.4-1
- 0.92.4

* Thu Jun  9 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.92.2-1
- 0.92.2 release

* Thu Apr 14 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.92.1-1
- 0.92.1 release

* Mon Feb 28 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.92.0-1
- 0.92.0 release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb  3 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.90.2-3
- Drop fonts patch as its causing issues

* Sat Jan 29 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.90.2-2
- bump build

* Fri Oct 15 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.90.2-1
- 0.90.2 release

* Tue Oct  5 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.90.1-1
- 0.90.1 release

* Wed Sep 29 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.90.0-1
- 0.90.0 stable release

* Mon Aug 30 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.89.5-1
- New upstream devel 0.89.5 release

* Wed Aug 25 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.89.4-1
- New upstream devel 0.89.4 release

* Tue Aug 17 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.89.3-1
- New upstream devel 0.89.3 release

* Tue Aug 17 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.89.2-1
- New upstream devel 0.89.2 release

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.89.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 14 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.89.1-1
- New upstream devel 0.89.1 release

* Thu Jun  3 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.88.1-1
- New upstream stable 0.88.1 release

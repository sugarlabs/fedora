%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name: sugar-datastore
Version: 0.110.0
Release: 1%{?dist}
Summary: Sugar Datastore

Group: Development/Libraries
License: GPLv2+
URL: http://sugarlabs.org/
Source0: http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.xz

BuildRequires: python-devel
Requires: xapian-bindings-python

%description
sugar-datastore is a simple log like datastore able to connect with multiple
backends. The datastore supports connectionig and disconnecting from
backends on the fly to help the support the limit space/memory
characteristics of the OLPC system and the fact that network services
may become unavailable at times

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'

#Remove libtool archives.
find %{buildroot} -type f -name "*.la" -delete

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS NEWS README
%{python_sitelib}/*
%{_bindir}/*
%{_datadir}/dbus-1/services/*.service

%changelog
* Wed Dec 28 2016 Ignacio Rodríguez <ignacio@fedoraproject.org> 0.110.0-1
- Sugar 0.110.0 stable release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.108.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

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

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.102.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul  2 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.102.0-1
- Sugar 0.102.0 stable release

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.101.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.0-1
- 0.101.0 devel release

* Fri Nov  1 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.100.0-1
- Sugar 0.100.0 stable release

* Tue Oct 8  2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.2-1
- 0.99.2 devel release

* Wed Jul 31 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.1-1
- 0.99.1 devel release

* Fri Jun 28 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.0-1
- 0.99.0 devel release

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 18 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.1-1
- Sugar 0.98.1 stable release

* Thu Nov 29 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.0-1
- Sugar 0.98.1 stable release

* Sat Nov 10 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.4-1
- 0.97.4 devel release

* Wed Nov  7 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.3-1
- 0.97.3 devel release

* Wed Nov  7 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.2-1
- 0.97.2 devel release

* Fri Oct  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.1-1
- 0.97.1 devel release

* Mon Sep 24 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.0-1
- 0.97.0 devel release
- Move from cjson to mainline python json

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 24 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.0-1
- 0.96.0 stable release

* Wed Mar 14 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.2-1
- devel release 0.95.2

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 25 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.1-1
- devel release 0.95.1

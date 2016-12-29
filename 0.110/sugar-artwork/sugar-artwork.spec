Summary: Artwork for Sugar look-and-feel
Name: sugar-artwork
Version: 0.110.0
Release: 1%{?dist}
URL: http://sugarlabs.org
Group: User Interface/Desktops
License:  ASL 2.0
Source0: http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.xz

BuildRequires: gtk2-devel
BuildRequires: gtk3-devel
BuildRequires: xorg-x11-apps
BuildRequires: perl-XML-Parser
BuildRequires: python
BuildRequires: python-empy
BuildRequires: icon-naming-utils
BuildRequires: icon-slicer

Requires: gtk2 gtk3

%description
sugar-artwork contains the themes and icons that make up the OLPC default 
look and feel.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

find %{buildroot} -type f -name "*.la" -delete

%post
touch --no-create %{_datadir}/icons/sugar || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/sugar || :

%postun
touch --no-create %{_datadir}/icons/sugar || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/sugar || :

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc COPYING
%{_datadir}/icons/sugar
%{_datadir}/themes/sugar-100/gtk-2.0/gtkrc
%{_datadir}/themes/sugar-72/gtk-2.0/gtkrc
%{_libdir}/gtk-2.0/*/engines/*.so

#gtk3
%{_datadir}/themes/sugar-100/gtk-3.0/gtk.css
%{_datadir}/themes/sugar-100/gtk-3.0/gtk-widgets.css
%{_datadir}/themes/sugar-100/gtk-3.0/settings.ini
%{_datadir}/themes/sugar-100/gtk-3.0/assets/*
%{_datadir}/themes/sugar-100/gtk-3.20/gtk.css
%{_datadir}/themes/sugar-100/gtk-3.20/gtk-widgets.css
%{_datadir}/themes/sugar-100/gtk-3.20/assets/*
%{_datadir}/themes/sugar-72/gtk-3.0/gtk.css
%{_datadir}/themes/sugar-72/gtk-3.0/gtk-widgets.css
%{_datadir}/themes/sugar-72/gtk-3.0/settings.ini
%{_datadir}/themes/sugar-72/gtk-3.0/assets/*
%{_datadir}/themes/sugar-72/gtk-3.20/gtk.css
%{_datadir}/themes/sugar-72/gtk-3.20/gtk-widgets.css
%{_datadir}/themes/sugar-72/gtk-3.20/assets/*

%changelog
* Wed Dec 28 2016 Ignacio Rodríguez <ignacio@fedoraproject.org> 0.110.0-1
- Sugar 0.110.0 stable release

* Sun Mar  6 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.108.1-1
- Sugar 0.108.1 stable release

* Fri Feb 19 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.108.0-2
- Add patch for gtk3.20 theme changes

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

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.101.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.4-1
- 0.101.4 devel release

* Sun Mar  9 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.3-1
- 0.101.3 devel release

* Sat Feb 15 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.2-1
- 0.101.2 devel release

* Sun Dec  8 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.0-1
- 0.101.0 devel release

* Fri Nov  1 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.100.0-1
- Sugar 0.100.0 stable release

* Tue Oct 8  2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.2-1
- 0.99.2 devel release
- Changes license to Apache 2.0

* Wed Jul 31 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.1-1
- 0.99.1 devel release

* Fri Jun 28 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.0-1
- 0.99.0 devel release
- Trim changelog

* Fri May 24 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.85.5-1
- Sugar 0.98.5 stable release

* Sat Feb 16 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.4-1
- Sugar 0.98.4 stable release

* Thu Jan 24 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.3-1
- Sugar 0.98.3 stable release

* Tue Dec 18 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.2-1
- Sugar 0.98.2 stable release

* Mon Dec 10 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.1-1
- Sugar 0.98.1 stable release

* Thu Nov 29 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.0-1
- Sugar 0.98.0 stable release

* Tue Nov 27 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.12-1
- 0.97.12 devel release

* Sat Nov 24 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.11-1
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

* Fri Oct  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.5-1
- 0.97.5 devel release

* Wed Sep 26 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.4-1
- 0.97.4 devel release

* Thu Sep 20 2012 Daniel Drake <dsd@laptop.org> - 0.97.3-1
- Ne development release

* Thu Sep 13 2012 Daniel Drake <dsd@laptop.org> - 0.97.2-1
- New development release

* Tue Aug 28 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.1-1
- 0.97.2 devel release

* Wed Aug 15 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.0-1
- 0.97.0 devel release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.4-1
- 0.96.4 stable release

* Sat Jun  2 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.3-1
- 0.96.3 stable release

* Sat May  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.2-1
- 0.96.2 stable release

* Mon Apr 30 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.1-1
- 0.96.1 stable release

* Tue Apr 24 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.0-1
- 0.96.0 stable release

* Thu Apr 19 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.5-1
- devel release 0.95.5

* Fri Mar 23 2012 Simon Schampijer <simon@laptop.org> - 0.95.4-1
- devel release 0.95.4

* Wed Mar 14 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.3-1
- devel release 0.95.3

* Mon Feb  6 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.2-3
- Update 0.95.2 tarball

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 22 2011 Simon Schampijer <simon@laptop.org> - 0.95.2-1
- include the gtk3 theme

* Tue Oct 25 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.1-1
- devel release 0.95.1

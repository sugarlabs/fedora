%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Summary: Constructionist learning platform
Name:    sugar
Version: 0.110.0
Release: 1%{?dist}
URL:     http://sugarlabs.org/
License: GPLv2+
Group:   User Interface/Desktops
Source0: http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.xz
Patch0:  sugar-gnomekeyring.patch

BuildRequires: dconf-devel
BuildRequires: gettext
BuildRequires: GConf2-devel
BuildRequires: gobject-introspection
BuildRequires: gtk3-devel
BuildRequires: gtksourceview3-devel
BuildRequires: intltool
BuildRequires: perl-XML-Parser
BuildRequires: pkgconfig
BuildRequires: python

Requires: avahi-tools
Requires: dbus-x11
Requires: dconf
Requires: ethtool
Requires: gnome-keyring-pam
Requires: gstreamer-plugins-espeak
Requires: gtksourceview3
Requires: gvfs
Requires: gwebsockets
Requires: libwnck3
Requires: libxklavier
Requires: metacity
Requires: NetworkManager
Requires: openssh
Requires: polkit
Requires: python-telepathy
Requires: sugar-artwork
Requires: sugar-cp-all
Requires: sugar-toolkit-gtk3
Requires: telepathy-mission-control
Requires: telepathy-gabble
Requires: telepathy-salut
Requires: upower
Requires: xdg-user-dirs

BuildArch: noarch

%description
Sugar provides simple yet powerful means of engaging young children in the 
world of learning that is opened up by computers and the Internet. With Sugar,
even the youngest learner will quickly become proficient in using the 
computer as a tool to engage in authentic problem-solving.  Sugar promotes 
sharing, collaborative learning, and reflection, developing skills that help 
them in all aspects of life. 

Sugar is also the learning environment for the One Laptop Per Child project. 
See http://www.laptop.org for more information on this project.

%package cp-all
Summary: All control panel modules 
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Requires: %{name}-cp-background %{name}-cp-backup %{name}-cp-datetime 
Requires: %{name}-cp-frame %{name}-cp-language %{name}-cp-modemconfiguration
Requires: %{name}-cp-network %{name}-cp-keyboard %{name}-cp-webaccount 
Requires: %{name}-cp-updater

%description cp-all
This is a meta package to install all Sugar Control Panel modules

%package cp-background
Summary: Sugar Background control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-background
This is the Sugar control panel to change the background

%package cp-backup
Summary: Sugar Backup control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-backup
This is the Sugar control panel to backup and restore the Journal

%package cp-datetime
Summary: Sugar Date and Time control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-datetime
This is the Sugar Date and Time settings control panel

%package cp-frame
Summary: Sugar Frame control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-frame
This is the Sugar Frame settings control panel

%package cp-keyboard
Summary: Sugar Keyboard control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-keyboard
This is the Sugar Keyboard settings control panel

%package cp-language
Summary: Sugar Language control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-language
This is the Sugar Language settings control panel

%package cp-modemconfiguration
Summary: Sugar Modem configuration control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Requires: mobile-broadband-provider-info

%description cp-modemconfiguration
This is the Sugar Modem configuration control panel

%package cp-network
Summary: Sugar Network control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-network
This is the Sugar Network settings control panel

%package cp-power
Summary: Sugar Power control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-power
This is the Sugar Power settings control panel

%package cp-updater
Summary: Sugar Activity Update control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-updater
This is the Sugar Activity Updates control panel

%package cp-webaccount
Summary: Sugar Web Account control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-webaccount
This is the Sugar Web Account control panel


%prep
%setup -q
%patch0 -p1 -b .keyring

%build
%configure
make

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=%{buildroot}
mkdir %{buildroot}/%{_datadir}/sugar/activities
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

%find_lang %{name}

%post
/bin/touch --no-create %{_datadir}/mime/packages &> /dev/null || :
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
	%{_sysconfdir}/gconf/schemas/sugar.schemas > /dev/null || :

%pre
if [ "$1" -gt 1 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/sugar.schemas > /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/sugar.schemas > /dev/null || :
fi

%postun
if [ $1 -eq 0 ] ; then
  /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
  /usr/bin/update-mime-database %{_datadir}/mime &> /dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
/usr/bin/update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :

%files -f %{name}.lang
%license COPYING
%config %{_sysconfdir}/dbus-1/system.d/nm-user-settings.conf
%config %{_sysconfdir}/gconf/schemas/sugar.schemas
%{_bindir}/sugar*
%{_datadir}/GConf/gsettings/sugar-schemas.convert
%{_datadir}/glib-2.0/schemas/org.sugarlabs.gschema.xml
%{_datadir}/mime/packages/sugar.xml
%{_datadir}/xsessions/sugar.desktop

%{python_sitelib}/*

%dir %{_datadir}/sugar
%dir %{_datadir}/sugar/activities
%dir %{_datadir}/sugar/extensions
%dir %{_datadir}/sugar/extensions/cpsection

%{_datadir}/sugar/data
%{_datadir}/sugar/extensions/deviceicon
%{_datadir}/sugar/extensions/globalkey
%{_datadir}/sugar/extensions/webservice
%{_datadir}/sugar/extensions/cpsection/*.py*
%{_datadir}/sugar/extensions/cpsection/aboutcomputer
%{_datadir}/sugar/extensions/cpsection/aboutme
%exclude %{_datadir}/sugar/extensions/cpsection/[b-z]*
%{_datadir}/polkit-1/actions/org.sugar.*.policy

%files cp-all

%files cp-background
%{_datadir}/sugar/extensions/cpsection/background

%files cp-backup
%{_datadir}/sugar/extensions/cpsection/backup

%files cp-datetime
%{_datadir}/sugar/extensions/cpsection/datetime

%files cp-frame
%{_datadir}/sugar/extensions/cpsection/frame

%files cp-keyboard
%{_datadir}/sugar/extensions/cpsection/keyboard

%files cp-language
%{_datadir}/sugar/extensions/cpsection/language

%files cp-modemconfiguration
%{_datadir}/sugar/extensions/cpsection/modemconfiguration

%files cp-network
%{_datadir}/sugar/extensions/cpsection/network

%files cp-power
%{_datadir}/sugar/extensions/cpsection/power

%files cp-updater
%{_datadir}/sugar/extensions/cpsection/updater

%files cp-webaccount
%{_datadir}/sugar/extensions/cpsection/webaccount

%changelog
* Wed Dec 28 2016 Ignacio Rodríguez <ignacio@fedoraproject.org> 0.110.0-1
- Sugar 0.110.0 stable release

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

* Mon Mar  9 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.104.0-2
- Explicitly require telepathy-gabble and telepathy-salut

* Sat Feb 14 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.104.0-1
- Sugar 0.104.0 stable release

* Sat Jan 17 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.103.2-1
- New upstream 0.103.2 development release

* Thu Dec 11 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.103.1-1
- New upstream 0.103.1 development release

* Thu Nov 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.103.0-1
- New upstream 0.103.0 development release

* Sat Sep 27 2014 Rex Dieter <rdieter@fedoraproject.org> 0.102.0-4
- update/optimize mime scriptlet

* Thu Sep 25 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.102.0-3
- Add mobile provider dep to the modem control panel

* Tue Aug 12 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.102.0-2
- Add new backup control panel
- Add dependency on dconf

* Wed Jul  2 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.102.0-1
- Sugar 0.102.0 stable release

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.101.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.7-1
- 0.101.7 devel release

* Sun Apr 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.6-1
- 0.101.6 devel release

* Thu Mar 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.5-1
- 0.101.5 devel release

* Sun Mar  9 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.4-1
- 0.101.4 devel release

* Sat Feb 15 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.3-1
- 0.101.3 devel release

* Tue Feb  4 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.1-2
- Compile GSettings schemas

* Mon Jan 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.1-1
- 0.101.1 devel release

* Sun Dec  8 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.0-1
- 0.101.0 devel release

* Fri Nov 22 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.100.2-1
- Sugar 0.100.2 stable release

* Fri Nov  1 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.100.1-1
- Sugar 0.100.1 stable release

* Tue Oct 8  2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.4-1
- 0.99.4 devel release

* Sat Aug 10 2013 Daniel Drake <dsd@laptop.org> 0.99.1-3
- Add dependency on libxklavier, used via gobject-introspection

* Mon Aug  5 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.1-2
- Add dependency on gwebsockets for webservices

* Wed Jul 31 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.1-1
- 0.99.1 devel release

* Thu Jul 11 2013 Daniel Drake <dsd@laptop.org> 0.99.0-2
- Remove dependencies not required by Sugar shell

* Fri Jun 28 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.0-1
- 0.99.0 devel release
- Trim changelog

* Sun May 26 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.8-2
- Update default control panels

* Fri May 24 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.8-1
- Sugar 0.98.8 stable release

* Fri Apr 12 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.7-1
- Sugar 0.98.7 stable release

* Fri Mar 22 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.6-1
- Sugar 0.98.6 stable release

* Fri Mar  8 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.5-1
- Sugar 0.98.5 stable release

* Sat Feb 16 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.4-1
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

* Sat Nov 10 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.11-1
- 0.97.11 devel release

* Wed Nov  7 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.10-1
- 0.97.10 devel release

* Thu Oct 25 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.9-1
- 0.97.9 devel release

* Tue Oct 16 2012 Daniel Drake <dsd@laptop.org> 0.97.8-1
- 0.97.8 devel release

* Thu Oct 11 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.7-1
- 0.97.7 devel release

* Fri Oct  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.6-1
- 0.97.6 devel release

* Thu Oct  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.5-2
- Split out Control Panels to sub packages
- Update gnome-keyring patch. RHBZ 862581
- Add patch to update build dependencies

* Thu Sep 27 2012 Daniel Drake <dsd@laptop.org> - 0.97.5-1
- New development release

* Thu Sep 20 2012 Daniel Drake <dsd@laptop.org> - 0.97.4-1
- New development release

* Thu Sep 13 2012 Daniel Drake <dsd@laptop.org> - 0.97.3-1
- New development release

* Tue Aug 28 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.2-1
- 0.97.2 devel release

* Tue Aug 21 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.1-1
- 0.97.1 devel release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.3-1
- 0.96.3 stable release

* Tue Jun  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.2-1
- 0.96.2 stable release

* Sat May  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.1-2
- Add patch to create gnome keyring if it doesn't exist

* Mon Apr 30 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.1-1
- 0.96.1 stable release

* Tue Apr 24 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.0-1
- 0.96.0 stable release

* Thu Apr 19 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.7-1
- devel release 0.95.7

* Mon Mar 26 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.6-1
- devel release 0.95.6

* Wed Mar 14 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.5-1
- devel release 0.95.5

* Tue Mar  6 2012 Daniel Drake <dsd@laptop.org> - 0.95.4-2
- Add dependency on sugar-toolkit-gtk3 (needed to launch activities)

* Thu Feb  2 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.4-1
- devel release 0.95.4

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jan  2 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.3-3
- Drop premature sugar-base obsoletion

* Thu Dec 22 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.3-2
- Obsolete sugar-base

* Wed Dec 21 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.3-1
- devel release 0.95.3

* Wed Nov 16 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.2-1
- devel release 0.95.2

* Tue Oct 25 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.1-1
- devel release 0.95.1

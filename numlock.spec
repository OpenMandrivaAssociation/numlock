# !!!!!!!! WARNING THIS HAS TO BE EDITED IN THE SVN !!!!!!!!!!!

Summary:	Numlock key locker
Name:		numlock
Version:	2.1.2
Release:	14
License:	GPL
Url:		http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/numlock/
Group:		System/Configuration/Boot and Init
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xtst)
# do not require X11 libs
AutoReq:	no
Requires(post):	rpm-helper
Requires(preun): rpm-helper
Provides:	NumLock = %{version}-%{release}

%description
NumLock enable to lock the numlock key. Only enable it at boot-time with
ntsysv or with any other SVSR like rc.d config scripts editor such as
tksysv or the ones from GNOME and KDE.
NumLock is safe for laptops since it is disabled by default.

%prep
%setup -q

%build
make CFLAGS="%{optflags}"

%install
make install TOP=%{buildroot} INITRDDIR=%{_initrddir}

%find_lang %{name} --with-man --all-name

%post
%_post_service numlock

%preun
%_preun_service numlock

%triggerpostun -- numlock < 2.1.2-2mdv
if [ -L "/etc/rc.d/rc5.d/*numlock" ]; then
 /sbin/chkconfig --level 7 numlock reset
fi

%files -f %{name}.lang
%config(noreplace) %{_initrddir}/%{name}
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.sh
%config(noreplace) %{_sysconfdir}/X11/xinit.d/numlock
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.1.2-6mdv2011.0
+ Revision: 666634
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.2-5mdv2011.0
+ Revision: 606834
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.2-4mdv2010.1
+ Revision: 523449
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.1.2-3mdv2010.0
+ Revision: 426260
- rebuild

* Thu Apr 16 2009 Frederic Crozat <fcrozat@mandriva.com> 2.1.2-2mdv2009.1
+ Revision: 367605
- Fix numlock enabling on upgrade (Mdv bug #49987)

* Wed Apr 08 2009 Frederic Crozat <fcrozat@mandriva.com> 2.1.2-1mdv2009.1
+ Revision: 365204
- Release 2.1.2 :
 - enable numlock in speedboot mode (Mdv bug 49572)

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2.1.1-3mdv2009.1
+ Revision: 351638
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.1.1-2mdv2009.0
+ Revision: 223354
- rebuild

* Thu Apr 03 2008 Olivier Blin <oblin@mandriva.com> 2.1.1-1mdv2008.1
+ Revision: 192055
- fix syntax error in xinit script

* Thu Apr 03 2008 Olivier Blin <oblin@mandriva.com> 2.1-1mdv2008.1
+ Revision: 192023
- 2.1
- do not change numlock status on remote displays
  (from Frank Griffin, #15299)
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 01 2007 Olivier Blin <oblin@mandriva.com> 2.0-18mdv2008.0
+ Revision: 57669
- remove fileutils/console-tools/glibc requires, they are required by basesystem
- Import numlock




* Tue Aug 22 2006 Pixel <pixel@mandriva.com> 2.0-17mdv2007.0
- add BuildRequires libxtst-devel

* Tue Aug 22 2006 Pixel <pixel@mandriva.com> 2.0-16mdv2007.0
- move out of /usr/X11R6
- moved to SVN

* Wed Mar  8 2006 Olivier Blin <oblin@mandriva.com> 2.0-15mdk
- disable autoReq back (not to require X11 libs)

* Mon Jan  9 2006 Olivier Blin <oblin@mandriva.com> 2.0-14mdk
- convert parallel init to LSB
- mkrel
- add missing Requires(preun)

* Mon Jan  2 2006 Olivier Blin <oblin@mandriva.com> 2.0-13mdk
- add url
- use Requires(post) instead of PreReq
- enable rpm autoReq back

* Mon Jan  2 2006 Olivier Blin <oblin@mandriva.com> 2.0-12mdk
- parallel init support

* Mon Feb 28 2005 Olivier Blin <oblin@mandrakesoft.com> 2.0-11mdk
- start numlock before dm service (#6738)

* Fri Dec  3 2004 Olivier Blin <blino@mandrake.org> 2.0-10mdk
- fix description (Rafael)

* Fri Dec  3 2004 Olivier Blin <blino@mandrake.org> 2.0-9mdk
- add nl man page
- test the real lock file /var/lock/subsys/numlock
  (from David MacKenzie, #12558)

* Sat Apr 19 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 2.0-8mdk
- make it lib64 aware

* Thu Feb 13 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 2.0-7mdk
- rebuild

* Tue Oct 16 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 2.0-6mdk
- fix obsolete-tag Copyright
- resync in cvs

* Thu Aug 30 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 2.0-5mdk
- fix provides

* Sat Jul 07 2001 Stefan van der Eijk <stefan@eijk.nu> 2.0-4mdk
- BuildRequires:	XFree86-devel

* Thu Jul  5 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 2.0-3mdk
- rebuild

* Thu Mar 29 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 2.0-2mdk
- user post and preun service macros

* Tue Jan  9 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 2.0-1mdk
- really fix the xinit.d file
- reintegrate into CVS

* Thu Nov  2 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0-11mdk
- fix the xinit.d file, thanks to fcrozat
- get latest code that ensure the numlock is on even if it was already
  on, thx to fcrozat

* Mon Sep 11 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0-10mdk
- tried to really fix numlock for fredl

* Wed Aug 30 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0-9mdk
- added %%{_initrddir}
- NumLock -> numlock by request of submarine ;-)
- %%config(noreplace)

* Wed Apr 26 2000 Pixel <pixel@mandrakesoft.com> 1.0-8mdk
- force non-requiring XFree86-libs

* Wed Apr 12 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.0-7mdk
- launch via /etc/X11/xinit.d

* Wed Apr  5 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0-6mdk
- Remove the noarch since now we have enable_X11_numlock.
- Cvs import.
- Add enable_X11_numlock program (thanks gégé).

* Fri Mar 31 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0-5mdk
- new groups

* Wed Dec 22 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- fix a bug in xterm handling (reject /dev/ttya??)

* Thu Nov 18 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- fix chkconfig
- explicitely requires console-tools for touch (this would be the first
  rpm to do this !) and fileutils for setleds (which may have cause problems)

* Fri Oct 28 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- fix a typo (rpm include the %%setup in the %%description section !!!)
- lowercase the rpm name for Lord DarkChmou

* Fri Oct 24 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- initial spec

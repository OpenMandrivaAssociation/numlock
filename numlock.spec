# !!!!!!!! WARNING THIS HAS TO BE EDITED IN THE SVN !!!!!!!!!!!

%define name numlock
%define version 2.1.2
%define release %mkrel 6

Summary: Numlock key locker
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Url: http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/numlock/
Group: System/Configuration/Boot and Init
Source0: %{name}-%{version}.tar.bz2
BuildRequires: libx11-devel
BuildRequires: libxtst-devel
BuildRoot: %{_tmppath}/%{name}-buildroot
# do not require X11 libs
autoReq: no
Requires(post): rpm-helper
Requires(preun): rpm-helper
Obsoletes: NumLock
Provides: NumLock = %{version}-%{release}

%description
NumLock enable to lock the numlock key. Only enable it at boot-time with
ntsysv or with any other SVSR like rc.d config scripts editor such as
tksysv or the ones from GNOME and KDE.
NumLock is safe for laptops since it is disabled by default.

%prep
%setup -q

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install TOP=$RPM_BUILD_ROOT INITRDDIR=%{_initrddir}

%post
%_post_service numlock

%preun
%_preun_service numlock

%triggerpostun -- numlock < 2.1.2-2mdv
if [ -L "/etc/rc.d/rc5.d/*numlock" ]; then
 /sbin/chkconfig --level 7 numlock reset
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755,root,root)
%config(noreplace) %{_initrddir}/%{name}
%config(noreplace) /etc/profile.d/%{name}.sh
%config(noreplace) /etc/X11/xinit.d/numlock
/usr/bin/*
%{_mandir}/man1/*
%lang(cs) %{_mandir}/cs/man1/*
%lang(et) %{_mandir}/et/man1/*
%lang(eu) %{_mandir}/eu/man1/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(nl) %{_mandir}/nl/man1/*
%lang(ru) %{_mandir}/ru/man1/*
%lang(uk) %{_mandir}/uk/man1/*

Summary:	Numlock key locker
Name:		numlock
Version:	2.1.2
Release:	11
License:	GPLv2
Group:		System/Configuration/Boot and Init
Url:		http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/numlock/
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xtst)
# do not require X11 libs
AutoReq:	no
Requires(post,preun):	rpm-helper
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


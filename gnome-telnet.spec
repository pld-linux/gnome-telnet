Summary:	GNOME Telnet is a 3-in-1 GNOME shell for Telnet, SSH, and RLogin
Summary(pl):	GNOME Telnet jest nak³adk± dla GNOME do programów Telnet, SSH oraz RLogin
Name:		gnome-telnet
Version:	2.4
Release:	1
URL:		http://www.cyest.org/
Source0:	http://www.cyest.org/downloads/%{name}-%{version}.tar.gz
License:	GPL
Group:		X11/Applications/Networking
Group(de):	X11/Applikationen/Netzwerkwesen
Group(pl):	X11/Aplikacje/Sieciowe
BuildRequires:	gnome-libs-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
Prereq:		telnet
Prereq:		openssh
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandif		%{_prefix}/man

%description
Gnome Telnet is a powerful frontend telnet client for GNOME. It not
only has support for telnet, but for ssh and rlogin as well.

%description
Gnome Telnet jest potê¿n± nak³adk± na programy telnet, ssh oraz rlogin
dla ¶rodowiska GNOME.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=$RPM_BUILD_ROOT%{_prefix}

install -d $RPM_BUILD_ROOT%{_applnkdir}/Network
install -d $RPM_BUILD_ROOT%{_pixmapsdir}/gtelnet
install -d $RPM_BUILD_ROOT%{_datadir}/icons

install share/GTelnet.desktop $RPM_BUILD_ROOT%{_applnkdir}/Network
install share/*.png $RPM_BUILD_ROOT%{_pixmapsdir}
install share/*.jpg $RPM_BUILD_ROOT%{_pixmapsdir}/gtelnet
install share/*.xpm $RPM_BUILD_ROOT%{_datadir}/icons

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc docs *.gz
%attr(755,root,root) %{_bindir}/gnome-telnet
%{_applnkdir}/Network/*.desktop
%{_pixmapsdir}/*.png
%{_pixmapsdir}/gtelnet
%{_datadir}/icons/*

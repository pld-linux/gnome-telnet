Summary:	GNOME Telnet is a 3-in-1 GNOME shell for Telnet, SSH, and RLogin
Summary(pl):	GNOME Telnet jest nak³adk± dla GNOME do programów Telnet, SSH oraz RLogin
Name:		gnome-telnet
Version:	2.4
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.cyest.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	bb5580a076b22b47097b60e2ec361325
Source1:	%{name}.desktop
Patch0:		%{name}-pl_translation.patch
URL:		http://www.cyest.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
Requires:	openssh-clients
Requires:	telnet
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_mandif		%{_prefix}/man

%description
Gnome Telnet is a powerful frontend telnet client for GNOME. It not
only has support for telnet, but for ssh and rlogin as well.

%description -l pl
Gnome Telnet jest potê¿n± nak³adk± na programy telnet, ssh oraz rlogin
dla ¶rodowiska GNOME.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=$RPM_BUILD_ROOT%{_prefix}

install -d $RPM_BUILD_ROOT%{_applnkdir}/Network
install -d $RPM_BUILD_ROOT%{_pixmapsdir}/gtelnet

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network
install share/*.png $RPM_BUILD_ROOT%{_pixmapsdir}
install share/*.jpg $RPM_BUILD_ROOT%{_pixmapsdir}/gtelnet
install share/*.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc docs AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gnome-telnet
%{_applnkdir}/Network/*.desktop
%{_pixmapsdir}/*.png
%{_pixmapsdir}/*.xpm
%{_pixmapsdir}/gtelnet

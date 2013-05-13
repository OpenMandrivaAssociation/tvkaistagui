Name:		tvkaistagui
Version:	1.3.0
Release:	2
License:	GPLv3
Group:		Video
Summary:	Fast and easy GUI for Finnish TVkaista service
URL:		http://helineva.net/%{name}
Source0:        http://helineva.net/%{name}/%{name}-%{version}-src.tar.gz
BuildRequires: 	pkgconfig(libpng)
BuildRequires:	pkgconfig(Qt3Support) >= 4.6.0
Requires:	vlc

%description
Download and play TV programs from Finnish TVkaista service.

%prep
%setup -q

%build
%qmake_qt4 CONFIG+=release src/tvkaista.pro
%make 

%install
rm -rf %{buildroot}
install -D -s -m 755 %{name} %{buildroot}/%{_bindir}/%{name}
install -D -m 644 src/images/tvkaista-48x48.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -D -m 644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop


%changelog
* Fri Jun 24 2011 Jani Välimaa <wally@mandriva.org> 1.3.0-1mdv2011.0
+ Revision: 686928
- new version 1.3.0
- require vlc

* Wed Apr 20 2011 Jani Välimaa <wally@mandriva.org> 1.2.1-1
+ Revision: 656294
- import tvkaistagui


%define debug_package %{nil}

Name:		tvkaistagui
Version:	1.3.0
Release:	3
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
install -D -s -m 755 %{name} %{buildroot}/%{_bindir}/%{name}
install -D -m 644 src/images/tvkaista-48x48.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -D -m 644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

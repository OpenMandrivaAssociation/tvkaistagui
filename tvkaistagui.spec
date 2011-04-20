Name:		tvkaistagui
Version:	1.2.1
Release:	%mkrel 1
License:	GPLv3
Group:		Video
Summary:	Fast and easy GUI for Finnish TVkaista service
URL:		http://helineva.net/%{name}
Source0:        http://helineva.net/%{name}/%{name}-%{version}-src.tar.gz
BuildRequires: 	libpng-devel
BuildRequires:	libqt4-devel >= 4.6.0
Suggests:	vlc

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

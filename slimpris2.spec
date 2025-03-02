Name:                   slimpris2
Version:                3.0.0
Release:                0.1%{?dist}
Summary:                MPRIS remote control of Logitech Media Server

License:                GPLv3
URL:                    https://github.com/mavit/slimpris2/
Source0:                https://github.com/mavit/slimpris2/archive/master.tar.gz#slimpris2-master.tar.gz

BuildArch:              noarch
BuildRequires:          autoconf
BuildRequires:          automake
BuildRequires:          intltool
BuildRequires:          make
BuildRequires:          pandoc
BuildRequires:          python3-devel
BuildRequires:          systemd
BuildRequires:          systemd-rpm-macros

Requires:               python3dist(dbus-python)
Requires:               python3dist(pygobject)
Requires:               python3dist(pyxdg)
Requires:               python3dist(simplejson)
Requires:               python3dist(six)

%description
slimpris2 provide MPRIS 2 remote control support for Logitech Media
Server, allowing it to be controlled using the user interface integrated
into your desktop.


%prep
%autosetup


%build
./autogen.sh
%configure
%make_build


%install
%make_install
rm %{buildroot}/%{_docdir}/%{name}/COPYING
install -m 0644 -p -D %{buildroot}/%{_docdir}/%{name}/%{name}.conf \
                      %{buildroot}/%{_sysconfdir}/%{name}.conf


%files
%config(noreplace) %{_sysconfdir}/%{name}.conf
%doc %{_mandir}/*/*
%doc AUTHORS
%doc README.md
%doc src/%{name}.conf
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/io.github.mavit.slimpris2.desktop
%{_datadir}/dbus-1/services/org.mpris.MediaPlayer2.slimpris2.service
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_userpresetdir}/80-%{name}.preset
%{_userunitdir}/%{name}.service


%changelog

%define libname %mklibname playerctl
%define devname %mklibname -d playerctl

Name:           playerctl
Version:        2.4.1
Release:        1
Summary:        Command-line MPRIS-compatible Media Player Controller
License:        LGPL-3.0-or-later
URL:            https://github.com/acrisci/playerctl
Source0:        https://github.com/acrisci/playerctl/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

Requires: python-gobject3
Requires: python-gi

Requires: %{libname} = %{EVRD}


%description
Playerctl is a command-line utility and library for controlling media players
that implement the MPRIS D-Bus Interface Specification. Playerctl makes it easy
to bind player actions, such as play and pause, to media keys. You can also get
metadata about the playing track such as the artist and title for integration
into statusline generators or other command-line tools.

For more advanced users, Playerctl provides an introspectable library available
in your favorite scripting language that allows more detailed control like the
ability to subscribe to media player events or get metadata such as artist and
title for the playing track.

Examples of players implementing the MPRIS D-Bus Interface Specification include
vlc, mpv, RhythmBox, web browsers, cmus, mpd, spotify and others.


%package -n %{devname}
Summary:        Development libraries and header files for %{name}
Requires:       %{name} = %{EVRD}
Requires:       %{libname} = %{EVRD}

%description -n %{devname}
%{summary}.


%package -n docs
Summary:        Documentation related to %{name}
BuildArch:      noarch
Requires:       %{name} = %{EVRD}
BuildRequires:  gtk-doc

%description -n docs
%{summary}.


%package -n %{libname}
Summary:        Libraries and shared code for %{name}
Requires:       %{name} = %{EVRD}

%description -n %{libname}
%{summary}.

%prep
%autosetup -p1

%build
%meson -Dbash-completions=true -Dzsh-completions=true
%meson_build

%install
%meson_install

%files
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}d
%{_datadir}/bash-completion/
%{_datadir}/dbus-1/services/org.mpris.MediaPlayer2.playerctld.service
%{_datadir}/man/man1/%{name}.*
%{_datadir}/zsh/

%files -n %{devname}
%license COPYING
%{_datadir}/gir-1.0/Playerctl-2.0.gir
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n docs
%license COPYING
%{_datadir}/gtk-doc/

%files -n %{libname}
%license COPYING
%{_libdir}/girepository-1.0/
%{_libdir}/lib%{name}.so.2*

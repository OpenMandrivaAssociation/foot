Name:           foot
Version:        1.7.2
Release:        2
Summary:        Fast, lightweight and minimalistic Wayland terminal emulator

License:        MIT
URL:            https://codeberg.org/dnkl/foot
Source0:        https://codeberg.org/dnkl/foot/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson >= 0.53
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(fcft) >= 2.3.0
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(tllist) >= 1.0.4
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner) 
BuildRequires:  pkgconfig(xkbcommon)
# require *-static for header-only library
BuildRequires:  tllist-static

Recommends:     %{name}-terminfo = %{version}-%{release}
# Optional dependency for bell = notify option
Recommends:     /usr/bin/notify-send
# Optional dependency for opening URLs
Recommends:     /usr/bin/xdg-open
Requires:       hicolor-icon-theme

%description
Fast, lightweight and minimalistic Wayland terminal emulator.
Features:
 * Fast
 * Lightweight, in dependencies, on-disk and in-memory
 * Wayland native
 * DE agnostic
 * Server/daemon mode
 * User configurable font fallback
 * On-the-fly font resize
 * On-the-fly DPI font size adjustment
 * Scrollback search
 * Keyboard driven URL detection
 * Color emoji support
 * IME (via text-input-v3)
 * Multi-seat
 * Synchronized Updates support
 * Sixel image support

%package        terminfo
Summary:        Terminfo files for %{name} terminal
BuildRequires:  /usr/bin/tic
Requires:       ncurses

%description    terminfo
%{summary}.

%prep
%autosetup -n %{name}

%build
%meson
%meson_build


%install
%meson_install
# Will be installed to correct location with rpm macros
rm %{buildroot}%{_docdir}/%{name}/LICENSE


%files
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}client
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}-server.desktop
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/bash-completion/completions/foot*
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/foot*
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}
%{_datadir}/zsh/site-functions/_%{name}client
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/CHANGELOG.md
%{_docdir}/%{name}/README.md
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}client.1*
%{_mandir}/man5/%{name}.ini.5*
%{_mandir}/man7/%{name}-ctlseqs.7*

%files terminfo
%license LICENSE
%dir %{_datadir}/terminfo/f
%{_datadir}/terminfo/f/%{name}
%{_datadir}/terminfo/f/%{name}-direct

Name:		rosegarden
Version:	15.10
Release:	0.1
Summary:	Midi, audio and notation editor
License:	GPLv2+
Group:		Sound
URL:		http://www.rosegardenmusic.com/
Source0:		https://sourceforge.net/projects/rosegarden/files/rosegarden/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	kdelibs4-devel
BuildRequires:	jackit-devel
BuildRequires:	ladspa-devel
BuildRequires:	liblrdf-devel >= 0.2
BuildRequires:	imagemagick
BuildRequires:	chrpath
BuildRequires:	libxml2-utils
BuildRequires:	dssi-devel
BuildRequires:	makedepend
BuildRequires:	fftw3-devel >= 3
BuildRequires:	python
BuildRequires:	pkgconfig(liblo) >= 0.7
BuildRequires:	pkgconfig(xft)
BuildRequires:  pkgconfig(alsa) >= 0.9
BuildRequires:	pkgconfig(liblircclient0)
BuildRequires:	pkgconfig(sndfile) >= 1.0.16
BuildRequires:	pkgconfig(samplerate) >= 0.1.2
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(libcurl)
# TODO: libz, samplerate, perl, xargs, sha1sum and cut

Requires:	flac
Requires:	libsndfile-progs
Requires:	libsamplerate-progs
Requires:	xterm
Suggests:	lilypond >= 2.18.2
Obsoletes:	%{name}4 < %{version}

%description
Rosegarden is an attractive, user-friendly MIDI and audio sequencer,
notation editor, and general-purpose music composition and editing
application for Unix and Linux

%files -n %{name}
%_bindir/%{name}
%{_datadir}/%{name}
%_datadir/applications/%{name}.desktop
%_datadir/icons/*/*/*/*%{name}*
%_datadir/mime/*
%{_datadir}/appdata/rosegarden.appdata.xml

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}

%build
export QTDIR=/usr/lib/qt4
%configure2_5x
%make

%install
%makeinstall_std

# install some extra files
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pr \
        data/autoload \
        data/chords \
        data/examples \
        data/fonts \
        data/library \
        data/pixmaps \
        data/presets \
        data/profile \
        data/styles \
        data/templates \
        %{buildroot}%{_datadir}/%{name}


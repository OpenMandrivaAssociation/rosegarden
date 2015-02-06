Name:		rosegarden
Version:	14.12
Release:	2
Summary:	Midi, audio and notation editor
License:	GPLv2+
Group:		Sound
URL:		http://www.rosegardenmusic.com/
Source0:	http://sourceforge.net/projects/rosegarden/files/rosegarden/14.02/%{name}-%{version}.tar.bz2
BuildRequires:	kdelibs4-devel
BuildRequires:	jackit-devel >= 1.9.10
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
BuildRequires:	libalsa-devel >= 0.9
BuildRequires:	pkgconfig(liblircclient0)
BuildRequires:	sndfile-devel >= 1.0.16
BuildRequires:	pkgconfig(samplerate) >= 0.1.2
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(x11)
BuildRequires:	curl-devel
# TODO: libz, samplerate, perl, xargs, sha1sum and cut

Requires:	flac
Requires:	libsndfile-progs
# For sndfile-resample, see https://bugzilla.novell.com/show_bug.cgi?id=443543
# - AdamW 2008/12
Requires:	libsamplerate-progs
Requires:	xterm
Suggests:	lilypond
Obsoletes:	%{name}4 < %{version}

%description
Rosegarden is an attractive, user-friendly MIDI and audio sequencer,
notation editor, and general-purpose music composition and editing
application for Unix and Linux

%files -n %{name}
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/*/*/*/*%{name}*
%{_datadir}/mime/*
%{_datadir}/appdata/rosegarden.appdata.xml

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}

%build
#generate configure
#sh bootstrap.sh
export QTDIR=/usr/lib/qt4
%configure
%make

%install
rm -fr %{buildroot}
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

#find_lang %%{name} --with-html

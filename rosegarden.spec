%define rel 1

Name:           rosegarden
Version:        11.11.1
Release:        %mkrel %rel
Summary:        Midi, audio and notation editor
URL:            http://www.rosegardenmusic.com/
Source0:        http://sourceforge.net/projects/rosegarden/files/%{name}/%{version}/%{name}-%{version}.tar.bz2
Patch0:         %{name}-1.9-fix-include.patch
Patch1:         %{name}-1.9-fix-search-path.patch
License:        GPLv2+
Group:          Sound
BuildRequires:  kdelibs4-devel
BuildRequires:  jackit-devel
BuildRequires:  ladspa-devel
BuildRequires:  liblrdf-devel
BuildRequires:  imagemagick
BuildRequires:  chrpath
BuildRequires:  libxml2-utils
BuildRequires:  dssi-devel
BuildRequires:  makedepend
BuildRequires:  fftw3-devel
BuildRequires:  python
BuildRequires:  liblo-devel
BuildRequires:  libxft-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  liblirc-devel
Requires:       flac
Requires:       libsndfile-progs
# For sndfile-resample, see https://bugzilla.novell.com/show_bug.cgi?id=443543
# - AdamW 2008/12
Requires:       libsamplerate-progs
Requires:       xterm
Suggests:       lilypond
Obsoletes:      %{name}4
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
Rosegarden is an attractive, user-friendly MIDI and audio sequencer,
notation editor, and general-purpose music composition and editing
application for Unix and Linux

%files -n %name -f %{name}.lang
%defattr(-,root,root)
%_bindir/%{name}
%{_datadir}/%{name}
%_datadir/applications/%{name}.desktop
%_datadir/icons/*/*/*/*%{name}*
%_datadir/mime/*

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0
%patch1 -p0

%build
#generate configure
#sh bootstrap.sh
export QTDIR=/usr/lib/qt4
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std

# isntall some extra files
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

%find_lang %{name} --with-html

%clean
rm -rf %buildroot

#vim: set ft=rpm tabstop=4 shiftwidth=4 expandtab smarttab autoindent smartindent nu:

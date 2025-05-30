Name:		rosegarden
Version:	24.12.1
Release:	1
Summary:	Midi, audio and notation editor
License:	GPLv2+
Group:		Sound
URL:		https://www.rosegardenmusic.com/
Source0:	http://sourceforge.net/projects/rosegarden/files/rosegarden/%(echo %{version}|cut -d. -f1-2)/%{name}-%{version}.tar.xz
#Patch0:		rosegarden-20.06-qt-5.15.patch
Patch0:		rosegarden-22.06-clang15.patch
BuildRequires:	jackit-devel >= 1.9.10
BuildRequires:	cmake ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	ladspa-devel
BuildRequires:	liblrdf-devel >= 0.2
BuildRequires:	pkgconfig(raptor2)
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
Requires:	%{_lib}samplerate0
Requires:	xterm
Suggests:	lilypond
Obsoletes:	%{name}4 < %{version}

%description
Rosegarden is an attractive, user-friendly MIDI and audio sequencer,
notation editor, and general-purpose music composition and editing
application for Unix and Linux

%files
%{_bindir}/%{name}
%{_libdir}/librosegardenprivate.so
%{_datadir}/%{name}
%{_datadir}/applications/com.rosegardenmusic.rosegarden.desktop
%{_datadir}/icons/*/*/*/*%{name}*
%{_datadir}/mime/*
%{_datadir}/metainfo/rosegarden.appdata.xml

#--------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake_qt5 -G Ninja
%ninja

%install
%ninja_install -C build

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

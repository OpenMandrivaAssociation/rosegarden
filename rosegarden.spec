%bcond_without	qt6

Summary:	Midi, audio and notation editor
Name:	rosegarden
Version:	25.06
Release:	1
License:	GPLv2+
Group:	Sound
Url:		https://www.rosegardenmusic.com/
Source0:	http://sourceforge.net/projects/rosegarden/files/rosegarden/%(echo %{version}|cut -d. -f1-2)/%{name}-%{version}.tar.xz
Source100:	rosegarden.rpmlintrc
Patch0:	rosegarden-25.06-clang15.patch
BuildRequires:	cmake >= 3.16.0
BuildRequires:	desktop-file-utils
#BuildRequires:	imagemagick
BuildRequires:	libxml2-utils
#BuildRequires:	makedepend
BuildRequires:	ninja
BuildRequires:	python
BuildRequires:	shared-mime-info
BuildRequires:	subversion
BuildRequires:	ladspa-devel
BuildRequires:	cmake(ECM)
%if %{with qt6}
BuildRequires:	qt6-qttools-linguist
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Core5Compat)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Network)
BuildRequires:	pkgconfig(Qt6PrintSupport)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Xml)
%else
BuildRequires:	qt5-linguist-tools
BuildRequires:	cmake(Qt5Core) >= 5.1.0
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Xml)
%endif
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(dssi)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:pkgconfig(gtk+-2.0)
BuildRequires:pkgconfig(jack)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(liblircclient0)
BuildRequires:	pkgconfig(liblo) >= 0.7
BuildRequires:	pkgconfig(lilv-0)
BuildRequires:	pkgconfig(lrdf) >= 0.2
BuildRequires:	pkgconfig(lv2)
BuildRequires:	pkgconfig(raptor2)
BuildRequires:	pkgconfig(samplerate) >= 0.1.2
BuildRequires:	pkgconfig(shared-mime-info)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(sndfile) >= 1.0.16
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(zlib)
# TODO: samplerate, perl, xargs, sha1sum and cut
Requires:	flac
# For sndfile-resample, see https://bugzilla.novell.com/show_bug.cgi?id=443543
# - AdamW 2008/12
Requires:	%{_lib}samplerate0
Requires:	libsndfile-progs
Requires:	xterm
Suggests:	fluidsynth
Suggests:	lilypond
%if %{with qt6}
Suggests:	plasma6-okular
%else
Suggests:	okular
%endif
Suggests:	qjackctl
Suggests:	wavpack
%rename	%{name}4

%description
Rosegarden is an attractive, user-friendly MIDI and audio sequencer, notation
editor, and general-purpose music composition and editing application for Unix
and Linux.

%files
%doc AUTHORS CHANGELOG COPYING README.md
%{_bindir}/%{name}
%{_libdir}/librosegardenprivate.so
%{_datadir}/%{name}
%{_datadir}/applications/com.rosegardenmusic.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/mimetypes/application-x-%{name}-*.png
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/metainfo/%{name}.appdata.xml

#--------------------------------------------------------------------

%prep
%autosetup -p1


%build
%if %{with qt6}
%cmake -G Ninja -DUSE_QT6=ON
%else
%cmake_qt5 -G Ninja -DUSE_QT6=OFF
%endif

%ninja_build


%install
%ninja_install -C build

# Install some extra files
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pr \
        data/autoload \
        data/chords \
        data/examples \
        data/fonts \
        data/library \
        data/percussion \
		data/pitches \
        data/pixmaps \
        data/presets \
        data/profile \
        data/rc \
        data/styles \
        data/templates \
        %{buildroot}%{_datadir}/%{name}

# FIXME Install manually translation .qm files:
# they are in build/src but not bundled with the main executable
mkdir -p %{buildroot}%{_datadir}/%{name}/locale
cp build/src/*.qm %{buildroot}%{_datadir}/%{name}/locale

# Fix desktop file
desktop-file-edit	--remove-category="X-SuSE-Sequencer" --remove-category="X-Red-Hat-Base" \
								--set-key="X-KDE-NativeMimeType" --set-value="audio/x-rosegarden-composition;" \
								%{buildroot}%{_datadir}/applications/com.rosegardenmusic.%{name}.desktop

#find_lang %%{name} --with-html

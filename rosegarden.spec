%define	upstream_name		rosegarden
%define	upstream_version	10.02
%define	svn			11505
%define	rel			0.%upstream_version.%svn.1

Name:		rosegarden
Version:	1.9
Release:	%mkrel %rel
Summary: 	Midi, audio and notation editor
URL: 		http://www.rosegardenmusic.com/
Source0: 	%{upstream_name}-svn%{svn}.tar.bz2
Patch0:  	%{upstream_name}-1.9-fix-include.patch
Patch1:  	%{upstream_name}-1.9-fix-search-path.patch
License: 	GPLv2+
Group: 		Sound
BuildRequires:	kdelibs4-devel
BuildRequires:	jackit-devel
BuildRequires:	ladspa-devel
BuildRequires:	liblrdf-devel
BuildRequires:	imagemagick
BuildRequires:	chrpath
BuildRequires:	libxml2-utils
BuildRequires:	dssi-devel
BuildRequires:	makedepend
BuildRequires:	fftw3-devel
BuildRequires:	python
BuildRequires:	liblo-devel
BuildRequires:	libxft-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	liblirc-devel
Requires:	flac
Requires: libsndfile-progs
# For sndfile-resample, see https://bugzilla.novell.com/show_bug.cgi?id=443543
# - AdamW 2008/12
Requires:	libsamplerate-progs
Requires:	xterm
Suggests:	lilypond
Obsoletes:	%{name}4
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Rosegarden is an attractive, user-friendly MIDI and audio sequencer,
notation editor, and general-purpose music composition and editing
application for Unix and Linux

%files -n %name -f %{name}.lang
%defattr(-,root,root)
%_bindir/%{upstream_name}
%_datadir/applications/%{upstream_name}.desktop
%_datadir/icons/*/*/*/*%{upstream_name}*
%_datadir/mime/*

#--------------------------------------------------------------------

%prep
%setup -q -n %{upstream_name}
%patch0 -p0
%patch1 -p0

%build
#generate configure
sh bootstrap.sh
export QTLIBDIR=%{_libdir}
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std
%find_lang %{name} --with-html

%clean
rm -rf %buildroot

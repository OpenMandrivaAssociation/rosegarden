Name:		rosegarden
Version:		13.06
Release:		1
Summary:		Midi, audio and notation editor
License:		GPLv2+
Group:		Sound
URL:		http://www.rosegardenmusic.com/
Source0:		https://sourceforge.net/projects/rosegarden/files/rosegarden/13.06/%{name}-%{version}.tar.bz2
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
BuildRequires:	libalsa-devel >= 0.9
BuildRequires:	pkgconfig(liblircclient0)
BuildRequires:	sndfile-devel >= 1.0.16
BuildRequires:	pkgconfig(samplerate) >= 0.1.2
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(x11)
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
%_bindir/%{name}
%{_datadir}/%{name}
%_datadir/applications/%{name}.desktop
%_datadir/icons/*/*/*/*%{name}*
%_datadir/mime/*

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}

%build
#generate configure
#sh bootstrap.sh
export QTDIR=/usr/lib/qt4
%configure2_5x
%make

%install
rm -fr %buildroot
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


#vim: set ft=rpm tabstop=4 shiftwidth=4 expandtab smarttab autoindent smartindent nu:


%changelog
* Sat Oct 20 2012 Giovanni Mariani <mc2374#mclink.it> 12.04-1
- New release 12.04
- Dropped P0 (applied upstream)
- Dropped BuildRoot, %%mkrel, %%defattr and %%clean section
- Removed a now useless %%define for release number
- Adjusted BReq for alsa devel package
- Added some BReqs and version info according to the configure output
- Added %%version to Obsoletes clause and made rpmlint happy
- Fixed file list


* Wed Nov 09 2011 Alexander Khrukin <akhrukin@mandriva.org> 11.11.1-1mdv2012.0
+ Revision: 729308
- version update to upstream 11.11.1

* Thu Apr 21 2011 Frank Kober <emuse@mandriva.org> 11.02-1
+ Revision: 656455
- update to new version 11.02
- new version 11.02

* Wed Nov 24 2010 Funda Wang <fwang@mandriva.org> 10.10-1mdv2011.0
+ Revision: 600342
- new version 10.10

* Tue Jun 08 2010 Rémy Clouard <shikamaru@mandriva.org> 10.04.2-1mdv2010.1
+ Revision: 547294
- bump release

* Sat May 01 2010 Rémy Clouard <shikamaru@mandriva.org> 10.04-1mdv2010.1
+ Revision: 541483
- Update to new rosegarden-10.04 (bugfix release)
- fix build
- fix #57337: audio file import now works as expected
- hopefully fix 58329: notation editor crash
  CCBUG: 57337
  CCBUG: 58329
- use retab to remove stupid tabs

  + Ahmad Samir <ahmadsamir@mandriva.org>
    - don't install scripts dir

* Thu Mar 25 2010 Ahmad Samir <ahmadsamir@mandriva.org> 10.02.1-2mdv2010.1
+ Revision: 527532
- add more files, examples, presets (should fix bug#58269)

* Sat Feb 20 2010 Rémy Clouard <shikamaru@mandriva.org> 10.02.1-1mdv2010.1
+ Revision: 508702
- update to final release
- new versioning scheme from upstream

  + Sandro Cazzaniga <kharec@mandriva.org>
    - clean spec

* Sat Jan 23 2010 Rémy Clouard <shikamaru@mandriva.org> 1.9-0.10.02.11505.1mdv2010.1
+ Revision: 495292
- bump release (beta)
- fix #56490
- fix #57216

* Sun Oct 25 2009 Rémy Clouard <shikamaru@mandriva.org> 1.9-0.10.02.11081.1mdv2010.0
+ Revision: 459196
- fix #52901
- update to newer upstream revision
- drop merged patch

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix spec file name
    - Use the Qt4 version

* Tue Aug 18 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.9-0.10.02.10693.3mdv2010.0
+ Revision: 417526
- Fix more path
- Fix search pach

* Sun Aug 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.9-0.10.02.10693.1mdv2010.0
+ Revision: 416851
- Fix build on x86_64
- New snapshot

  + Rémy Clouard <shikamaru@mandriva.org>
    - fix obsoletes

* Tue Jun 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.9-0.09.10.10351.1mdv2010.0
+ Revision: 384349
- Use Qt4/Kde4 layout

  + Rémy Clouard <shikamaru@mandriva.org>
    - fix buildrequires
    - remove unneeded %%post and %%postun sections
    - import rosegarden4



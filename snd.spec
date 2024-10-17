Name: 		snd
Summary: 	Audio file editor
Version: 	11.4
Release: 	4
Source0:	ftp://ccrma-ftp.stanford.edu/pub/Lisp/%{name}-%{version}.tar.gz
URL:		https://www-ccrma.stanford.edu/software/snd/
License:	BSD-like
Group:		Sound
#patch0 was sent upstream by Kharec
Patch0:		snd-11.4-fix-str-fmt.patch
BuildRequires:	gsl-devel ladspa-devel xpm-devel guile-devel
BuildRequires:	pkgconfig(gamin)
BuildRequires:	fftw-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	mesaglu-devel
BuildRequires:	gtk2-devel
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(samplerate)

%description
Snd is a free sound editor modelled loosely after Emacs and an old,
sorely-missed PDP-10 sound editor named Dpysnd.

%prep
%setup -q
%patch0 -p0

%build
export LDFLAGS="-lX11 -ldl -lpthread"
%configure2_5x	--with-ladspa \
		--with-gsl \
		--with-gl \
		--with-alsa \
		--with-gtk \
		--with-jack \
		--with-guile \
		--with-midi
		
%make
make sndplay sndinfo
make audinfo
										
%install
# stupid hack, sorry, I'm lazy
cp mkinstalldirs ..
%{makeinstall}
cp sndplay sndinfo $RPM_BUILD_ROOT%{_bindir}

#menu

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Snd
Comment=%{summary}
Exec=%{_bindir}/%{name} %U
Icon=sound_section
Terminal=false
Type=Application
Categories=GTK;Audio;AudioVideoEditing;
EOF

%files
%defattr(-,root,root)
%doc README.Snd HISTORY.Snd tutorial NEWS COPYING
%{_bindir}/%{name}*
%{_datadir}/applications/*
%{_datadir}/%{name}/*
%{_mandir}/*/*


%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 11.4-2mdv2011.0
+ Revision: 614932
- the mass rebuild of 2010.1 packages

* Thu Apr 01 2010 Sandro Cazzaniga <kharec@mandriva.org> 11.4-1mdv2010.1
+ Revision: 530744
- update to 11.4
- add a patch for fix string format && add a comment for p0: patch was sent upstream.
- fix %%build and %%install: no "sndrecord" anymore...
- update file list for new version

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 9.10-2mdv2009.0
+ Revision: 269291
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jun 11 2008 Austin Acton <austin@mandriva.org> 9.10-1mdv2009.0
+ Revision: 218082
- new version

* Sat Feb 09 2008 Funda Wang <fwang@mandriva.org> 9.7-1mdv2008.1
+ Revision: 164429
- update to new version 9.7

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Dec 28 2007 Austin Acton <austin@mandriva.org> 9.6-1mdv2008.1
+ Revision: 138738
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - do not harcode icon extension

* Sat Aug 25 2007 Austin Acton <austin@mandriva.org> 9.3-1mdv2008.0
+ Revision: 71329
- new version

* Fri Jul 20 2007 Adam Williamson <awilliamson@mandriva.org> 9.2-1mdv2008.0
+ Revision: 53984
- fix menu entry: app is called Snd, not Totem, and has no icon of its own
- drop old menu file and X-Mandriva category
- new release 9.2

* Fri Jun 08 2007 Austin Acton <austin@mandriva.org> 9.1-1mdv2008.0
+ Revision: 37143
- new version

* Tue May 01 2007 Austin Acton <austin@mandriva.org> 9.0-1mdv2008.0
+ Revision: 20116
- 9.0


* Mon Feb 19 2007 Emmanuel Andry <eandry@mandriva.org> 8.8-1mdv2007.0
+ Revision: 122619
- fix buildrequires
- fix buildrequires
- New version 8.8
- add jack support

* Fri Jan 05 2007 Lenny Cartier <lenny@mandriva.com> 8.7-1mdv2007.1
+ Revision: 104482
- Update to 8.7
- Import snd

* Mon Aug 14 2006 Austin Acton <austin@mandriva.org> 8.3-1mdv2007.0
- 8.3
- xdg

* Tue Jun 27 2006 Austin Acton <austin@mandriva.org> 8.2-1mdk
- New release 8.2

* Wed May 10 2006 Lenny Cartier <lenny@mandriva.com> 8.1-1mdk
- 8.1

* Thu Mar 30 2006 Austin Acton <austin@mandriva.org> 8-1mdk
- 8
- source URL
- enable MIDI
- change audio from OSS to ALSA
- change GUI toolkit from motif to GTK (YAY!)

* Mon Jan 16 2006 Lenny Cartier <lenny@mandriva.com> 7.18-1mdk
- 7.18

* Wed Jan 11 2006 Austin Acton <austin@mandriva.org> 7.17-1mdk
- 7.17

* Tue Aug 30 2005 Austin Acton <austin@mandriva.org> 7.14-1mdk
- 7.14

* Wed Apr 27 2005 Austin Acton <austin@mandriva.org> 7.12-1mdk
- 7.12

* Tue Feb 22 2005 Lenny Cartier <lenny@mandrakesoft.com> 7.10-1mdk
- 7.10

* Wed Jan 05 2005 Austin Acton <austin@mandrake.org> 7.9-1mdk
- 7.9

* Wed Nov 10 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 7.8-1mdk
- 7.8

* Thu Jul 01 2004 Austin Acton <austin@mandrake.org> 7.5-1mdk
- 7.5
- configure 2.5
- disable sndsine for now, no time to fix

* Tue May 18 2004 Austin Acton <austin@mandrake.org> 7.4-1mdk
- 7.4


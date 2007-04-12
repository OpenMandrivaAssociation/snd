%define name	snd
%define version 8.8
%define release %mkrel 1

Name: 		%{name}
Summary: 	Audio file editor
Version: 	%{version}
Release: 	%{release}

Source0:	ftp://ccrma-ftp.stanford.edu/pub/Lisp/%{name}-%{version}.tar.bz2
URL:		http://www-ccrma.stanford.edu/software/snd/
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gsl-devel ladspa-devel xpm-devel guile-devel
BuildRequires:	libgamin-devel
BuildRequires:	fftw-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	MesaGLU-devel
BuildRequires:	gtk2-devel
BuildRequires:	libjack-devel
BuildRequires:	libsamplerate-devel

%description
Snd is a free sound editor modelled loosely after Emacs and an old,
sorely-missed PDP-10 sound editor named Dpysnd.

%prep
%setup -q -n %{name}-8

%build
%configure2_5x	--with-ladspa \
		--with-gsl \
		--with-gl \
		--with-alsa \
		--with-gtk \
		--with-jack \
		--with-guile \
		--with-midi
		
%make
make sndplay sndrecord sndinfo
# fixme: make audinfo
										
%install
rm -rf $RPM_BUILD_ROOT
# stupid hack, sorry, I'm lazy
cp mkinstalldirs ..
%{makeinstall}
cp sndplay sndrecord sndinfo $RPM_BUILD_ROOT%{_bindir}
# cp sndsine $RPM_BUILD_ROOT/%_bindir
%find_lang %{name}

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="sound_section.png" needs="x11" title="Snd" longtitle="Audio file editor" section="Multimedia/Sound" xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Totem
Comment=%{summary}
Exec=%{_bindir}/%{name} %U
Icon=%{name}
Terminal=false
Type=Application
Categories=GTK;Audio;AudioVideoEditing;X-MandrivaLinux-Multimedia-Sound;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%doc README.Snd TODO.Snd HISTORY.Snd tutorial
%{_bindir}/%{name}*
%{_datadir}/applications/*
%{_datadir}/%{name}/*
%{_menudir}/%{name}
%{_mandir}/*/*



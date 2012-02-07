%define name	snd
%define version 12.8
%define release 1

Name: 		%{name}
Summary: 	Audio file editor
Version: 	%{version}
Release: 	%{release}
Source0:	ftp://ccrma-ftp.stanford.edu/pub/Lisp/%{name}-%{version}.tar.gz
URL:		http://www-ccrma.stanford.edu/software/snd/
License:	BSD-like
Group:		Sound
Patch0:		snd-gfile-werror.patch
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
%setup -q
%patch0 -p1

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
make sndplay sndinfo
make audinfo
										
%install
# stupid hack, sorry, I'm lazy
cp mkinstalldirs ..
%{makeinstall}
cp sndplay sndinfo $RPM_BUILD_ROOT%{_bindir}
%find_lang %{name}

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

%files -f %{name}.lang
%doc README.Snd HISTORY.Snd tutorial NEWS COPYING
%{_bindir}/%{name}*
%{_datadir}/applications/*
%{_datadir}/%{name}/*
%{_mandir}/*/*

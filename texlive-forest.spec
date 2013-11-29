# revision 31930
# category Package
# catalog-ctan /graphics/pgf/contrib/forest
# catalog-date 2013-10-17 10:50:39 +0200
# catalog-license lppl1.3
# catalog-version 1.04
Name:		texlive-forest
Version:	1.04
Release:	1
Summary:	Drawing (linguistic) trees
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/forest
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/forest.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/forest.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/forest.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is provides a PGF/TikZ-based mechanism for drawing
linguistic (and other kinds of) trees. Its main features are: -
a packing algorithm which can produce very compact trees; - a
user-friendly interface consisting of the familiar bracket
encoding of trees plus the key-value interface to option-
setting; - many tree-formatting options, with control over
option values of individual nodes and mechanisms for their
manipulation; - the possibility to decorate the tree using the
full power of PGF/TikZ; and - an externalization mechanism
sensitive to code-changes.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/forest/forest.sty
%doc %{_texmfdistdir}/doc/latex/forest/README
%doc %{_texmfdistdir}/doc/latex/forest/forest.pdf
#- source
%doc %{_texmfdistdir}/source/latex/forest/forest.dtx
%doc %{_texmfdistdir}/source/latex/forest/forest.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

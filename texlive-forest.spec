%global tl_name forest
%global tl_revision 78931

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1.5
Release:	%{tl_revision}.1
Summary:	Drawing (linguistic) trees
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/forest
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/forest.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/forest.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/forest.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(elocalloc)
Requires:	texlive(environ)
Requires:	texlive(etoolbox)
Requires:	texlive(inlinedef)
Requires:	texlive(l3packages)
Requires:	texlive(pgf)
Requires:	texlive(pgfopts)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a PGF/TikZ-based mechanism for drawing linguistic
(and other kinds of) trees. Its main features are: a packing algorithm
which can produce very compact trees; a user-friendly interface
consisting of the familiar bracket encoding of trees plus the key-value
interface to option-setting; many tree-formatting options, with control
over option values of individual nodes and mechanisms for their
manipulation; the possibility to decorate the tree using the full power
of PGF/TikZ; and an externalization mechanism sensitive to code-changes.


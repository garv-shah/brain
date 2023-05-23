----------------------------------------------------------
Package:      unitipa
Version:      0.4  (20 October, 2021)
Author:       निरंजन
Description:  TIPA typefaces with Unicode characters.
Repository:   https://gitlab.com/niruvt/unitipa (archived)
License:      GPLv3, GFDLv1.3
----------------------------------------------------------
I have stopped maintaining this package and also taken it
back from the distributions as I have realized that it is
not ideal to use this package. The only purpose I had in
mind while writing this package was to get the visual shapes
of TIPA with Unicode characters in the input. This purpose
is served very well by the CMU-serif font. Please refer to
the file CMU-serif.tex and its output pdf to see the
characters that differ visually. They are just 4 which is a
very small number and the difference is not very much. I
have compared almost all the characters, but commented the
ones which show the exact same visual shape. You can
uncomment those lines from the source code to test it
yourself.

I apologize for providing a package that wasn't really
producing good results. A comment on StackExchange by an
expert user warned me about the use of Computer Modern
Unicode font, instead of using T3 encoding, but because of
my inexperience in LaTeX I assumed that this font is the
default font in every document (which isn't true). I tried
compiling a document with the default font i.e. Latin Modern
and I couldn't see the characters that I had listed in the
package documentation. Therefore I wrote this package. Now
that I have come to know about a more modern and recommended
way of getting the TIPA shapes in our documents, I am taking
this package back. The git repository of this project won't
accept issues and MRs henceforth, but the project
development and history will still be publicly available in
the archived state.

Best,
निरंजन
2021/10/20

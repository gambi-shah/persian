# Persian

Persian language support for LaTeX using Babel.

The `persian` package provides Persian language support for
pdfTeX, XeTeX, and LuaTeX.

## Features

- Persian language support through Babel
- Persian numerals and numbering
- Persian captions and translations
- Persian support for standard LaTeX documents
- Support for pdfTeX, XeTeX, and LuaTeX
- Support for Beamer

## Requirements

- LaTeX2e
- Babel
- XeTeX or LuaTeX for Unicode Persian typesetting

## Installation

Clone or download this repository and place the package files
in a directory where LaTeX can find them.

For example:

    git clone https://github.com/gambi-shah/persian.git

The package can then be loaded with:

    \usepackage{persian}

## Usage

A minimal example:

    \documentclass{article}
    \usepackage{persian}

    \begin{document}

    سلام دنیا!

    \end{document}

For XeLaTeX and LuaLaTeX, a Persian font can be selected according
to the font setup of the system.

## Supported Engines

| Engine | Support |
|--------|---------|
| pdfTeX | Basic |
| XeTeX  | Supported |
| LuaTeX | Supported |

The main development focus of the current release is LuaTeX,
followed by XeTeX. pdfTeX and Beamer support are currently
more limited and will be improved in future releases.

## License

This package is distributed under the
LaTeX Project Public License, version 1.3c or later (LPPL).

See the `LICENSE` file for the full license text.

## Maintainer

Amer Amikhteh

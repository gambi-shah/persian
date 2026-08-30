import argparse
import configparser
import os
import re


class CaseSensitiveConfigParser(configparser.ConfigParser):
    def optionxform(self, optionstr: str) -> str:
        return optionstr


def get_params(value: str) -> str:
    params = sorted(set(re.findall(r'#\d', value)))
    return ''.join(params)


def write_definitions(output, values):
    for key, value in values.items():
        params = get_params(value)
        output.write(
            f'    \\def\\{key}{params}{{{value}}}\n'
        )


def write_translations(output, values):
    for key, value in values.items():
        output.write(
            f'    \\deftranslation[to=Persian]{{{key}}}{{{value}}}%\n'
        )


def generate_def(output_path=None):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    ini_path = os.path.join(script_dir, 'persian-dictionary.ini')

    if output_path is None:
        output_path = os.path.join(
            project_root,
            'persian-captions.def'
        )

    if not os.path.exists(ini_path):
        print(f"Error: File not found at {ini_path}")
        return

    config = CaseSensitiveConfigParser(interpolation=None)
    config.read(ini_path, encoding='utf-8')

    with open(output_path, 'w', encoding='utf-8') as f:

        # Copyright and license
        f.write(
            '% Persian translations for LaTeX captions and package/class names.\n'
            '%\n'
            '% The translation data in this file were derived from XePersian, Babel,\n'
            '% and Polyglossia as distributed with TeX Live 2026.\n'
            '%\n'
            '% The original data were extracted and processed on Linux Mint using\n'
            '% dedicated Python scripts, and subsequently reviewed and refined. The\n'
            '% resulting work includes both technical and code-level modifications\n'
            '% as well as corrections and improvements to the Persian translations.\n'
            '%\n'
            '% This file is part of the Persian package.\n'
            '%\n'
            '% Copyright (C) 2026 Amer Amikhteh\n'
            '%\n'
            '% This work may be distributed and/or modified under the\n'
            '% conditions of the LaTeX Project Public License, either version 1.3c\n'
            '% of this license or (at your option) any later version.\n'
            '%\n'
            '% The latest version of this license is in\n'
            '% https://www.latex-project.org/lppl/\n'
            '% and version 1.3c or later is part of all distributions of LaTeX\n'
            '% version 2008 or later.\n'
            '%\n'
            '% This work is "maintained" by Amer Amikhteh.\n'
            '%\n'
            '% The current maintainer of this work is Amer Amikhteh.\n'
            '%\n'
        )

        # File identification
        f.write(
                '\n\n\n'
            '\\ProvidesFile{persian-captions.def}\n'
            '[2026/08/27 v0.1 Persian translations for LaTeX captions '
            'and package/class names]\n'
            '\n'
        )

        # Document-level definitions
        if 'document' in config:
            for key, value in config['document'].items():
                params = get_params(value)
                f.write(
                    f'\\def\\{key}{params}{{{value}}}\n'
                )

            f.write('\n')

        # Package, class, and translator definitions
        for section in config.sections():

            if section == 'document':
                continue

            if section == 'translator':
                f.write(
                    '\\IfPackageLoadedTF{translator}{\n'
                )

                for key, value in config[section].items():
                    f.write(
                        f'    \\providetranslation{{{key}}}{{{value}}}\n'
                    )

                f.write('}{}%\n\n')
                continue

            if section.startswith('class:'):
                class_name = section.removeprefix('class:')

                f.write(
                    f'\\IfClassLoadedTF{{{class_name}}}{{\n'
                )

                if class_name == 'beamer':
                    f.write(
                        '    \\languagepath{Persian}\n'
                    )

                    write_translations(
                        f,
                        config[section]
                    )
                else:
                    write_definitions(
                        f,
                        config[section]
                    )

                f.write('}{}%\n\n')
                continue

            f.write(
                f'\\IfPackageLoadedTF{{{section}}}{{\n'
            )

            write_definitions(
                f,
                config[section]
            )

            f.write('}{}%\n\n')

        # End of file
        f.write('\\endinput\n')

    print(f"Successfully generated: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--output')
    args = parser.parse_args()

    generate_def(args.output)
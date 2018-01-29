#!/usr/bin/env python3
import argparse
import json
import yaml


def write_json(target, manifest):
    with open(target, 'w', encoding='utf-8') as g:
        json.dump(obj=manifest, fp=g, indent=4)
        g.write('\n')


def main():
    '''The master copy is YAML so we can have comments.'''
    parser = argparse.ArgumentParser()
    parser.add_argument('--nightly', metavar='PATH',
                        help='Write nightly build manifest to PATH')
    args = parser.parse_args()

    with open('org.freedesktop.Bustle.yaml', 'r', encoding='utf-8') as f:
        manifest = yaml.load(f)

    write_json('org.freedesktop.Bustle.json', manifest)

    if args.nightly:
        bustle_module_source = manifest['modules'][-1]["sources"][0]
        bustle_module_source['branch'] = 'master'
        del bustle_module_source['commit']

        manifest['tags'] = ['nightly']
        manifest['desktop-file-name-prefix'] = '(Nightly) '

        write_json(args.nightly, manifest)


if __name__ == '__main__':
    main()

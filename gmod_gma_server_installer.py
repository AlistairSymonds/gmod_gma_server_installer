import argparse as ap
from pathlib import Path
import sys
import subprocess

def main():
    parser = ap.ArgumentParser()
    parser.add_argument("--gmod_dir", required=True)
    parser.add_argument("--gma_dir", required=True)

    args = parser.parse_args()

    gmod_path = Path(args.gmod_dir)
    gma_search_path = Path(args.gma_dir)

    gmad_path = None
    if (gmod_path / 'bin' / 'gmad.exe').exists():
        gmad_path = (gmod_path / 'bin' / 'gmad.exe')
    elif (gmod_path / 'bin' / 'gmad_linux').exists():
        gmad_path = (gmod_path / 'bin' / 'gmad_linux')
    else:
        print("Searched the following paths for gmad:")
        print(gmod_path / 'bin' / 'gmad.exe')
        print(gmod_path / 'bin' / 'gmad_linux')
        print("Couldn't find gmad - exiting")
        sys.exit(1)

    print("Recursively searching " + str(gma_search_path) + " for .gma files to extract and add" )
    gma_glob = gma_search_path.glob('**/*.gma')
    gmas = list(gma_glob)
    print("Found the following gmod addon files: " )
    for p in gmas:
        print(p)
    print("total addons found: " + str(len(gmas)) )
    print("Extracting using: " + str(gmad_path))

    for p in gmas:
        gmad_cmd = [str(gmad_path.absolute()), 'extract', '-file', '', '-out', '']
        gmad_cmd[3] = str(p.absolute())
        gmad_cmd[5] = str((gmod_path / 'garrysmod').absolute())
        print(gmad_cmd)
        subprocess.run(gmad_cmd, capture_output=True)

if __name__== "__main__":
    main()
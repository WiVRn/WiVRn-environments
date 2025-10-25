#!/usr/bin/env python3

import os
import subprocess

SCRIPT_DIR=os.path.dirname(__file__)
BASE_DIR=os.path.dirname(SCRIPT_DIR)

ENV_DIR = os.path.join(BASE_DIR, "environments")

def export(blender, src, dst):
    subprocess.check_call([blender, "-b", "-P", os.path.join(SCRIPT_DIR, "blender_gltf_converter.py"), "--", src, dst]) 

def export_all(blender):
    for dir in os.listdir(ENV_DIR):
        dir = os.path.join(ENV_DIR, dir)
        if not os.path.isdir(dir):
            continue

        for f in os.listdir(dir):
            if f.endswith(".blend"):
                export(blender, os.path.join(dir, f), f[:-5] + "glb")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser("Export blend files to gltf")
    parser.add_argument("--blender-path", default="blender")

    args = parser.parse_args()

    export_all(args.blender_path)

#!/usr/bin/env python3

import json
import os
import subprocess

SCRIPT_DIR=os.path.dirname(__file__)
BASE_DIR=os.path.dirname(SCRIPT_DIR)

ENV_DIR = os.path.join(BASE_DIR, "environments")

def export(blender: str, src: str, dst: str):
    subprocess.check_call([blender, "-b", "-P", os.path.join(SCRIPT_DIR, "blender_gltf_converter.py"), "--", src, dst]) 

def export_all(blender: str) -> list:
    meta = []
    for dir in os.listdir(ENV_DIR):
        dir = os.path.join(ENV_DIR, dir)
        if not os.path.isdir(dir):
            continue

        for f in os.listdir(dir):
            if f.endswith(".blend"):

                base = f[:-6]
                out = f"{base}.glb"

                m = json.load(open(os.path.join(dir, f"{base}.json")))

                export(blender, os.path.join(dir, f), out)
                m["url"] = out
                m["size"] = os.stat(out).st_size
                meta.append(m)
    return meta

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser("Export blend files to gltf")
    parser.add_argument("--blender-path", default="blender")

    args = parser.parse_args()

    meta = export_all(args.blender_path)
    with open("index.json", "w") as f:
        json.dump(meta, f)

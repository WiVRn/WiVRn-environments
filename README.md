# Custom environments for [WiVRn](https://github.com/WiVRn/WiVRn)
This repository hosts 3D models that can be used in the lobby of WiVRn's headset application.

# Contributing
In order to create a new environment, fork the project, create a new directory at the top level and save a blender file in it.
It is recommended to have all the assets stored out of the blender file, in the same directory.

Write a JSON file with the same name as the blender file with the following content:
```json
{
	"name": "<name of the environment>",
	"description": "<long description>",
	"author": "<your name or nickname>"
}
```

Once integrated, automation will [export a glb](https://docs.blender.org/manual/en/4.5/addons/import_export/scene_gltf2.html) file from your blend and generate a preview using the default camera. Due to limitations in the WiVRn renderer, only texture colours and per-vertex normals will be used, there is no support for light sources.

It is recommended to first test the exported file through `scripts/export-all.py` (pass `--blender-path` to specify the blender binary to use). You can then upload the glb to the headset and in WiVRn open from the customize tab.

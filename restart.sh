#!/bin/bash

podman stop PH-FileSystem

podman rm PH-FileSystem

podman image rm ph-file-system

podman build -t=ph-file-system .

podman run -dt -p 40003:2000 --cpus=0.25 -m=256m --name=PH-FileSystem ph-file-system
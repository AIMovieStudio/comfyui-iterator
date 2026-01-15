# Iterator Load Image

Loads an image from a specific file path.

## Inputs
- **file_path**: The absolute path to the image file.

## Outputs
- **image**: The loaded image as a ComfyUI IMAGE tensor.
- **filename**: The name of the file (without path).

## Usage
Use this node in conjunction with `Iterator List Files`. Connect the `file_paths` output from the list node to the `file_path` input of this node. This allows you to iterate over all images in a folder.

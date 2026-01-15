# Iterator Load String

Loads text content from a specific file path.

## Inputs
- **file_path**: The absolute path to the text file.

## Outputs
- **content**: The content of the file as a string.
- **filename**: The name of the file (without path).

## Usage
Use this node in conjunction with `Iterator List Files`. Connect the `file_paths` output from the list node to the `file_path` input of this node. This allows you to iterate over all text files in a folder.

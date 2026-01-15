# Iterator List Files

Lists files in a specified directory, filtering by extension.

## Inputs
- **directory**: The absolute path to the directory to scan.
- **extension**: Comma-separated list of file extensions to include (e.g., `png, jpg, txt`). Default: `png, jpg, jpeg, webp, bmp`.
- **limit**: Maximum number of files to return. Set to `0` for no limit.

## Outputs
- **file_paths**: A list of file paths found in the directory.

## Usage
Connect this node to `Iterator Load Image` or `Iterator Load String` to process the found files. When this node outputs a list, downstream nodes will typically execute for each item in the list (batch processing).

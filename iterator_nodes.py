import torch
import os
import numpy as np
from PIL import Image, ImageOps

class IteratorListFiles:
    """Lists files in a directory, returning paths as a list of strings.
    Get the list of files to process."""
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "directory": ("STRING", {"default": ""}),
            },
            "optional": {
                "extension": ("STRING", {"default": "png, jpg, jpeg, webp, bmp, txt, json, csv, md"}),
                "limit": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("file_paths",)
    FUNCTION = "list_files"
    CATEGORY = "Iterator"
    OUTPUT_IS_LIST = (True,)

    def list_files(self, directory, extension="png, jpg, jpeg, webp, bmp, txt, json, csv, md", limit=0):
        if not os.path.isdir(directory):
            print(f"Directory not found: {directory}")
            return ([],)

        extensions = [e.strip().lower() for e in extension.split(",")]
        
        files = []
        try:
            for f in os.listdir(directory):
                ext = os.path.splitext(f)[1].lower().replace(".", "")
                if ext in extensions:
                    files.append(os.path.join(directory, f))
        except Exception as e:
            print(f"Error listing files: {e}")
            return ([],)
        
        files.sort()
        
        if limit > 0:
            files = files[:limit]

        return (files,)

class IteratorLoadImage:
    """Loads a single image from a file path.
    Load the content (Image)."""
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "file_path": ("STRING", {"default": "", "forceInput": True}),
            }
        }

    RETURN_TYPES = ("IMAGE", "STRING")
    RETURN_NAMES = ("image", "filename")
    FUNCTION = "load_image"
    CATEGORY = "Iterator"

    def load_image(self, file_path):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        i = Image.open(file_path)
        i = ImageOps.exif_transpose(i)
        if i.mode == 'I':
            i = i.point(lambda x: x * (1 / 255))
        image = i.convert("RGB")
        image = np.array(image).astype(np.float32) / 255.0
        image = torch.from_numpy(image)[None,]
        
        filename = os.path.basename(file_path)
        return (image, filename)

class IteratorLoadString:
    """Loads text content from a single file.
    Load the content (String)."""
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "file_path": ("STRING", {"default": "", "forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("content", "filename")
    FUNCTION = "load_string"
    CATEGORY = "Iterator"

    def load_string(self, file_path):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Try multiple encodings
        encodings = ['utf-8-sig', 'utf-16', 'shift_jis', 'cp932', 'euc_jp', 'cp1252', 'latin-1']
        content = None
        
        for enc in encodings:
            try:
                with open(file_path, 'r', encoding=enc) as f:
                    content = f.read()
                break
            except (UnicodeDecodeError, UnicodeError):
                continue
        
        if content is None:
            # Final fallback: read as utf-8 with replacement for invalid characters
            with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
        
        filename = os.path.basename(file_path)
        return (content, filename)

from .iterator_nodes import (
    IteratorListFiles,
    IteratorLoadImage,
    IteratorLoadString,
)

NODE_CLASS_MAPPINGS = {
    "IteratorListFiles": IteratorListFiles,
    "IteratorLoadImage": IteratorLoadImage,
    "IteratorLoadString": IteratorLoadString,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "IteratorListFiles": "Iterator List Files",
    "IteratorLoadImage": "Iterator Load Image",
    "IteratorLoadString": "Iterator Load String",
}

WEB_DIRECTORY = "./web"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]

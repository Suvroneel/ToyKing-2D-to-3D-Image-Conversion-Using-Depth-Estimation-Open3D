import cv2
import numpy as np
import base64

# Replace dummy_depth_model with your real depth estimation model
def image_to_pseudo_3d(img: np.ndarray, invert: bool = True) -> str:
    """
    Converts an RGB image to pseudo-3D depth image and returns base64 PNG.
    """
    depth_map = dummy_depth_model(img)

    # Normalize and invert depth
    depth_norm = cv2.normalize(depth_map, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    if invert:
        depth_norm = 255 - depth_norm

    # Apply color map
    depth_colored = cv2.applyColorMap(depth_norm, cv2.COLORMAP_JET)

    # Encode PNG in-memory
    success, buffer = cv2.imencode(".png", depth_colored)
    if not success:
        raise RuntimeError("Failed to encode depth image")

    return base64.b64encode(buffer).decode("utf-8")


def dummy_depth_model(img):
    """
    Dummy depth map generator for testing.
    Replace with your real depth estimation model.
    """
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    depth_map = cv2.GaussianBlur(gray, (7, 7), 0)
    return depth_map

from PIL import Image, ImageFilter
import argparse

def apply_filter(image_path, filter_name):
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: Image not found at '{image_path}'")
        return

    filters = {
        "blur": ImageFilter.BLUR,
        "contour": ImageFilter.CONTOUR,
        "sharpen": ImageFilter.SHARPEN
    }

    if filter_name in filters:
        filtered = img.filter(filters[filter_name])
        filtered.show()
        output_name = f"filtered_{filter_name}.jpg"
        filtered.save(output_name)
        print(f"Filtered image saved as {output_name}")
    else:
        print("Error: Filter not recognized. Available filters are: blur, contour, sharpen")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Apply a filter to an image using PIL.")
    parser.add_argument("image_path", help="Path to the input image file")
    parser.add_argument("filter_name", help="Name of the filter to apply (blur, contour, sharpen)")
    
    args = parser.parse_args()
    apply_filter(args.image_path, args.filter_name)

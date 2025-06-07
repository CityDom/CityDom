style digital_text:
    font "DS-DIGI.TTF"
    size 40

# Define a scaling factor
define scale_factor = 0.7

init python:
    def scale_image(image, scale):
        # Load the image and get its size
        img = renpy.load_image(image)
        width, height = img.get_size()
        return im.Scale(image, int(width * scale), int(height * scale))

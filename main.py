# check for existing training and valid slideshow, if yes, skip making slides
from pathlib import Path
from SlideShow import SlideShow
from ImageHomography import transform, get_transform_h

def main() -> None : 
    # Make slides
    train_slides = SlideShow(path="data\\y", amount=500)
    valid_slides = SlideShow(path="data\\y_valid", amount=200)
    surface_slides = SlideShow(path="data\\surface", amount=1)
    
    train_slides.make_slides(name="train_y")
    valid_slides.make_slides(name="valid_y")
    surface_slides.make_slides(name="surface")

    # Projecting and Capturing slides
    # Change camera index if needed
    camera_index = 0

    train_slides.project(output_path="data\\surf1\\train\\x", camera_index=camera_index)
    valid_slides.project(output_path="data\\surf1\\valid\\x", camera_index=camera_index)
    surface_slides.project(output_path="data\\surf1\\train\\s", camera_index=camera_index)
    surface_slides.project(output_path="data\\surf1\\valid\\s", camera_index=camera_index)

    # Resize
    homography = get_transform_h()
    print(homography)
    transform(path="data\\surf1\\train\\x", amount=500, homography=homography)
    transform(path="data\\surf1\\valid\\x", amount=200, homography=homography)
    transform(path="data\\surf1\\train\\s", amount=1, homography=homography)
    transform(path="data\\surf1\\valid\\s", amount=1, homography=homography)

    # Save data to zip

    # Maybe upload it - can be impossible
if __name__ == "__main__" :
    main()
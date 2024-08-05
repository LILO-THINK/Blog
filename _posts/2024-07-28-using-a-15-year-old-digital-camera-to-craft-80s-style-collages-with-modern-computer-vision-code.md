---
layout: post
title: Using a 15-Year-Old Digital Camera to Craft 80s-Style Collages with Modern Computer Vision Code
id: 2024-07-28-using-a-15-year-old-digital-camera-to-craft-80s-style-collages-with-modern-computer-vision-code.md
categories:
  - documentation
  - digital tools
  - image
image: https://live.staticflickr.com/65535/53885511802_6bf251bd43_z.jpg
share: "true"
comments: "true"
filename: Blog/_posts/2024-07-28-using-a-15-year-old-digital-camera-to-craft-80s-style-collages-with-modern-computer-vision-code.md
tags:
  - photos
  - python
  - opencv
  - camera
  - homemade2024
date: 2024-07-28
author: lina
---

In today's fast-paced digital world, where new camera models are launched every year, it's easy to forget the charm and capabilities of older equipment. This blog post explores the creative possibilities of using an older digital camera, the Canon EOS 40D, released in 2007. We dive into its historical significance, its impact on photography, and how it can still be a powerful tool for artistic expression today. Inspired by the works of David Hockney, we will recreate his iconic photographic collages using modern techniques and Python scripts.

#### The Canon EOS 40D: A Glimpse into the Past

Released in August 2007, the Canon EOS 40D was a significant advancement in digital photography. It featured a 10.1-megapixel APS-C CMOS sensor, a DIGIC III image processor, and the ability to shoot at 6.5 frames per second. This camera bridged the gap between amateur and professional photography, offering features like Live View mode and a robust magnesium alloy body. At the time, it was celebrated for its high image quality, speed, and durability.

#### David Hockney and Photographic Collages

David Hockney, a renowned British artist, revolutionized the art world with his unique photographic collages, often referred to as "joiners." In the 1980s, Hockney created these works by taking multiple photographs of a scene and arranging them to form a larger, composite image. This technique allowed him to capture multiple perspectives and moments in a single piece, challenging the conventional notions of time and space in photography.

To see more, check his [webpage](https://www.hockney.com/works/photos/photographic-collages).
I'm a huge fun of his concept as you can see in my time during my studies in the Cinema School [[2006-06-01-do-you-always-step-inside-people-s-minds]]
#### Modern Techniques with an Old Camera

Despite being over a decade old, the Canon EOS 40D remains a versatile tool for creative projects. Inspired by Hockney's joiners, we can use this camera to capture a series of images and combine them into a cohesive collage. Here's how you can do it:

1. **Capture the Images**:
    - Use the Canon EOS 40D to take multiple overlapping photographs of your subject. Ensure significant overlap (30-50%) between shots.
    - Vary the angles and perspectives slightly to add depth to the final collage.

2. **Processing with Python and OpenCV**:
    - Use Python scripts to automate the stitching and blending process. OpenCV, a powerful image processing library, can detect features, match them, and align the images seamlessly.
    - Add artistic effects like borders, rotations, and adjustable opacity to mimic Hockney's style.

#### Many Iterations Later

When I first experimented with creating a Hockney-style collage using my Canon EOS 40D, the initial script in Python employed OpenCV's stitching capabilities to produce an impeccably uniform image. This high-resolution, seamless result, while technically impressive, felt at odds with the essence of my project. I was using an early digital camera to reference David Hockney, an artist known for his analog photographic collages, which celebrated imperfections and unique perspectives. The digital precision seemed to overshadow the analog charm I sought to emulate.

<img src="https://live.staticflickr.com/65535/53886765454_ff0d4bcea1_z.jpg" />

Realizing this, I decided to embrace a touch of glitch, aiming for a more experimental feel that echoed the analog spirit of Hockney's work. The challenge became finding ways to introduce deliberate imperfections, creating a collage that blended the old with the new. This exercise in balancing digital precision with analog character led to a final piece that honored both the technological advancements and the artistic quirks of different eras.

You can check in this gallery on Flick the iteractions along the process 🫀
<a data-flickr-embed="true" href="https://www.flickr.com/photos/200845412@N02/albums/72177720319181700" title="2024 07 PyCV à lá Hockney"><img src="https://live.staticflickr.com/65535/53885511802_6bf251bd43_z.jpg" width="640" height="480" alt="2024 07 PyCV à lá Hockney"/></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

#### Example Python Script

Here’s a simplified version of the Python script we used to create our Hockney-style collage:

```python
import cv2
import numpy as np
import glob
import random

def add_border(image, border_size=2):
    return cv2.copyMakeBorder(image, border_size, border_size, border_size, border_size, cv2.BORDER_CONSTANT, value=[255, 255, 255])

image_files = [f'_MG_{i}.JPG' for i in range(9737, 9789)]
images = [cv2.imread(img) for img in image_files]
resized_images = [cv2.resize(img, (600, 400)) for img in images]
bordered_images = [add_border(img) for img in resized_images]

collage_height = 3000
collage_width = 5000
collage = np.ones((collage_height, collage_width, 3), dtype=np.uint8) * 255

sift = cv2.SIFT_create()
keypoints_descriptors = [sift.detectAndCompute(img, None) for img in bordered_images]

index_params = dict(algorithm=1, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)

base_img = bordered_images[0]
h, w = base_img.shape[:2]
collage_center_x = collage_width // 2 - w // 2
collage_center_y = collage_height // 2 - h // 2
collage[collage_center_y:collage_center_y+h, collage_center_x:collage_center_x+w] = base_img
placed_images = [(collage_center_y, collage_center_x, h, w, base_img, keypoints_descriptors[0])]

def find_best_match_position(img, kp_des, placed_images):
    best_match = None
    best_position = None
    for (y, x, h, w, placed_img, kp_des_placed) in placed_images:
        matches = flann.knnMatch(kp_des[1], kp_des_placed[1], k=2)
        good_matches = [m for m, n in matches if m.distance < 0.7 * n.distance]
        if len(good_matches) > 10:
            src_pts = np.float32([kp_des[0][m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
            dst_pts = np.float32([kp_des_placed[0][m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
            M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
            if M is not None:
                h, w = img.shape[:2]
                pts = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
                dst = cv2.perspectiveTransform(pts, M)
                dst += np.float32([[[x, y]]])
                min_x, min_y = np.int32(dst.min(axis=0).ravel() - 0.5)
                max_x, max_y = np.int32(dst.max(axis=0).ravel() + 0.5)
                if min_x >= 0 and min_y >= 0 and max_x <= collage_width and max_y <= collage_height:
                    if best_match is None or len(good_matches) > best_match:
                        best_match = len(good_matches)
                        best_position = (min_y, min_x)
    return best_position

for i in range(1, len(bordered_images)):
    best_position = find_best_match_position(bordered_images[i], keypoints_descriptors[i], placed_images)
    if best_position:
        y, x = best_position
        h, w = bordered_images[i].shape[:2]
        
        angle = random.uniform(-5, 5)
        M = cv2.getRotationMatrix2D((w // 2, h // 2), angle, 1)
        rotated_img = cv2.warpAffine(bordered_images[i], M, (w, h), borderValue=(255, 255, 255))
        
        if x + w <= collage_width and y + h <= collage_height:
            blend_region = collage[y:y+h, x:x+w]
            alpha = 0.5
            blended = cv2.addWeighted(rotated_img, alpha, blend_region, 1 - alpha, 0)
            collage[y:y+h, x:x+w] = blended
        
            placed_images.append((y, x, h, w, bordered_images[i], keypoints_descriptors[i]))

cv2.imwrite('hockney_collage.jpg', collage)
print("Collage created successfully. Saved as 'hockney_collage.jpg'.")

cv2.imshow('Hockney Collage', collage)
cv2.waitKey(0)
cv2.destroyAllWindows()

```

#### Conclusion

The Canon EOS 40D, despite its age, proves to be a versatile and creative tool for modern photography projects. By combining the camera's capabilities with Python and OpenCV, we can recreate the artistic style of David Hockney's photographic collages. This journey not only pays homage to the past but also showcases the timeless nature of creativity and technology.

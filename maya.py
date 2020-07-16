import cv2
import numpy as np
import matplotlib.pyplot as plt

background = cv2.imread('./Imagenes/FondoNegro.png')
overlay = cv2.imread('./Imagenes/cero1.png')
overlay = cv2.resize(overlay, (200,100))

rows,cols,channels = overlay.shape

background[100:100+rows, 0:0+cols ] = overlay

plt.imshow(overlay)
plt.show()

def overlay_transparent(background, overlay, x, y):

    background_width = background.shape[1]
    background_height = background.shape[0]

    if x >= background_width or y >= background_height:
        return background

    h, w = overlay.shape[0], overlay.shape[1]

    if x + w > background_width:
        w = background_width - x
        overlay = overlay[:, :w]

    if y + h > background_height:
        h = background_height - y
        overlay = overlay[:h]

    if overlay.shape[2] < 4:
        overlay = np.concatenate(
            [
                overlay,
                np.ones((overlay.shape[0], overlay.shape[1], 1), dtype = overlay.dtype) * 255
            ],
            axis = 2,
        )

    overlay_image = overlay[..., :3]
    mask = overlay[..., 3:] / 255.0

    background[y:y+h, x:x+w] = (1.0 - mask) * background[y:y+h, x:x+w] + mask * overlay_image

    return background

plt.imshow(overlay_transparent(background,overlay,5,5))
plt.axis("off")
plt.show()

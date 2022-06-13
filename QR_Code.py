from qrcode.constants import ERROR_CORRECT_H
import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=15,border=4,)
qr.add_data("https://github.com/ankitkumar0021")
qr.make(fit =True)
img=qr.make_image(fill_color="black",back_color="white")
img.save("MYgithub.png")
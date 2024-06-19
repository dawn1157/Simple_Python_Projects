import qrcode as qr
from PIL import Image as img
# PIL helps to formating and editing

image = qr.QRCode(version= 1, 
                error_correction= qr.constants.ERROR_CORRECT_H,
                box_size=10, border= 5)

image.add_data('https://www.apple.com/shop/buy-mac/macbook-pro/16-inch-space-gray-apple-m2-max-with-12-core-cpu-and-38-core-gpu-1tb')
image.make(fit=True)
qr_code = image.make_image(fill_color = 'maroon',
                           back_color = 'white')
qr_code.save('05_QR_code_generator/advance_qr.png')
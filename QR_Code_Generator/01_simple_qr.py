import qrcode as qr

input = input
# print(dir(qr))

qr_code = qr.make('https://www.apple.com/shop/buy-mac/macbook-pro/16-inch-space-gray-apple-m2-max-with-12-core-cpu-and-38-core-gpu-1tb')
# .make() --> helps us make the qr code!
qr_code.save('05_QR_code_generator/my_qr_dawn.jpeg')
# .save() --> helps us save the image in any format .png/.jpeg etc.




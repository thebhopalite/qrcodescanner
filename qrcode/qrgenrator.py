import qrcode
qr=qrcode.QRCode(version=1,border=5,box_size=10)


myurl="www.youtube.com/thecodingsniper"
qr.add_data(myurl)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("youtube.png")
print("Qr Code generated")
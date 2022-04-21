import io 
import qrcode
site = "https://canallaneza.art/"
img = qrcode.make(site)
img.save("./qrs/qr.png")
qr = qrcode.QRCode()
qr.add_data(site)
f = io.StringIO()
qr.print_ascii(out=f)
f.seek(0)
print(f.read())

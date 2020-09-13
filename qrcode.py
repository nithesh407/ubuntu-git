import pyqrcode
url = "https://www.hackerrank.com/certificates/cf11ad65396a"
K=pyqrcode.create(url)
K.svg('Qr.svg',scale=8)


import qrcode
data = "Kumar yash"  # add whatever data  you want to show in Qr code after scanning 
qr = qrcode.make(data)
qr.save("qrcode.png")
print("success")
        

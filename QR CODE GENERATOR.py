import qrcode

# Phone number to be encoded in the QR code
phone_number = "tel:+917645053056"  # Replace with the actual phone number

# Create a QR code object
qr = qrcode.QRCode(
    version=1,  # QR code size
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Box size in pixels
    border=4,  # Border thickness (in boxes)
)

# Add the phone number (tel:) to the QR code
qr.add_data(phone_number)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save("phone_number_qr_code.png")

# Show the image
img.show()

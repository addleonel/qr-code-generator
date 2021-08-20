if __name__ == '__main__':
    import qrcode
    from PIL import Image

    OVERLAY_IMAGE = '../images/overlay_image.jpg'  # this is an example
    DATA_CONSTANT = 'https://github.com/addleonel/python-fundamentals'
    SAVE_QR_CODE_PATH = '../qrcode_images/python_fundamentals_with_logo.png'
 
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    qr.add_data(DATA_CONSTANT)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color=(255, 2, 19), 
        back_color=(255, 255, 255),
    )

    logo_display = Image.open(OVERLAY_IMAGE)
    logo_display.thumbnail((70, 70))

    logo_position = ((img.size[0] - logo_display.size[0])//2, (img.size[1] - logo_display.size[1])//2)

    img.paste(logo_display, logo_position)
    img.save(SAVE_QR_CODE_PATH) 
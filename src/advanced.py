if __name__ == '__main__':
    DATA_CONSTANT = 'https://github.com/addleonel/python-fundamentals'
    SAVE_QR_CODE_PATH = '../qrcode_images/red_python_fundamentals.png'

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    qr.add_data(DATA_CONSTANT)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color=(255, 0, 0), 
        back_color=(255, 255, 255),
    )
    
    img.save(SAVE_QR_CODE_PATH)
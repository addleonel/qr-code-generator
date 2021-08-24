if __name__ == '__main__':
    import qrcode
    from PIL import Image, ImageOps, ImageDraw

    
    DATA_CONSTANT = 'https://github.com/addleonel/python-fundamentals'
    SAVE_QR_CODE_PATH = '../qrcode_images/python_fundamentals_background.png'

    # Circular Thumbnail
    image = Image.open('../images/overlay_image.png')
    image = image.resize((120, 120))
    bigsize = (image.size[0]*3, image.size[1]*3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(image.size, Image.ANTIALIAS)
    image.putalpha(mask)
    
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

    img.save(SAVE_QR_CODE_PATH)

    background = Image.open(SAVE_QR_CODE_PATH)

    logo_position = ((background.size[0] - image.size[0])//2, (background.size[1] - image.size[1])//2)

    background.paste(image, logo_position, image)
    background.save('../qrcode_images/python_fundamentals_with_logo_.png') 
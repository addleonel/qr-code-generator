import qrcode
import qrcode.image.svg as qrsvg
from qrcode.image.styledpil import StyledPilImage
# module drawers
from qrcode.image.styles.moduledrawers import (
    RoundedModuleDrawer, GappedSquareModuleDrawer
)



class QRGenerator:

    def __init__(self, text_content, output_path):
        self.text_content = text_content
        self.output_path = output_path

    def provoke(self):
        """
        This is the most easier way to make a qrcode
        just need the following arguments
        text_content -> text, URL, phone, SMS, or any other text
        output_path -> is the name of the generated QRcode file i.e ./qrcode/name_file.ext
        """
        extension = self.output_path.split('.')[-1].lower()
        
        if extension in ('png', 'jpg', 'jpeg'):
            qr_img = qrcode.make(self.text_content)
        elif extension in ('svg',):
            factory = qrsvg.SvgPathImage
            qr_img = qrcode.make(self.text_content, image_factory=factory)    
        
        qr_img.save(self.output_path)



if __name__ == '__main__':
    QR_NAME_FILE = 'python_fundamentals.jpeg'
    DATA_CONSTANT = 'https://github.com/addleonel/python-fundamentals'
    OUTPUT_PATH_ONE = '../qrcode_images/' + QR_NAME_FILE
    
    QRGenerator(DATA_CONSTANT, OUTPUT_PATH_ONE).provoke()
    
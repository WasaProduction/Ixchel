from os import listdir, path


class StartupCheck:
    def __init__(self):
        """ For sidebar """
        # Check for mathing amount of button images and frame files
        btn_img_dir = '/Users/jaimegonzalezquirarte/PycharmProjects/Ixchel/assets/icons/buttons'
        frm_dir = '/Users/jaimegonzalezquirarte/PycharmProjects/Ixchel/UI/Frames'
        len([entry for entry in listdir(btn_img_dir) if path.isfile(path.join(btn_img_dir, entry))])
        if len([entry for entry in listdir(btn_img_dir) if path.isfile(path.join(btn_img_dir, entry))]) == len([entry for entry in listdir(frm_dir) if path.isfile(path.join(frm_dir, entry))]):
            print('missing files')

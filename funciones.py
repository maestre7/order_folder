

def check_type_file(file):
    """Depending on the type of file we put it in one or another folder"""

    doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
    img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff')
    software_types = ('.exe', '.pkg', '.dmg')

    try:
        if file.extension in doc_types:
            return "documents"
        if file.extension in img_types:
            return "images"
        if file.extension in software_types:
            return "software"
        else:
            return None

    except Exception as err:
        raise Exception(f"{__name__}: {err}, {file}")
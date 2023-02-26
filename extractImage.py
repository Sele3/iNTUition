import fitz
import io
import os

images_path = './frontend/public/media/'

def extract_image(file):
    pdf_data = file.read()
    mem_file = io.BytesIO(pdf_data)
    pdf_file = fitz.open(stream=mem_file, filetype='pdf')

    # for page in pdf_file:
    #     # Get the image list from the page
    #     image_list = page.getImageList()

    #     # Iterate over each image in the image list
    #     for image in image_list:
    #         # Get the xref of the image
    #         xref = image[0]

    #         # Get the image data from the xref
    #         img_data = pdf_file.extractImage(xref)

    #         # Write the image data to a file
    #         with open(os.path.join(images_path, f'image{xref}.png') , 'wb') as image_file:
    #             image_file.write(img_data['image'])

    # #         with open('image{}.png'.format(xref), 'wb') as f:
    # #             f.write(img_data['image'])

    # #Calculate number of pages in PDF file
    page_nums = len(pdf_file)

    # #Create empty list to store images information
    images_path = './frontend/public/media/'

    #Extract all images information from each page
    for page_num in range(page_nums):
        images_list = []
        page_content = pdf_file[page_num]
        images_list.extend(page_content.get_images())

        for i, image in enumerate(images_list, start=1):
            #Extract the image object number
            xref = image[0]
            #Extract image
            base_image = pdf_file.extract_image(xref)
            #Store image bytes
            image_bytes = base_image['image']
            #Store image extension
            image_ext = base_image['ext']
            #Generate image file name
            image_name = str(i) + '.' + image_ext
            #Save image
            with open(os.path.join(images_path, image_name) , 'wb') as image_file:
                image_file.write(image_bytes)
                
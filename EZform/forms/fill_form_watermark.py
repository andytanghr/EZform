import os
import sys
from fpdf import FPDF
from PyPDF2 import PdfFileReader, PdfFileWriter

def makePDF(customerData):
    # declare location of PDFs to use
    overlay_pdf_file_name = 'overlay_PDF.pdf' # textOverSuccess.pdf
    pdf_template_file_name = 'DL43.pdf' # base_PDF_template


    pdf = FPDF('P', 'mm', 'letter') # paragraph oriented, millimeters measured, letter page sized
    pdf.add_page()
    pdf.set_font('Arial', '', 12) # font, style ('' means normal), 14pt

    ### test dictionary for overlay data
    ### WORKS

    result_pdf_file_name = "./forms/pdfs/" + customerData['last_name'] + ".pdf"
    form_dictionary = \
    {
        'form': 'ACCT',
        'data': [
                # initial x = 23, initial y = 20, shift x by 5, y by 7
                { 'x': 28, 'y': 27, 'w': 77, 'h': 3, 'value': customerData['last_name'] }, # last name
                { 'x': 28, 'y': 31, 'w': 74, 'h': 3, 'value': customerData['first_name'] }, # first name
                { 'x': 31, 'y': 36, 'w': 73, 'h': 3, 'value': customerData['middle_name'] }, # middle name
                { 'x': 22, 'y': 41, 'w': 82, 'h': 3, 'value': customerData['suffix'] }, # suffix
                # { 'x': 31, 'y': 36, 'w': 73, 'h': 3, 'value': customerData['maiden_name'] }, # maiden name
                { 'x': 55, 'y': 52, 'w': 12, 'h': 3, 'value': str(customerData['birth_month']) }, # birth month (##)
                { 'x': 71, 'y': 52, 'w': 12, 'h': 3, 'value': str(customerData['birthday']) }, # birthday (##)
                { 'x': 87, 'y': 52, 'w': 12, 'h': 3, 'value': str(customerData['birth_year']) }, # birth year (####)
                { 'x': 17, 'y': 55, 'w': 20, 'h': 3, 'value': customerData['SSN1'] },
                { 'x': 43, 'y': 55, 'w': 16, 'h': 3, 'value': customerData['SSN2'] }, # SSN2 (##)
                { 'x': 65, 'y': 55, 'w': 27, 'h': 3, 'value': customerData['SSN3'] }, # SSN3 (####)
                { 'x': 33, 'y': 62, 'w': 3, 'h': 3, 'value': customerData['male'] }, # sex male
                { 'x': 48, 'y': 62, 'w': 3, 'h': 3, 'value': customerData['female'] }, # sex female
                { 'x': 92, 'y': 62, 'w': 12, 'h': 3, 'value': customerData['weight'] }, # weight (lbs)
                { 'x': 29, 'y': 66, 'w': 25, 'h': 3, 'value': customerData['eye_color'] }, # eye color
                { 'x': 72, 'y': 66, 'w': 12, 'h': 3, 'value': customerData['height_ft'] }, # height (ft)
                { 'x': 92, 'y': 66, 'w': 12, 'h': 3, 'value': customerData['height_in'] }, # height (in)
                # { 'x': 35, 'y': 71, 'w': 9, 'h': 3, 'value': customerData['race'] }, # race
                #
                # # contact information
                { 'x': 132, 'y': 27, 'w': 68, 'h': 3, 'value': customerData['home_phone'] }, # home phone
                { 'x': 133, 'y': 32, 'w': 66, 'h': 3, 'value': customerData['other_phone'] }, # other phone
                { 'x': 121, 'y': 37, 'w': 78, 'h': 3, 'value': customerData['email'] }, # email
                #
                # address information
                { 'x': 144, 'y': 48, 'w': 56, 'h': 3, 'value': customerData['residential_address'] }, # residential address
                { 'x': 119, 'y': 53, 'w': 49, 'h': 3, 'value': customerData['residential_city'] }, # residential city
                { 'x': 180, 'y': 53, 'w': 20, 'h': 3, 'value': customerData['residential_state'] }, # residential state
                { 'x': 126, 'y': 59, 'w': 25, 'h': 3, 'value': customerData['residential_zip'] }, # residential ZIP
                { 'x': 166, 'y': 59, 'w': 34, 'h': 3, 'value': customerData['residential_county'] }, # residential county

                # if residential address is same as mailing, values in this group will be the same as the group immediately above
                { 'x': 138, 'y': 64, 'w': 62, 'h': 3, 'value': customerData['mailing_address'] }, # mailing address
                { 'x': 119, 'y': 69, 'w': 49, 'h': 3, 'value': customerData['mailing_city'] }, # mailing city
                { 'x': 180, 'y': 69, 'w': 20, 'h': 3, 'value': customerData['mailing_state'] }, # mailing state
                { 'x': 126, 'y': 74, 'w': 25, 'h': 3, 'value': customerData['mailing_zip'] }, # mailing ZIP
                { 'x': 167, 'y': 74, 'w': 33, 'h': 3, 'value': customerData['mailing_county'] }, # mailing county
                { 'x': 14.5, 'y': 90.5, 'w': 3, 'h': 3, 'value': customerData['q1yes'] }, # Q1 Y
                { 'x': 22.4, 'y': 90.5, 'w': 3, 'h': 3, 'value': customerData['q1no'] }, # Q1 N
                { 'x': 14.5, 'y': 94.4, 'w': 3, 'h': 3, 'value': customerData['q2yes'] }, # Q2 Y
                { 'x': 22.4, 'y': 94.4, 'w': 3, 'h': 3, 'value': customerData['q2no'] }, # Q2 N
                { 'x': 14.5, 'y': 108.5, 'w': 3, 'h': 3, 'value': customerData['q3yes'] }, # Q3 Y
                { 'x': 22.4, 'y': 108.5, 'w': 3, 'h': 3, 'value': customerData['q3no'] }, # Q3 N
                { 'x': 14.5, 'y': 112.4, 'w': 3, 'h': 3, 'value': customerData['q4yes'] }, # Q4 Y
                { 'x': 22.4, 'y': 112.4, 'w': 3, 'h': 3, 'value': customerData['q4no'] }, # Q4 N
                { 'x': 192, 'y': 112, 'w': 8.5, 'h': 3, 'value': customerData['q4_amount'] }, # Q4 $ amount
                { 'x': 14.5, 'y': 116.2, 'w': 3, 'h': 3, 'value': customerData['q5yes'] }, # Q5 Y
                { 'x': 22.4, 'y': 116.2, 'w': 3, 'h': 3, 'value': customerData['q5no'] }, # Q5 N
                { 'x': 14.5, 'y': 120.1, 'w': 3, 'h': 3, 'value': customerData['q6yes'] }, # Q6 Y
                { 'x': 22.4, 'y': 120.1, 'w': 3, 'h': 3, 'value': customerData['q6no'] }, # Q6 N
                { 'x': 159, 'y': 120, 'w': 8, 'h': 3, 'value': customerData['q6amount'] }, # Q6 # amount
                { 'x': 14.5, 'y': 127.2, 'w': 3, 'h': 3, 'value': customerData['q7yes'] }, # Q7 Y
                { 'x': 22.4, 'y': 127.2, 'w': 3, 'h': 3, 'value': customerData['q7no'] }, # Q7 N
                { 'x': 134, 'y': 127, 'w': 8, 'h': 3, 'value': customerData['q7amount'] }, # Q7 $ amount
                { 'x': 14.5, 'y': 131.4, 'w': 3, 'h': 3, 'value': customerData['q8yes'] }, # Q8 Y
                { 'x': 22.4, 'y': 131.4, 'w': 3, 'h': 3, 'value': customerData['q8no'] }, # Q8 N
                { 'x': 153, 'y': 130, 'w': 51, 'h': 3, 'value': customerData['q8text'] }, # Q8 text
                { 'x': 14.5, 'y': 138.8, 'w': 3, 'h': 3, 'value': customerData['q9yes'] }, # Q9 Y
                { 'x': 22.4, 'y': 138.8, 'w': 3, 'h': 3, 'value': customerData['q9no'] }, # Q9 N
                { 'x': 14.5, 'y': 150.4, 'w': 3, 'h': 3, 'value': customerData['q10yes'] }, # Q10 Y
                { 'x': 22.4, 'y': 150.4, 'w': 3, 'h': 3, 'value': customerData['q10no'] }, # Q10 N
                { 'x': 41, 'y': 154, 'w': 43, 'h': 3, 'value': customerData['q10a_emergency_name'] }, # Q10a emergency name
                { 'x': 109, 'y': 154, 'w': 35, 'h': 3, 'value': customerData['q10a_emergency_phone'] }, # Q10a emergency phone number
                { 'x': 155, 'y': 154, 'w': 48, 'h': 3, 'value': customerData['q10a_emergency_address'] }, # Q10a emergency address
                { 'x': 41, 'y': 158, 'w': 43, 'h': 3, 'value': customerData['q10b_emergency_name'] }, # Q10b emergency name
                { 'x': 109, 'y': 158, 'w': 35, 'h': 3, 'value': customerData['q10b_emergency_phone'] }, # Q10b emergency phone number
                { 'x': 155, 'y': 158, 'w': 48, 'h': 3, 'value': customerData['q10b_emergency_address'] }, # Q10b emergency address
                { 'x': 14.5, 'y': 167.7, 'w': 3, 'h': 3, 'value': customerData['q11yes'] }, # Q11 Y
                { 'x': 22.4, 'y': 153, 'w': 3, 'h': 3, 'value': customerData['q11no'] }, # Q11 N
                { 'x': 63, 'y': 173, 'w': 3, 'h': 3, 'value': customerData['q11improved'] }, # Q11 improved
                { 'x': 85, 'y': 175, 'w': 3, 'h': 3, 'value': customerData['q11deteriorated'] }, # Q11 deteriorated
                { 'x': 14.5, 'y': 153, 'w': 3, 'h': 3, 'value': customerData['q12yes'] }, # Q12 Y
                { 'x': 17.4, 'y': 153, 'w': 3, 'h': 3, 'value': customerData['q12no'] }, # Q12 N
                { 'x': 30, 'y': 153, 'w': 174, 'h': 3, 'value': customerData['q12text'] }, # Q12 text
                { 'x': 14.5, 'y': 153, 'w': 3, 'h': 3, 'value': customerData['q13yes'] }, # Q13 Y
                { 'x': 22.4, 'y': 153, 'w': 3, 'h': 3, 'value': customerData['q13no'] }, # Q13 N
                { 'x': 14.5, 'y': 153, 'w': 3, 'h': 3, 'value': customerData['q14yes'] }, # Q14 Y
                { 'x': 22.4, 'y': 153, 'w': 3, 'h': 3, 'value': customerData['q14no'] }, # Q14 N
                { 'x': 14.5, 'y': 153, 'w': 3, 'h': 3, 'value': customerData['q15yes'] }, # Q15 Y
                { 'x': 22.4, 'y': 153, 'w': 3, 'h': 3, 'value': customerData['q15no'] }, # Q15 N
                { 'x': 14.5, 'y': 153, 'w': 3, 'h': 3, 'value': customerData['q16yes'] }, # Q16 Y
                { 'x': 22.4, 'y': 153, 'w': 3, 'h': 3, 'value': customerData['q16no'] }, # Q16 N
                { 'x': 40, 'y': 153, 'w': 163, 'h': 3, 'value': customerData['q16text'] }, # Q16 text
                { 'x': 14.5, 'y': 153, 'w': 3, 'h': 3, 'value': customerData['q17yes'] }, # Q17 Y
                { 'x': 22.4, 'y': 153, 'w': 3, 'h': 3, 'value': customerData['q17no'] }, # Q17 N

                # affirmation/signature question about housing type (house, apartment, motel, shelter)
                { 'x': 47, 'y': 255, 'w': 3, 'h': 3, 'value': customerData['house'] }, # house
                { 'x': 79, 'y': 255, 'w': 3, 'h': 3, 'value': customerData['apartment'] }, # apartment
                { 'x': 97, 'y': 255, 'w': 3, 'h': 3, 'value': customerData['motel'] }, # motel
                { 'x': 110, 'y': 255, 'w': 3, 'h': 3, 'value': customerData['shelter'] }, # shelter
        ]
    }

    # adds form data to overlay pdf
    for field in range(0, len(form_dictionary['data'])):
        pdf.set_xy(form_dictionary['data'][field]['x'], form_dictionary['data'][field]['y'])
        pdf.cell(form_dictionary['data'][field]['w'], form_dictionary['data'][field]['h'], form_dictionary['data'][field]['value'])

    # ready to overlay to watermark template
    pdf.output('overlay_PDF.pdf')
    pdf.close()


    ### this takes the overlay data and merges it with the watermark template
    ### WORKS
    with open("./forms/DL43en.pdf", 'rb') as pdf_template_file, open(overlay_pdf_file_name, 'rb') as overlay_PDF_file:
        # open watermark template pdf object
        pdf_template = PdfFileReader(pdf_template_file)
        # open overlay data pdf object
        overlay_PDF = PdfFileReader(overlay_PDF_file)

        template_total_pages = pdf_template.getNumPages()
        # iterate through each page to flatten overlay data and watermark template
        for page_number in range(0, template_total_pages):
            # get each page from watermark template
            template_page = pdf_template.getPage(page_number)
            # merge overlay data to watermark template
            template_page.mergePage(overlay_PDF.getPage(page_number))
            # write result to new PDF
            output_pdf = PdfFileWriter()
            output_pdf.addPage(template_page)
        with open(result_pdf_file_name, 'wb') as result_pdf_file:
            output_pdf.write(result_pdf_file)






























# import io
# from fpdf import FPDF
# from pdfrw import PdfReader, PdfWriter, PageMerge


# from PyPDF2.generic import BooleanObject, NameObject, IndirectObject


# blank_pdf_file_name = 'blank_PDF.pdf'






# # test data to fill in form
# acct_vin = 'hello imma test phrase'
# acct_year = str(2000)
# acct_make = str('makeorbreak')







# VIN
# ACCT0
# # pdf.set_xy(ACCT0x, ACCT0y)
# pdf.set_xy(13, 146)
# # pdf.cell(ACCT0w, ACCT0h, ACCT0)
# pdf.cell(94, 5.5, acct_vin)

# # year
# # pdf.set_xy(ACCT1x, ACCT1y)
# pdf.set_xy(108, 146)
# # pdf.cell(ACCT1w, ACCT1h, ACCT1)
# pdf.cell(23, 5.5, acct_year)

# # make
# pdf.set_xy(133, 146)
# pdf.cell(22, 5.5, acct_make)


''' previous test dictionary
form_dictionary = {
    'Vehicle Identification Number': 'TEST VIN #',
    'Year': 'TEST 1999',
    'Make': 'TES Cake',
    'Body Style': 'TEST Being There',
    'Model': 'TEST Modal',
    'TitleDocument Number if unknown leave blank': 'TEST 111 111',
    'Texas License Plate Number if unknown leave blank': 'TEST 12AS3F',
    'Printed Name of Applicant Owner': 'TEST FIRSTNAME',
    'Date': 'TEST TODAY',
    'Additional Applicant Owner': 'TEST NONE',
    'Date_2': 'TEST TODAY',
    'First Name or Entity Name Middle Name Last Name Suffix if any': 'TEST ENTITY MIDDLE',
    'Mailing Address City State Zip': 'TEST 123 FAKE ST',
    'Email': 'TEST GABBA@HEY.COM',
    'Phone Number': 'TEST 123-123-1234'
}
'''












# ### ITERATING TO CREATE OVERLAY PDF NOT WORKING YET
# incoming_form = {
#     'form': 'ACCT',
#     'ACCT0x': 13,
#     'ACCT0y': 146,
#     'ACCT0w': 94,
#     'ACCT0h': 5.5,
#     'ACCT0': 'testing for iterating',
#     'ACCT1x': 108,
#     'ACCT1y': 146,
#     'ACCT1w': 23,
#     'ACCT1h': 5.5,
#     'ACCT1': '1999',
#     'ACCT2x': 133,
#     'ACCT2y': 146,
#     'ACCT2w': 22,
#     'ACCT2h': 5.5,
#     'ACCT2': 'iterate make',
# }

# # order the form fields topmost to bottom, leftmost to right???
# # ACCT (Application for a Certified Copy of Title) ACCT(form_field)

# # the form data is incoming as a dictionary
# # for field, value in incoming_form: MAYBS NOT WORK
# for field in range(0, len(incoming_form)-1):
#     pdf.set_xy(incoming_form['form'] + str(field) + 'x', incoming_form['form'] + str(field) + 'y')
#     pdf.cell(incoming_form['form'] + str(field) + 'w', incoming_form['form'] + str(field) + 'h', incoming_form['form'] + str(field))

# # ready to overlay to watermark template
# pdf.output('overlay_PDF.pdf')
# pdf.close()












'''
# ### TRYING TO REFACTOR SO THAT ONLY ONE PYTHON LIB IS USED. THOUGH I ADD /NEEDAPPEARANCES FLAG, RESULTS COME UP BLANK, FIELDS NOT FILLED. FIELDS FILLED IN BY DICTIONARY KEY-VALUE PAIRS, MERGED WITH A BLANK PAGE TO FLATTEN
# # set NeedAppearances flag
# def set_need_appearances(PdfFileWriter):
#     catalog = PdfFileWriter._root_object
#     # get the AcroForm tree
#     if '/AcroForm' not in catalog:
#         PdfFileWriter._root_object.update({
#             NameObject('/AcroForm'): IndirectObject(len(PdfFileWriter._objects), 0, PdfFileWriter)
#         })

#     need_appearances = NameObject('/NeedAppearances')
#     PdfFileWriter._root_object['/AcroForm'][need_appearances] = BooleanObject(True)
#     return PdfFileWriter

# with open(pdf_template_file_name, 'rb') as pdf_template_file, open(blank_pdf_file_name, 'rb') as blank_PDF_file:
#     # open blank pdf object
#     blank_PDF = PdfFileReader(blank_PDF_file)

#     # open  watermark template pdf object
#     pdf_template = PdfFileReader(pdf_template_file)

#     if '/AcroForm' in pdf_template.trailer['/Root']:
#         pdf_template.trailer['/Root']['/AcroForm'].update(
#             {NameObject('/NeedAppearances'): BooleanObject(True)}
#         )

#     template_total_pages = pdf_template.getNumPages()
#     # iterate through each page to flatten overlay data and watermark template
#     for page_number in range(0, template_total_pages):
#         # get each page from watermark template
#         template_page = pdf_template.getPage(page_number)

#         # write result to new PDF
#         output_pdf = PdfFileWriter()
#         set_need_appearances(output_pdf)
#         if '/AcroForm' in output_pdf._root_object:
#             output_pdf._root_object['/AcroForm'].update(
#                 {NameObject('/NeedAppearances'): BooleanObject(True)}
#             )
#         output_pdf.updatePageFormFieldValues(template_page, form_dictionary)
#         template_page.mergePage(blank_PDF.getPage(0))

#         output_pdf.addPage(template_page)
#     with open(result_pdf_file_name, 'wb') as result_pdf_file:
#         output_pdf.write(result_pdf_file)
'''
































# # testing compound /with/ statements to allow opened files to close
# # with open(pdf_template_file_name, 'rb') as pdf_template, open(overlay_pdf_file_name, 'rb') as overlay_PDF: # template_file_opened:

# # open your watermark template PDF
# pdf_template = PdfFileReader(open(pdf_template_file_name, 'rb'))
# # open overlay data pdf
# overlay_PDF = PdfFileReader(open(overlay_pdf_file_name, 'rb'))

# template_total_pages = pdf_template.getNumPages()
# # iterate through each page to flatten overlay data and watermark template
# for page_number in range(0, template_total_pages):
#     # get each page from watermark template
#     template_page = pdf_template.getPage(page_number)
#     # merge overlay data to watermark template
#     template_page.mergePage(overlay_PDF.getPage(page_number))
#     # write result to new PDF
#     output_pdf = PdfFileWriter()
#     output_pdf.addPage(template_page)
# output_pdf.write(open(result_pdf_file_name, 'wb'))





















# # get each page from watermark template
# template_page = pdf_template.getPage(0)
# # merge overlay data to watermark template
# template_page.mergePage(overlay_PDF.getPage(0))
# # write result to new PDF
# output_pdf = PdfFileWriter()
# output_pdf.addPage(template_page)
# output_pdf.write(open(result_pdf_file_name, 'wb'))














# applies watermark original form
# argv = sys.argv[1:] # find a way to get watermark original form from method other than passing in CLI arguments
# as of 5-15-18 2:30p usage: python3 fill_form_watermark.py -u textOverSuccess.pdf decryptedVTR431flat.pdf
# as of 5-15-18 2:45p usage: set inpfn and wmarkfn are variable names/filenames to the input and watermark files

# check if watermark underneath flag is necessary
# underneath = '-u' # in argv
# if underneath:
#     del argv[argv.index('-u')]
# inpfn, wmarkfn = argv

# get first page of template
# inpfn = 'textOverSuccess.pdf'
# wmarkfn = 'decryptedVTR341flat.pdf'

# outfn = 'watermark.' + os.path.basename(inpfn) # -u flag puts watermark underneath

# wmark = PageMerge().add(PdfReader(wmarkfn).pages[0])[0]
# trailer = PdfReader(inpfn)
# for page in trailer.pages:
#     PageMerge(page).add(wmark, prepend=underneath).render()
# PdfWriter(outfn, trailer=trailer).write()

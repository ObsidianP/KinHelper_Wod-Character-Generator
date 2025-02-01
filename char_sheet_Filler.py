import os
from datetime import datetime 
from fillpdf import fillpdfs
        
def get_pdf(): 
    #if os.path.exists('w5_character_sheets_v2.pdf'):
    fillpdfs.print_form_fields("w5_character_sheets_v2.pdf",sort=False)
    os.path.dirname
        #Make a copy of formfillable pdf to make sure we keep original format
    #timestamp = repr(datetime.strftime(datetime.now(),"%d-%m-%Y_%H-%M"))
    #char_name.genName to be created with another script
    #pdf_name = 'w5_core_'+'_'+char_name+'_'+'_character_sheet_'+timestamp
    #Character_stats -class should be called to generate character and fill sheet
    # #pdf_namefill
get_pdf()

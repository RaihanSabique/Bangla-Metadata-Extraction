# -*- coding: utf-8 -*-
#happy_coding('~')
import json
import dataExtraction.filereader.docreader as docreader
import dataExtraction.filereader.readpdf as readpdf
import dataExtraction.getmetadata.mergedata as mergedata
import dataExtraction.tracking.trackingprojectid as tracking
from pprint import pprint

import os

#print('Here:'+font.__str__('cjøx Dbœqb I mgevq gš¿Yvjq/¯’vbxq miKvi wefvM'))

from flask import Flask, jsonify, request, flash, render_template
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

ROOT_DIR = os.path.abspath("../../")


TTFSearchPath = (
            'c:/winnt/fonts',
            'c:/windows/fonts',
            '/usr/lib/X11/fonts/TrueType/',
            '/usr/share/fonts/truetype',
            '/usr/share/fonts',             #Linux, Fedora
            '/usr/share/fonts/dejav',      #Linux, Fedora
            '%(REPORTLAB_DIR)s/fonts',      #special
            '%(REPORTLAB_DIR)s/../fonts',   #special
            '%(REPORTLAB_DIR)s/../../fonts',#special
            '%(CWD)s/fonts',                #special
            '~/fonts',
            '~/.fonts',
            '%(XDG_DATA_HOME)s/fonts',
            '~/.local/share/fonts',
            #mac os X - from
            #http://developer.apple.com/technotes/tn/tn2024.html
            '~/Library/Fonts',
            '/Library/Fonts',
            '/Network/Library/Fonts',
            '/System/Library/Fonts',
            )

pdf_file_name = 'dataExtraction/dppFile/pdf/dpp1.pdf'

# For debugging
# Begin
#pdftotext.extract(pdf_file_name)
#text=pdfreader.extract_pdf(pdf_file_name)
#text=pyreader.convert_pdf_to_html(pdf_file_name)
#text=readpdf.pdf_to_text(pdf_file_name)
#print(text)


#meetingMinute
#data_list,raw_data,converted_data=docreader.doc_reader_tree_formate('dataExtraction/dppFile/meetingminute/mm2.docx')
#pprint(raw_data)
#mergedata.get_merge_meetingminute(raw_data,converted_data)


#~ data_list="xy!› öœ"
#data_list,raw_data,converted_data=docreader.doc_reader_tree_formate('dataExtraction/dppFile/doc/newdpp2.docx')
#test_data_list,test_raw_data,test_converted_data=docreader.doc_reader_tree_formate('dataExtraction/dppFile/doc/newdpp2.docx')

#mergedata.get_merge_dpp_1(data_list, converted_data,test_converted_data)
#finalresult = json.loads(dpp_result)
#print(finalresult)
#raw_data=docreader.get_docx_text('dataExtraction/dppFile/dppsummary/Summary01.docx')
#print(data_list)
#pprint(converted_data)
#result=mergedata.get_summary_merge_data(raw_data,converted_data)
#print(result)
#print(raw_data[0])
#docreader.print_doc('dataExtraction/dppFile/dppsummary/Summary01.docx')

# End
data_list,raw_data,converted_data =docreader.doc_reader_tree_formate('dataExtraction/dppFile/doc/dpp4.docx')
#pprint(raw_data)
dpp_result=mergedata.clustering_and_get_merge_dpp(raw_data, converted_data,'12345')
#pprint(dpp_result)
finalresult = json.loads(dpp_result)
#print(finalresult)

#@app.route('/<string:folder_name>/<string:dpp_name>', methods=['POST','GET'])
@app.route('/',methods=['POST'])
def start():
    Test=request.form['test']
    print(Test)

@app.route('/data_extraction',methods=['POST'])
def extraction():
    try:
        data=request.get_json(force=True)
        project_name = data['project_name']
        project_id = data['project_id']
        folder_name = data['folder_name']
        file_name = data['file_name']
        print(project_name)
        p_id = tracking.get_project_id(project_name)
        print(p_id)
        if str(p_id) == str(project_id):
            print('id matched', project_id)
            return get_tasks(folder_name, file_name, str(project_id))
        elif str(p_id) == "" or p_id == None:
            tracking.set_project_id(str(project_id), project_name)
            return get_tasks(folder_name, file_name, str(project_id))
    except Exception as e:
        return '<p>error<p>'

def get_tasks(folder_name,file_name,project_id):

    #object_list = getTableData('dppFile/doc/'+dpp_name)
    #print(object_list)
    data_list,raw_data,converted_data =docreader.doc_reader_tree_formate('dataExtraction/dppFile/'+ folder_name +'/'+ file_name)
    #pprint(raw_data)
    if(folder_name=='dpp'):
        dpp_result=mergedata.clustering_and_get_merge_dpp(raw_data, converted_data,project_id)
        finalresult = json.loads(dpp_result)
    if(folder_name=='summary'):
        summary_result=mergedata.get_merge_summary(raw_data, converted_data,project_id)
        finalresult = json.loads(summary_result)
    if (folder_name == 'meetingminute'):
        meetingminute_result = mergedata.get_merge_meetingminute(raw_data, converted_data,project_id)
        finalresult = json.loads(meetingminute_result)
    return jsonify(finalresult)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5555')





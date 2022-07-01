from flask import Flask, render_template, request, send_file
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os

import backEnd
import constants
import mcd
import dominos
import burger_king
import pizza_hut
import kfc



app = Flask(__name__)
app.config['SECRET_KEY'] = 'badminton'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Upload File")

@app.route('/new', methods = ['GET', 'POST'])

@app.route('/', methods = ['GET', 'POST'])
def home():
    form = UploadFileForm()
    title = "ExParse"
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        return render_template('subscribe.html')
    return render_template('home.html', title = title, form = form)


@app.route('/about')
def about():
    return render_template("about.html")

#THIS IS CHANGED
@app.route('/subscribe')
def subscribe():
    title = "ExParse"
    return render_template("subscribe.html")

company = ""
sheetname = ""
column_to_extract = ""
column_to_input = ""

runner = ""
@app.route('/results', methods = ["POST"])

def results():
    global runner
    print(request.form.get('filename'))
    print(convert_filepath(request.form.get("filename")))
    company = request.form.get("company")
    runner = backend_object(company)
    print (runner)
    runner.extract_from_excel()
    #Notifies the user that the program is running.
    #This extracts all prices and items from a webiste.
    runner.extract_all_prices()
    #put message box asking whether or not to put data into this column
    #Puts the data into an excel sheet.
    runner.put_in_excel()
    #Checks if there are any new items
    new = runner.check_if_new()
    if new:
        runner.handle_new_items()
    title = "Results"
    return render_template("upload_excel.html")

@app.route('/download')
def download():
    global runner
    #print(convert_filepath(request.form.get("filename")))
    return send_file(runner.filePath, as_attachment= True)

def backend_object(company):
    if company == "McDonalds":
        return mcd.mcdonald(convert_filepath(request.form.get("filename")), request.form.get("sheet_name"), constants.mcdonalds, request.form.get("extraction"), request.form.get("insertion"))
    if company == "KFC":
        return kfc.kfc_class(convert_filepath(request.form.get("filename")), request.form.get("sheet_name"), constants.mcdonalds, request.form.get("extraction"), request.form.get("insertion"))
        #return kfc.kfc(self.filepath, self.sheetname, self.websites, self.column)
    if company == "Burger King":
        return burger_king.burger_king(convert_filepath(request.form.get("filename")), request.form.get("sheet_name"), constants.mcdonalds, request.form.get("extraction"), request.form.get("insertion"))
    if company == "Pizza Hut":
        return pizza_hut.pizza_hut(convert_filepath(request.form.get("filename")), request.form.get("sheet_name"), constants.mcdonalds, request.form.get("extraction"), request.form.get("insertion"))
    if company == "Dominos":
        return dominos.dominos(convert_filepath(request.form.get("filename")), request.form.get("sheet_name"), constants.mcdonalds, request.form.get("extraction"), request.form.get("insertion"))

def convert_filepath(file_name):
    return ("/Users/adyab/IdeaProjects/exparse-hdfc/static/files/"+file_name)

if __name__ == "__main__":
    app.run(debug=True)
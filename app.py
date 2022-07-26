from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename

app=Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    global file
    if request.method=='POST':
        file=request.files["file"]
        file.save(secure_filename("uploaded"+file.filename))
        with open("uploaded"+file.filename,"a") as f:
            f.write("This was added later!")
        print(file)
        print(type(file))
        return render_template("index.html", btn="download.html")

@app.route("/download")
def download():
    return send_file("uploaded"+file.filename, attachment_filename="yourfile.csv", as_attachment=True)


if __name__ == "__main__":
    app.debug=True
    app.run()
from flask import Flask, request, render_template
from Steganography import Steganography
from PIL import Image

app = Flask(__name__, template_folder="templates")

maxFileSize = 10485760

defaultImagePath = 'pictures\\'

app.config['MAX_CONTENT_PATH'] = maxFileSize

@app.route("/", methods = ["POST", "GET"])
def home():
    return render_template("homepage.html")

@app.route("/merge", methods = ['GET','POST'])
def mergeImages():
    img1 = request.files['img1']
    img2 = request.files['img2']
    
    img1_name = defaultImagePath + 'image1.png'
    img2_name = defaultImagePath + 'image2.png'
    
    img1.save(img1_name)
    img2.save(img2_name)
    outputImageName = defaultImagePath + 'merged.png'
    
    merge(img1_name, img2_name, outputImageName)
    im = Image.open(outputImageName)
    im.show()
    return render_template("merge.html")

@app.route("/unmerge", methods = ['GET','POST'])
def unmergeImages():
    img = request.files['img']

    img_name = defaultImagePath + 'toUnmerge.png'

    img.save(img_name)

    outputImageName = defaultImagePath + 'unmerged.png'

    unmerge(img_name, outputImageName)
    im = Image.open(outputImageName)
    im.show()
    return render_template("unmerge.html")

def merge(img1, img2, output):
    merged_image = Steganography.merge(Image.open(img1), Image.open(img2))
    merged_image.save(output)

def unmerge(img, output):
    unmerged_image = Steganography.unmerge(Image.open(img))
    unmerged_image.save(output)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/team")
def team():
    return render_template("team.html")

if __name__ == "__main__":
    app.run()

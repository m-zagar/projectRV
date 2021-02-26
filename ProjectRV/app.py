from flask import Flask, render_template, request, url_for
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
import base64
import io

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
	return render_template('index.html')

@app.route("/plot/", methods=['POST'])
def plot():
	
    # plot funcion values !DISABLED!
    a0 = int(request.form['a0'])
    a1 = int(request.form['a1'])
    a2 = int(request.form['a2'])
    a3 = int(request.form['a3'])
    V = int(request.form['V'])
    w1 = int(request.form['w1'])
    w2 = int(request.form['w2'])

    # ploting
    fig, ax = plt.subplots(figsize=(25,16))
    (markerline, stemlines, baseline) = plt.stem([w2-w1, (2*w1)-w2, w1, w2, (2*w2)-w1, (2*w1), w1+w2, (2*w2), (3*w1), (2*w1)+w2, (2*w2)+w1, (3*w2)], [pow(V, 2) * a2, (3/4) * pow(V, 3) * a3, ((1/4) * V)*(4 * a1 + 9 * a3 * pow(V,2)), ((1/4) * V) * (4 * a1 + 9 * a3 * pow(V,2)), (3/4) * pow(V, 3) * a3, (1/2) * pow(V, 2) * a2, pow(V, 2) * a2, (1/2) * pow(V, 2) * a2, (1/4)*pow(V, 3) * a3, (3/4)*pow(V, 3) * a3, (3/4)*pow(V, 3) * a3, (1/4)*pow(V, 3) * a3])
    plt.setp(stemlines, linestyle="-", color="black", linewidth=1.5)
    plt.setp(markerline, marker='^', markersize=5, markeredgecolor="black", markeredgewidth=2)
    plt.setp(baseline, visible=False)
    ax.set_ylim(bottom=0)
    ax.set_ylabel('A', rotation=0, fontsize=30, labelpad=30);
    plt.yticks(fontsize=25)

    # setting x-labels
    x = [w2-w1, (2*w1)-w2, w1, w2, (2*w2)-w1, (2*w1), w1+w2, (2*w2), (3*w1), (2*w1)+w2, (2*w2)+w1, (3*w2)]
    labels = ['\u03C9\u2082-\u03C9\u2081', '2\u03C9\u2081-\u03C9\u2082', '\u03C9\u2081', '\u03C9\u2082', '2\u03C9\u2082-\u03C9\u2081', '2\u03C9\u2081', '\u03C9\u2081+\u03C9\u2082', '2\u03C9\u2082', '3\u03C9\u2081', '2\u03C9\u2081+\u03C9\u2082', '2\u03C9\u2082+\u03C9\u2081', '3\u03C9\u2082']
    plt.xticks(x, labels, rotation='65', fontsize=30)

    # remove top and right borders
    right_side = ax.spines["right"]
    top_side = ax.spines["top"]
    right_side.set_visible(False)
    top_side.set_visible(False)

    # convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    
    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    wlabels = ("\u03C9\u2082-\u03C9\u2081", '2\u03C9\u2081-\u03C9\u2082', '\u03C9\u2081', '\u03C9\u2082', '2\u03C9\u2082-\u03C9\u2081', '2\u03C9\u2081', '\u03C9\u2081+\u03C9\u2082', '2\u03C9\u2082', '3\u03C9\u2081', '2\u03C9\u2081+\u03C9\u2082', '2\u03C9\u2082+\u03C9\u2081', '3\u03C9\u2082')
    wvalues = (w2-w1, (2*w1)-w2, w1, w2, (2*w2)-w1, (2*w1), w1+w2, (2*w2), (3*w1), (2*w1)+w2, (2*w2)+w1, (3*w2))
    avalues = ('A', pow(V, 2) * a2, (3/4) * pow(V, 3) * a3, ((1/4) * V)*(4 * a1 + 9 * a3 * pow(V,2)), ((1/4) * V) * (4 * a1 + 9 * a3 * pow(V,2)), (3/4) * pow(V, 3) * a3, (1/2) * pow(V, 2) * a2, pow(V, 2) * a2, (1/2) * pow(V, 2) * a2, (1/4)*pow(V, 3) * a3, (3/4)*pow(V, 3) * a3, (3/4)*pow(V, 3) * a3, (1/4)*pow(V, 3) * a3)

    return render_template("index.html", image=pngImageB64String, wlabels=wlabels, wvalues=wvalues, avalues=avalues, valuew1=w1, valuew2=w2)

@app.route("/equation/")
def equation():
    return render_template('equation.html')

if __name__ == "__main__":
	app.run()
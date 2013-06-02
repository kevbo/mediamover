# point to this file in /etc/rc.local. with the env
import os
import shutil
from collections import OrderedDict

import yaml
from flask import Flask
from flask import request, redirect, url_for, render_template


app = Flask(__name__)

with open('media.yaml') as f:
    DATA = yaml.load(f)

DOWNLOADS = DATA['source_dir']
TARGETS = OrderedDict(sorted(DATA['targets'].items(), key=lambda t: t[0]))


@app.route("/")
def index():
    things = os.listdir(DOWNLOADS)
    things = [ thing for thing in things if not thing.startswith('.')]
    return render_template('index.html', things=things)

@app.route("/move/")
def move():
    source = request.args.get('source', None)
    target = request.args.get('target', None)
    print source
    print target
    if all((source, target)):
        shutil.move("{0}{1}".format(DOWNLOADS, source), TARGETS[target])
        return render_template('success.html', source=source, target=target)
    if source and not target:
        return render_template('move.html', targets=TARGETS, source=source)
    if not source and not target:
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
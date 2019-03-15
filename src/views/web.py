#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from flask import request, render_template, flash
from ..forms import ContactForm
from src import app
from src import mail, Message
from src.util.utility import download_file
from threading import Thread


@app.route("/about")
def about():
    return render_template('about.html')    


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
     
    if request.method == 'POST':
        if form.validate() == False:
            flash('Alle feltene må fylles ut.')
            return render_template('contact.html', form=form)
        else:
            msg = Message(form.subject.data, sender='contact@example.com', recipients=['magnus.oye@gmail.com'])
            msg.body = """
            Fra: %s, %s;
            
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return render_template('contact.html', success=True)
 
    elif request.method == 'GET':
        return render_template('contact.html', form=form)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        text = request.form['text']
        if text.startswith('magnet'):
            thread = Thread(target = download_file(text), args = (10, ))
            thread.start()
            thread.join()
            return render_template('uploaded_file.html')
        else:
            return """Dette er ikke en magnetlink"""
    return render_template('index.html')
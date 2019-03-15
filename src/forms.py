#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src import app
from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, validators
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    name = TextField("Name",  [validators.Required("Vennligst skriv inn ditt navn.")])
    email = TextField("Email",  [validators.Required("Vennligst skriv inn email."), validators.Email("Vennligst skriv inn email.")])
    subject = TextField("Subject",  [validators.Required("Vennligst skriv inn emne.")])
    message = TextAreaField("Message",  [validators.Required("Vennligst skriv inn din melding.")])
    submit = SubmitField("Send")
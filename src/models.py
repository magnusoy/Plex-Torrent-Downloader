#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src import app
from . import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, path):
        self.path = path


class Series(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, path):
        self.path = path

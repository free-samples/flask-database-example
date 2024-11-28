import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:mysecretpassword@db:5432/mydatabase'  # Or your database URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
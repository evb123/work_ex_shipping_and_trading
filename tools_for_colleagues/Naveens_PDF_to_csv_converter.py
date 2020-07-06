#!/usr/bin/env python
# coding: utf-8

# # Naveen's PDF Converter
# 
# The purpose of the notebook is to convert PDFs of tables into csv files.


import tabula

# change pdf_path and name of csv output file
pdf_path = r"C:<path>"
name_csv = "Naveen.csv"

tabula.convert_into(
                pdf_path
                , name_csv
                ## can change folling options, turn on/off with '#'
                ,pages = 'all'
                #, spreadsheet = True
                # lattice = True
                #, area=(500, 22, 695, 589)
                , multiple_tables = True
                #, guess = False
                , stream = True
                ,output_format="csv"
               )
## Can also use read_pdf() to create python object
#tabula.read_pdf()


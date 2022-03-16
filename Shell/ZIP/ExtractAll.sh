#!/bin/bash
#unzips all zip files in folder using unar
for FILE in *; do unar -d $FILE; done
# translation file is at https://raw.githubusercontent.com/apertium/apertium-fra-eng/master/apertium-fra-eng.fra-eng.dix
lt-expand apertium-fra-eng.fra-eng.dix | rg vblex | sed 's/:>//g' | sed 's/<vblex>//g' | sed 's/<sep>//g' | sed 's/:/,/g' | sed 's/#//g' | sort -u > fr-en.csv
# add etre (it is special cased in the dataset)
echo 'être,be' >> fr-en.csv

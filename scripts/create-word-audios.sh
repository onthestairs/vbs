# download audio files from https://web.archive.org/web/20140626053312/http://download.shtooka.net/fra-balm-voc_flac.tar

inputdir="./data/oral/shtooka/flac"
tmpfile="/tmp/french-words.txt"
usedwords="/tmp/french-used-words.txt"
setsfile="./data/oral/sets.json"
outputdir="./public/oral/audio"
outputsetsfile="./src/data/oral/sets.json"

cp $setsfile $outputsetsfile

yq -p='xml' -o=json '.' "$inputdir/index.xml" | jq -c '[.index.group.file[] | {path: ."+@path", text: .tag."+@swac_text"}] | .[]' >$tmpfile
jq -r 'flatten | .[]' $setsfile >$usedwords

while read -r line; do
  filename=$(echo $line | jq -r '.path')
  text=$(echo $line | jq -r '.text')
  infile="$inputdir"/"$filename"
  outfile="$outputdir"/"$text".mp3
  if grep -q "^$text$" "$usedwords"; then
    if ! test -f $outfile; then
      echo "Doing '$text.'. In: $infile, Out: $outfile"
      ffmpeg -i "$infile" -ab 320k -map_metadata 0 -id3v2_version 3 "$outfile"
    else 
	echo "Skipping '$text'. mp3 already exists"
    fi

  else
    echo "Skipping '$text'"
    continue
  fi
done <"$tmpfile"

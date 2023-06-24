import json
import os
import shutil
import subprocess

INPUT_DIR = "./data/oral/shtooka/flac"
SETS_FILE = "./data/oral/sets.json"
OUTPUT_DIR = "./public/oral/audio"
OUTPUT_SETS_FILE = "./src/data/oral/sets.json"

shutil.copy(SETS_FILE, OUTPUT_SETS_FILE)

# Read index.xml using yq and convert it to JSON using jq
index_xml_path = os.path.join(INPUT_DIR, "index.xml")
index_json = subprocess.check_output(
    ["yq", "-p", "xml", "-o", "json", ".", index_xml_path]
).decode("utf-8")
index_data = json.loads(index_json)
file_list = index_data["index"]["group"]["file"]
# print(file_list)

files = [
    {"path": file["+@path"], "text": file["tag"]["+@swac_text"]} for file in file_list
]

with open(SETS_FILE, "r") as f:
    sets = json.loads(f.read())
    used_words = set([word for word_set in sets for word in word_set])

for file in files:
    filename = file["path"]
    text = file["text"]
    infile = os.path.join(INPUT_DIR, filename)
    outfile = os.path.join(OUTPUT_DIR, f"{text}.mp3")

    if text in used_words:
        if not os.path.exists(outfile):
            print(f"Doing '{text}'. In: {infile}, Out: {outfile}")
            subprocess.run(
                [
                    "ffmpeg",
                    "-i",
                    infile,
                    "-ab",
                    "320k",
                    "-map_metadata",
                    "0",
                    "-id3v2_version",
                    "3",
                    outfile,
                ]
            )
        else:
            print(f"Skipping '{text}'. mp3 already exists")
    else:
        print(f"Skipping '{text}'")

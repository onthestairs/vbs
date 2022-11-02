import csv
import json

verbs = []

with open("./french-verb-conjugation.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        verb = {
            "infinitive": row["infinitive"],
            "indicative": {
                "present": {
                    "first_person_singular": row[
                        "indicative|present|first person singular"
                    ],
                    "second_person_singular": row[
                        "indicative|present|second person singular"
                    ],
                    "third_person_singular": row[
                        "indicative|present|third person singular"
                    ],
                    "first_person_plural": row[
                        "indicative|present|first person plural"
                    ],
                    "second_person_plural": row[
                        "indicative|present|second person plural"
                    ],
                    "third_person_plural": row[
                        "indicative|present|third person plural"
                    ],
                }
            },
        }
        verbs.append(verb)

with open("verbs.json", "w") as f:
    f.write(json.dumps(verbs))

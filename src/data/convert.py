import csv
import json

verbs = []

with open("./french-verb-conjugation.csv") as f:
    reader = csv.DictReader(f)
    seen_infinitives = set()
    for row in reader:
        infinitive = row["infinitive"]
        if infinitive in seen_infinitives:
            print(f"Skipping {infinitive}, Already seen")
            continue
        seen_infinitives.add(infinitive)
        verb = {
            "infinitive": infinitive,
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

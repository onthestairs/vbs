import csv
import json
from collections import defaultdict

translations = defaultdict(list)

with open("./fr-en.csv") as f:
    reader = csv.reader(f)
    for french, english in reader:
        translations[french].append(english)


verbs = []

with open("./french-verb-conjugation.csv") as f:
    reader = csv.DictReader(f)
    seen_infinitives = set()
    for row in reader:
        infinitive = row["infinitive"]
        english = translations.get(infinitive)
        if not english:
            print(f"No translation for {infinitive}")
            continue
        if infinitive in seen_infinitives:
            print(f"Skipping {infinitive}, Already seen")
            continue
        seen_infinitives.add(infinitive)
        verb = {
            "english": english,
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
                },
                "imperfect": {
                    "first_person_singular": row[
                        "indicative|imperfect|first person singular"
                    ],
                    "second_person_singular": row[
                        "indicative|imperfect|second person singular"
                    ],
                    "third_person_singular": row[
                        "indicative|imperfect|third person singular"
                    ],
                    "first_person_plural": row[
                        "indicative|imperfect|first person plural"
                    ],
                    "second_person_plural": row[
                        "indicative|imperfect|second person plural"
                    ],
                    "third_person_plural": row[
                        "indicative|imperfect|third person plural"
                    ],
                },
                "future": {
                    "first_person_singular": row[
                        "indicative|future|first person singular"
                    ],
                    "second_person_singular": row[
                        "indicative|future|second person singular"
                    ],
                    "third_person_singular": row[
                        "indicative|future|third person singular"
                    ],
                    "first_person_plural": row["indicative|future|first person plural"],
                    "second_person_plural": row[
                        "indicative|future|second person plural"
                    ],
                    "third_person_plural": row["indicative|future|third person plural"],
                },
            },
            "subjunctive": {
                "present": {
                    "first_person_singular": row[
                        "subjunctive|present|first person singular"
                    ],
                    "second_person_singular": row[
                        "subjunctive|present|second person singular"
                    ],
                    "third_person_singular": row[
                        "subjunctive|present|third person singular"
                    ],
                    "first_person_plural": row[
                        "subjunctive|present|first person plural"
                    ],
                    "second_person_plural": row[
                        "subjunctive|present|second person plural"
                    ],
                    "third_person_plural": row[
                        "subjunctive|present|third person plural"
                    ],
                },
                "imperfect": {
                    "first_person_singular": row[
                        "subjunctive|imperfect|first person singular"
                    ],
                    "second_person_singular": row[
                        "subjunctive|imperfect|second person singular"
                    ],
                    "third_person_singular": row[
                        "subjunctive|imperfect|third person singular"
                    ],
                    "first_person_plural": row[
                        "subjunctive|imperfect|first person plural"
                    ],
                    "second_person_plural": row[
                        "subjunctive|imperfect|second person plural"
                    ],
                    "third_person_plural": row[
                        "subjunctive|imperfect|third person plural"
                    ],
                },
            },
        }
        verbs.append(verb)

with open("verbs.json", "w") as f:
    f.write(json.dumps(verbs))

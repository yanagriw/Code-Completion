import os
import pandas as pd

num_examples = 50

results_folder = 'results'
splitted_examples_folder = 'splitted_examples'

comparison_data = []

for i in range(1, num_examples + 1):
    candidate_filename = f'example{i}.txt'
    reference_filename = f'{i}_annot.txt'

    candidate_filepath = os.path.join(results_folder, candidate_filename)
    reference_filepath = os.path.join(splitted_examples_folder, reference_filename)

    with open(candidate_filepath, 'r', encoding='utf-8') as f:
        candidate_text = f.read().strip()

    with open(reference_filepath, 'r', encoding='utf-8') as f:
        reference_text = f.read().strip()

    comparison_data.append({
        'Example': i,
        'Candidate Text': candidate_text,
        'Reference Text': reference_text,
    })

df = pd.DataFrame(comparison_data)

output_filename = 'comparison_table.csv'
df.to_csv(output_filename, index=False, encoding='utf-8')
import sacrebleu
import nltk
import os

def compute_exact_match(generated_codes, reference_codes):
    total_samples = len(generated_codes)
    exact_matches = 0

    for gen_code, ref_code in zip(generated_codes, reference_codes):
        gen_code_normalized = gen_code.strip()
        ref_code_normalized = ref_code[0].strip()

        if gen_code_normalized == ref_code_normalized:
            exact_matches += 1

    exact_match_percentage = (exact_matches / total_samples) * 100
    return exact_match_percentage

def compute_chrF(generated_texts, reference_texts, beta=2):
    chrf = sacrebleu.corpus_chrf(generated_texts, reference_texts, beta=beta)
    return chrf.score

def compute_chrF_pp(generated_texts, reference_texts, beta=2):
    chrf = sacrebleu.corpus_chrf(generated_texts, reference_texts, beta=beta, word_order=2)
    return chrf.score

def compute_bleu(candidate_texts, reference_texts):
    bleu = sacrebleu.corpus_bleu(candidate_texts, reference_texts)
    return bleu.score


def compute_edit_distance(candidate_texts, reference_texts):
    total_distance = 0
    num_examples = len(candidate_texts)

    for i in range(num_examples):
        candidate = candidate_texts[i]
        reference = reference_texts[i]
        distance = nltk.edit_distance(candidate, reference)
        total_distance += distance

    average_distance = total_distance / num_examples
    return average_distance

def read_data(num_examples=50):
    candidate_texts_folder = 'results'
    reference_texts_folder = 'splitted_examples'
    candidate_texts = []
    reference_texts = []
    for i in range(1, num_examples + 1):
        filename_candidate = f'example{i}.txt'
        filepath = os.path.join(candidate_texts_folder, filename_candidate)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            candidate_texts.append(content)

        filename_reference = f'{i}_annot.txt'
        filepath = os.path.join(reference_texts_folder, filename_reference)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            # Wrap the content in a list, as the metrics expect a list of references per candidate
            reference_texts.append([content])
    return candidate_texts, reference_texts

def main():
    candidate_texts, reference_texts = read_data()

    exact_match = compute_exact_match(candidate_texts, reference_texts)
    print(f"Exact Match Score: {exact_match:.2f}")

    bleu_score = compute_bleu(candidate_texts, reference_texts)
    print(f"BLEU Score: {bleu_score:.2f}")

    avg_chrF = compute_chrF(candidate_texts, reference_texts)
    print(f"chrF Score: {avg_chrF:.2f}")

    chrF_pp = compute_chrF_pp(candidate_texts, reference_texts)
    print(f"chrF++ Score: {chrF_pp:.2f}")

    edit_distance = compute_edit_distance(candidate_texts, reference_texts)
    print(f"Edit Distance: {edit_distance:.2f}")

if __name__ == "__main__":
    main()
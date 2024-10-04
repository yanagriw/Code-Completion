from transformers import AutoModelForCausalLM, AutoTokenizer

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def strip_result(decoded_text):
    # Find the position of the "<fim_middle>" flag
    fim_middle_pos = decoded_text.find('<fim_middle>')

    # Find the first newline character after the "<fim_middle>" flag
    newline_pos = decoded_text.find('\n', fim_middle_pos)

    return decoded_text[fim_middle_pos + len('<fim_middle>'):newline_pos].strip()

def main():
    checkpoint = "bigcode/tiny_starcoder_py"
    device = "cpu"

    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)

    # Get the token IDs for the new line character(s)
    newline_token_id = tokenizer.encode('\n', add_special_tokens=False)[0]

    for i in range(1, 51):
        input_text = read_input_file(f'splitted_examples/{i}.txt')
        inputs = tokenizer.encode(input_text, return_tensors="pt").to(device)
        max_length = len(inputs[0]) + 20

        outputs = model.generate(inputs, max_length=max_length, eos_token_id=newline_token_id)
        decoded_text = tokenizer.decode(outputs[0])

        with open(f"results/example{i}.txt", 'w') as output_file:
            output_file.write(strip_result(decoded_text))

if __name__ == "__main__":
    main()
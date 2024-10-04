To complete this task, I created 4 Python scripts:

### split.py

This script divides text files into three parts: **prefix**, **middle**, and **suffix**. 

Using the `--file_path` argument, you can specify the name of the input file for splitting. 

The `--output_path` argument designates the name of the file where the result will be saved. The prefix and suffix are stored in files named `splitted_examples/{i}.txt` in a format compatible with the StarCoder model. The middle parts are saved in files named `splitted_examples/{i}_annot.txt`. 

The `--cursor_pos` argument indicates the end of the prefix part and the beginning of the middle part that needs to be predicted. It is assumed that the middle part continues until the start of a new line.

### model.py

For this task, I utilized the `tiny_starcoder` model. By specifying the `eos_token_id` argument, I ensured that code generation stops after a `\n` character is generated. However, in some cases, the generated output may include the beginning of the suffix part. To resolve this issue, I created a function `strip_result()` that retains only the correctly generated portion. The final result is saved in a file named `results/example{i}.txt`.

### metrics.py

This script performs an evaluation of the obtained results and outputs them to the standard output. I employed metrics such as **Exact Match**, **chrF**, **chrF++**, **BLEU**, and **Edit Distance**. The results are as follows:

* Exact Match Score: 4.00
* BLEU Score: 45.47
* chrF Score: 59.98
* chrF++ Score: 54.15
* Edit Distance: 27.56
  
Because the chrF score compares text at the character level, it can recognize similarities between the generated code and the reference code even when there are minor differences like variable names or formatting. This makes it a better fit for evaluating code generation tasks, as it more accurately reflects how close the generated code is to the intended functionality.

### compare.py

I developed this script to record the actual missing examples and the generated code in CSV format for more convenient manual comparison.


### My Considerations

For this assignment, I used five of my own Python scripts, which were divided into 50 examples. I manually selected the splitting position for each example to evaluate the model's performance on both simple template tasks and more complex formulas and algorithms.

The metrics I utilized indicated average performance. Despite the Exact Match score being only 4%, my own annotations showed success in 34% of cases (these annotations are recorded in the file `comparison_table.csv`). I considered a result successful if the generated code would produce the same program output in most tests and would not lead to errors. As anticipated, the model performs well in simple, template-like scenarios (e.g., reading text from a file, completing function parameters, adding frequently repeated code segments, and so on). However, the generated code often contained incorrect variable names or correct code with minor mistakes that could cause compilation errors. Additionally, the model was unable to complete well-known formulas (such as entropy) and straightforward parts of algorithms. Overall, the model provides useful suggestions that can be slightly refined to achieve the correct result.

##Arithmetic Formatter##

"""
It is a function that receives a list of strings that are arithmetic 
problems and returns the problems arranged vertically and side-by-side. 
The function optionally take a second argument. When the second 
argument is set to True, the answers should be displayed.
https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter
"""

def arithmetic_arranger(problems, display_result=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    split_problems = [problem.split() for problem in problems] 
    results = [eval(problem) for problem in problems]

    for sp in split_problems:
        operand1, operator, operand2 = sp
        if operator != '+' and sp[1] != '-':
            return "Error: Operator must be '+' or '-'."
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        result = str(results[split_problems.index(sp)])
        max_length = max(len(operand1), len(operand2))
        arranged_problems += f"{operand1.rjust(max_length + 2)}\n{operator} {operand2.rjust(max_length)}\n{'-'*(max_length + 2)}\n{result.rjust(max_length + 2)}\n"
    
    arranged_problems = arranged_problems.split("\n")
    

    opp1_line = "    ".join(arranged_problems[0::4])
    op_opp2_line = "    ".join(arranged_problems[1::4])
    dash_line = "    ".join(arranged_problems[2::4])
    result_line = "    ".join(arranged_problems[3::4])

    if display_result:
        arranged_problems = f"{opp1_line}\n{op_opp2_line}\n{dash_line}\n{result_line}"
    else:
        arranged_problems = f"{opp1_line}\n{op_opp2_line}\n{dash_line}"
    return arranged_problems

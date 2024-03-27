"""
Shell code cooker command line module.
"""

import sys

def shell_code_formatter(machine_code):
	"""
	Function that formats plain machine code into executable instructions.	
	:param str machine_code: String to be formatted as executable set of instructions.
	:return: str
	"""
	return "\\x" + "\\x".join([machine_code[i:i + 2] for i in range(0, len(machine_code), 2)])


def write_file(content):
	"""
	Utilitarian procedure to write a file into disk.	
	:param str or bytes content: Content to be written into file.
	:return: None
	"""
	with open("shellcode.txt", "w") as writer:
		writer.write(content)


if __name__ == "__main__":
	if len(sys.argv) < 2:
		raise Exception("Missing machine code argument.") 
	write_file(shell_code_formatter(sys.argv[1]))



import os, sys
def change_format(arg):
	from nbformat import v3, v4
	with open(arg) as fpin:
		text = fpin.read()

	nbook = v3.reads_py(text)
	nbook = v4.upgrade(nbook)
	jsonform = v4.writes(nbook) + "\n"
	new_file = arg + ".ipynb"
	with open(new_file, "w") as fpout:
		fpout.write(jsonform)

def main():
	arg = sys.argv[1]
	change_format(arg)
	os.remove(arg)

if __name__ == '__main__':
	main()
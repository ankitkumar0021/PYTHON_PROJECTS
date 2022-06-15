import pywhatkit as pw

txt="""PyWhatKit is a Python library with various helpful features. It's easy-to-use and does not require you to do any additional setup. Currently, it has about 300k+ downloads and counting. New updates are released frequently with new features and bug fixes."""
pw.text_to_handwriting(txt,"demo1.png",[255,0,0])

print("END")



A simple Mail Merge project built with Python that automatically generates
personalized letters for a list of invited guests.

The project reads a template letter, retrieves names from a text file,
replaces the [name] placeholder with each person's name, and creates a separate 
personalized letter for every recipient.

⚙️ How It Works
Reads the template letter from starting_letter.txt.
Reads all names from invited_names.txt.
Removes unnecessary whitespace from each name.
Replaces the [name] placeholder with the recipient's name.
Creates a personalized letter for each recipient.
Saves the generated letters inside the ReadyToSend folder.


📁 Project Structure
Mail Merge Project/
│
├── Input/
│   ├── Letters/
│   │   └── starting_letter.txt
│   │
│   └── Names/
│       └── invited_names.txt
│
├── Output/
│   └── ReadyToSend/
│       ├── letter_for_Alex.txt
│       ├── letter_for_Sam.txt
│       └── ...
│
└── main.py


🛠️ Concepts Practiced
File handling with open()
Reading text files
Writing text files
readlines()
String manipulation
strip()
replace()
for loops
List comprehensions
Formatted strings (f-strings)
Automated file generation

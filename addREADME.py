import re

def increment_last_number_in_readme(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        readme_content = file.read()

    numbers = re.findall(r'\b\d+\b', readme_content)

    if numbers:
        last_number = numbers[-1]
        new_last_number = str(int(last_number) + 1)
        updated_readme_content = re.sub(r'\b{}\b$'.format(last_number), new_last_number, readme_content)
    else:
        updated_readme_content = readme_content + "\n1"

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(updated_readme_content)

increment_last_number_in_readme('README.MD')

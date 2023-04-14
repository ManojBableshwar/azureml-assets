from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap, CommentedSeq
import snakemd
import argparse
import re
import os

# parameter to read the component yaml file
parser = argparse.ArgumentParser()
parser.add_argument('--component', type=str, default='component.yaml')
args = parser.parse_args()

# read the component yaml file and parse it
yaml = YAML()
with open(args.component, 'r') as f:
    component = yaml.load(f)

doc = snakemd.new_doc()

def add_intro(doc, component):
    doc.add_heading(component['display_name'], level=2)
    doc.add_heading("Name ", level=3)
    doc.add_paragraph(component['name'])
    doc.add_heading("Version ", level=3)
    doc.add_paragraph(component['version'])
    doc.add_heading("Type ", level=3)
    doc.add_paragraph(component['type'])
    doc.add_heading("Description ", level=3)
    doc.add_paragraph(component['description'])
    return doc

# set attributes
def get_comments_map(self, key):
    coms = []
    comments = self.ca.items.get(key)
    if comments is None:
        return coms
    for token in comments:
        if token is None:
            continue
        elif isinstance(token, list):
            coms.extend(token)
        else:
            coms.append(token)
    return coms

def get_comments_seq(self, idx):
    coms = []
    comments = self.ca.items.get(idx)
    if comments is None:
        return coms
    for token in comments:
        if token is None:
            continue
        elif isinstance(token, list):
            coms.extend(token)
        else:
            coms.append(token)
    return coms


setattr(CommentedMap, 'get_comments', get_comments_map)
setattr(CommentedSeq, 'get_comments', get_comments_seq)

def check_comments(data):
    if isinstance(data, CommentedMap):
        for k, v in data.items():
           comments = data.get_comments(k)
    elif isinstance(data, CommentedSeq):
        for idx, item in enumerate(data):
            comments = data.get_comments(k)
    for comment in comments:
        text = comment.value
        text = re.sub(r"[\n\t\s]*", "", text)
        if text:
            return True 
    return False
        
def insert_comments_between_inputs(doc, data):
    if isinstance(data, CommentedMap):
        for k, v in data.items():
           comments = data.get_comments(k)
    elif isinstance(data, CommentedSeq):
        for idx, item in enumerate(data):
            comments = data.get_comments(k)
    for comment in comments:
        text=comment.value
        text = re.sub(r"#", "", text)
        doc.add_paragraph(text)

    return doc

def insert_comments_under_input(doc, data):
    for comments in data:
        if comments:
            for comment in comments:
                doc.add_paragraph(comment.value.strip('#'))
    return doc



def add_inputs(doc, component):
    doc.add_heading("Inputs ", level=2)
    headers = ['Name', 'Description', 'Type', 'Default', 'Optional', 'Enum']
    rows = []
    if component.ca.items.get('inputs') is not None:
        doc = insert_comments_under_input(doc, component.ca.items.get('inputs'))

    for k, v in component['inputs'].items():
        row = []
        row.append(k)
        row.append(v['description'] if 'description' in v else ' ')
        row.append(v['type'])
        row.append(v['default'] if 'default' in v else ' ')
        row.append(v['optional'] if 'optional' in v else ' ')
        row.append(v['enum'] if 'enum' in v else ' ') 
        
        if check_comments(v):
            rows.append(row)
            doc.add_table(headers, rows)
            doc = insert_comments_between_inputs(doc, v)
            rows = []  
        else:
            rows.append(row)

    doc.add_table(headers, rows)
    return doc


def add_outputs(doc, component):
    doc.add_heading("Outputs ", level=2)
    headers = ['Name', 'Description', 'Type']
    rows = []
    if component.ca.items.get('outputs') is not None:
        doc = insert_comments_under_input(doc, component.ca.items.get('outputs'))

    for k, v in component['outputs'].items():
        row = []
        row.append(k)
        row.append(v['description'] if 'description' in v else ' ')
        row.append(v['type'])
        
        if check_comments(v):
            rows.append(row)
            doc.add_table(headers, rows)
            doc = insert_comments_between_inputs(doc, v)
            rows = []      
        else:
            rows.append(row)

    doc.add_table(headers, rows)
    return doc

doc=add_intro(doc, component)
doc=add_inputs(doc, component)
doc=add_outputs(doc, component)

# get the directory of the component.yaml file
dir = os.path.dirname(args.component)

# write the README.md file in directory of the component.yaml file
with open(os.path.join(dir, 'README.md'), 'w') as f:
    f.write(doc.render())

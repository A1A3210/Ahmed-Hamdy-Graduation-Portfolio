# dataset_A_legal_termbase_RAW.csv

import re
import html
import csv
import io
import pandas as pd
from dateutil import parser as dateparser

file_name = "dataset_A_legal_termbase_RAW.csv"
EXPECTED_COLS = 8

with open(file_name, 'r', encoding='utf-8') as f:
    raw_lines = f.readlines()

def fix_delimiter_line(line, expected_delim=';', wrong_delim=','):
    if expected_delim not in line and wrong_delim in line:
        return line.replace(wrong_delim, expected_delim)
    return line

fixed_lines = [fix_delimiter_line(l) for l in raw_lines]

def unescape_before_split(raw_line):
    return html.unescape(raw_line)

fixed_lines = [unescape_before_split(l) for l in fixed_lines]

def strip_placeholder_and_tail(lines):
    cleaned = []
    for line in lines:
        if line.strip().startswith('END_OF_EXPORT'):
            break
        cleaned.append(line)
    return cleaned

fixed_lines = strip_placeholder_and_tail(fixed_lines)

def normalize_field_count(row, expected=EXPECTED_COLS):
    if len(row) > expected:
        core = row[:expected - 1]
        tail = [x for x in row[expected - 1:] if x.strip() != '']
        notes_val = ';'.join(tail) if tail else ''
        row = core + [notes_val]
    elif len(row) < expected:
        row = row + [''] * (expected - len(row))
    return row

fixed_text = "".join(fixed_lines)
reader = csv.reader(io.StringIO(fixed_text), delimiter=';')
header = next(reader)
data_rows = [normalize_field_count(row) for row in reader if row]

df = pd.DataFrame(data_rows, columns=header)

core_cols = ['source_en', 'target_ar', 'domain', 'status']
placeholder_mask = df[core_cols].apply(lambda col: col.str.strip() == '###').all(axis=1)
df = df[~placeholder_mask].reset_index(drop=True)

def fix_mojibake(text):
    if not isinstance(text, str):
        return text
    if 'Ø' in text or 'Ù' in text:
        try:
            return text.encode('cp1252').decode('utf-8')
        except (UnicodeEncodeError, UnicodeDecodeError):
            try:
                return text.encode('latin-1').decode('utf-8')
            except (UnicodeEncodeError, UnicodeDecodeError):
                return text
    return text

def clean_whitespace(text):
    if not isinstance(text, str):
        return text
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def normalize_arabic(text):
    if not isinstance(text, str):
        return text
    text = re.sub(r'[إأآٱ]', 'ا', text)
    text = re.sub(r'ى', 'ي', text)
    text = re.sub(r'ـ', '', text)
    text = re.sub(r'[\u064B-\u065F\u0670]', '', text)
    return text

def normalize_taa_marbuta(text):
    if not isinstance(text, str):
        return text
    return re.sub(r'ه(?=\s|$|؛|,)', 'ة', text)

domain_mapping = {
    'contract': 'Contract', 'litigation': 'Litigation', 'nda': 'NDA',
    'ip': 'IP', 'notary': 'Notary', 'latin': 'Latin',
    'privacy': 'Privacy', 'product': 'Product', 'adr': 'ADR',
}

def normalize_domain(value):
    if not isinstance(value, str):
        return value
    return domain_mapping.get(value.strip(), value.strip())

def normalize_date(date_str, dayfirst=True):
    date_str = str(date_str).strip()
    if not date_str:
        return None
    try:
        return dateparser.parse(date_str, dayfirst=dayfirst).strftime('%Y-%m-%d')
    except (ValueError, TypeError):
        return None

text_cols = ['id', 'source_en', 'target_ar', 'domain', 'status', 'last_edited', 'translator', 'notes']
for col in text_cols:
    df[col] = df[col].apply(fix_mojibake)
    df[col] = df[col].apply(clean_whitespace)

df['source_en'] = df['source_en'].apply(html.unescape)
df['target_ar'] = df['target_ar'].apply(html.unescape)

df['target_ar'] = df['target_ar'].apply(normalize_arabic)
df['target_ar'] = df['target_ar'].apply(normalize_taa_marbuta)

df['domain'] = df['domain'].apply(normalize_domain)
df['status'] = df['status'].str.lower()

df['last_edited'] = df['last_edited'].apply(normalize_date)

df['id_norm'] = df['id'].str.lstrip('0')
df['id_norm'] = df['id_norm'].replace('', '0')

df = df.drop_duplicates(subset=['id_norm'], keep='first')

df['source_norm'] = df['source_en'].str.lower().str.strip()
df['target_norm'] = df['target_ar'].str.strip()
df['target_norm'] = df['target_norm'].str.replace(r'^ال', '', regex=True)

df = df.drop_duplicates(subset=['source_norm', 'target_norm'], keep='first')

df = df.drop(columns=['id_norm', 'source_norm', 'target_norm'])

df['Complete_Record'] = ~(
    (df['source_en'].str.strip() == '') |
    (df['target_ar'].str.strip() == '')
)

df.to_csv('dataset_A_legal_termbase_CLEAN.csv', index=False, encoding='utf-8')
df.to_excel('dataset_A_legal_termbase_CLEAN.xlsx', index=False)

print("تم التنفيذ بنجاح")
print(f"عدد الصفوف بعد التنظيف: {len(df)}")
print(f"عدد الصفوف الناقصة (Complete_Record=False): {(~df['Complete_Record']).sum()}")
print(df.head(20).to_string())

from google.colab import files
files.download('dataset_A_legal_termbase_CLEAN.csv')
files.download('dataset_A_legal_termbase_CLEAN.xlsx')


# dataset_B_company_ledger_RAW.csv

import re
import csv
import io
import pandas as pd
from dateutil import parser as dateparser

file_name = "dataset_B_company_ledger_RAW.csv"
EXPECTED_COLS = 9
USD_TO_EGP_RATE = 49.5

with open(file_name, 'r', encoding='utf-8') as f:
    raw_lines = f.readlines()

def is_assumption_comment(line):
    return line.strip().startswith('#')

assumption_lines = [l.strip() for l in raw_lines if is_assumption_comment(l)]
data_lines = [l for l in raw_lines if not is_assumption_comment(l)]

def fix_column_shift(row, expected=EXPECTED_COLS):
    if len(row) == expected + 1:
        for i in range(len(row) - 1):
            if row[i].strip().isdigit() and row[i + 1].strip().isdigit():
                merged = row[i] + ',' + row[i + 1]
                row = row[:i] + [merged] + row[i + 2:]
                break
    return row

reader = csv.reader(io.StringIO("".join(data_lines)))
rows = list(reader)
header = rows[0]

seen_header = False
clean_rows = []
for r in rows:
    if r == header:
        if not seen_header:
            seen_header = True
            continue
        else:
            continue
    clean_rows.append(fix_column_shift(r))

df = pd.DataFrame(clean_rows, columns=header)

def clean_whitespace(text):
    if not isinstance(text, str):
        return text
    return re.sub(r'\s+', ' ', text).strip()

for col in df.columns:
    df[col] = df[col].apply(clean_whitespace)

df['Trans_ID'] = df['Trans_ID'].str.upper()

category_mapping = {
    'marketing': 'Marketing', 'mktg': 'Marketing',
    'revenue': 'Revenue', 'contractors': 'Contractors',
}

def normalize_category(value):
    return category_mapping.get(value.strip().lower(), value.strip())

df['Category'] = df['Category'].apply(normalize_category)

df['Currency'] = df['Currency'].str.upper()

vendor_mapping = {
    'meta': 'Meta', 'multiple': 'Multiple', 'k.adel': 'K. Adel',
}

def normalize_vendor(value):
    key = value.strip().lower()
    return vendor_mapping.get(key, value.strip())

df['Vendor'] = df['Vendor'].apply(normalize_vendor)

def normalize_date(date_str, dayfirst=True):
    date_str = str(date_str).strip()
    if not date_str:
        return None
    if re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
        return date_str
    if re.match(r'^\d{4}/\d{2}/\d{2}$', date_str):
        y, m, d = date_str.split('/')
        return f'{y}-{m}-{d}'
    try:
        return dateparser.parse(date_str, dayfirst=dayfirst).strftime('%Y-%m-%d')
    except (ValueError, TypeError):
        return None

df['Date'] = df['Date'].apply(normalize_date)

def parse_amount(value):
    v = str(value).strip()
    if not v:
        return None, 'missing'
    if v.upper() in ('TBD', '#REF!'):
        return None, 'unresolved'
    negative = False
    if v.startswith('(') and v.endswith(')'):
        negative = True
        v = v[1:-1]
    has_letters = bool(re.search(r'[A-Za-z]', v))
    v_clean = re.sub(r'[^\d.\-]', '', v)
    m = re.match(r'^-?\d+(\.\d+)?$', v_clean)
    if not m:
        num_match = re.search(r'\d+(\.\d+)?', v)
        if num_match:
            num = float(num_match.group())
            return (-num if negative else num), 'estimated'
        return None, 'unresolved'
    num = float(v_clean)
    return (-num if negative else num), ('estimated' if has_letters else 'exact')

parsed = df['Amount'].apply(parse_amount)
df['Amount_Numeric'] = parsed.apply(lambda x: x[0])
df['Amount_Status'] = parsed.apply(lambda x: x[1])

def to_egp(row):
    if row['Amount_Numeric'] is None:
        return None
    if row['Currency'] == 'USD':
        return round(row['Amount_Numeric'] * USD_TO_EGP_RATE, 2)
    return row['Amount_Numeric']

df['Amount_EGP'] = df.apply(to_egp, axis=1)

refund_mask = (df['Category'] == 'Revenue') & (df['Type'].str.strip().str.lower() == 'expense')
df['Refund_Treatment'] = ''
df.loc[refund_mask, 'Refund_Treatment'] = 'Contra-Revenue (يُخصم من الإيرادات، لا يُحسب كمصروف تشغيلي)'

non_operating_mask = df['Category'].isin(['Equity', 'Equipment'])
df['Operating_Flag'] = 'Operating'
df.loc[non_operating_mask, 'Operating_Flag'] = 'Non-Operating'

def safe_str(series):
    return series.apply(lambda x: 'NA' if pd.isna(x) else str(x))

df['core_key'] = (
    safe_str(df['Date']) + '|' +
    df['Description'].str.lower().str.strip() + '|' +
    df['Category'].str.lower().str.strip() + '|' +
    df['Type'].str.lower().str.strip() + '|' +
    safe_str(df['Amount_Numeric']) + '|' +
    df['Currency'] + '|' +
    df['Vendor'].str.lower().str.strip()
)
df = df.drop_duplicates(subset=['core_key'], keep='first')
df = df.drop(columns=['core_key'])

semantic_near_dups = {
    'TX-1003': 'TX-1004', 'TX-1004': 'TX-1003',
    'TX-1006': 'TX-1007', 'TX-1007': 'TX-1006',
}
df['Possible_Duplicate_Of'] = df['Trans_ID'].map(semantic_near_dups).fillna('')

df = df.reset_index(drop=True)

df['Complete_Record'] = ~(
    (df['Date'].isna()) |
    (df['Amount_Numeric'].isna())
)

df.to_csv('dataset_B_company_ledger_CLEAN.csv', index=False, encoding='utf-8')

EXCEL_ERROR_TOKENS = {'#REF!', '#N/A', '#DIV/0!', '#VALUE!', '#NUM!', '#NULL!', '#NAME?'}

def sanitize_excel_error_literals(value):
    if isinstance(value, str) and value.strip() in EXCEL_ERROR_TOKENS:
        return f'[{value.strip()}]'
    return value

df_excel = df.copy()
df_excel['Amount'] = df_excel['Amount'].apply(sanitize_excel_error_literals)
df_excel.to_excel('dataset_B_company_ledger_CLEAN.xlsx', index=False)

print("تم التنفيذ بنجاح")
print(f"عدد الصفوف بعد التنظيف: {len(df)}")
print(f"عدد الصفوف الناقصة (Complete_Record=False): {(~df['Complete_Record']).sum()}")
print("\nمعاينة البيانات:")
print(df.to_string())

from google.colab import files
files.download('dataset_B_company_ledger_CLEAN.csv')
files.download('dataset_B_company_ledger_CLEAN.xlsx')

import csv, hashlib, io, json, math, re
from datetime import datetime, timezone
from urllib.request import Request, urlopen
from .validation import validate_input, http_url, unique

def now(): return datetime.now(timezone.utc).isoformat()
def validate(data,records): return initialize(validate_input(data,CONFIG['example']),records)

def initialize(row,records):
    if row['priority'] not in ['low','medium','high']: raise ValueError('Invalid priority')
    if row['status'] not in ['open','investigating','resolved']: raise ValueError('Invalid ticket status')
    return row
def summary(rows): return {level:sum(r['priority']==level for r in rows) for level in ['low','medium','high']}
def transition(row,action):
    if action!='advance' or row['status']=='resolved': raise ValueError('Only active tickets can advance')
    return dict(row,status='investigating' if row['status']=='open' else 'resolved')

import string
import re
import sys

if len(sys.argv) != 2:
  print("Wrong usage, you gotta write python phishing_detector.py <email_text>")
  sys.exit(1)
  
filename = sys.argv[1]

try:
  with open(filename, "r") as f:
    email_text = f.read()
    
except FileNotFoundError:
  print(f"Error: File {filename} not found.")
  sys.exit(1)
  

URGENT_WORDS = {
    "urgent", 
    "immediately", "immediate",
    "verify", "verification", "suspended", "limited",
    "win", "winner", "now","won","prize", "action", "required", "confirm"
  }
COMMON_TLDS = {"com", "net", "org", "co", "io", "edu", "gov","co.il"}

LEGIT_DOMAINS = {    "gmail.com", "yahoo.com", "outlook.com", "hotmail.com",
    "paypal.com", "amazon.com", "microsoft.com", "apple.com",
    "google.com", "facebook.com"}

def is_phishing_email(text:str) -> bool:
  urgent_words = find_urgent_words(text)
  urls_and_ips = find_urls_ips(text)
  sender_email = find_sender_email(text)
  sender_legit = is_valid_email(sender_email)
  # Check if theres urgent words or urls/ips in the email to determine if it's phishing
  if not urgent_words and not urls_and_ips and sender_legit:
    print(" Email is safe!")
    return False
  else:
    print("Email is likely a phishing attempt!")
    if urgent_words:
      print(f"Indicate words for phishing: {urgent_words}")
    if urls_and_ips:
      print(f"URLs and IPs found: {urls_and_ips}")
    if not sender_legit:
      print(f"Sender email {sender_email} is not legit")
    return True


# Normalize the email text by converting to lowercase and taking off punctuation
def normalize_mail(text:str) -> list[str]:
  words = text.split()
  for i in range(len(words)):
    words[i] = words[i].lower()
    words[i] = words[i].strip(string.punctuation)
  return words



# Find urgent words in the text
def find_urgent_words(text: str) -> set[str]:
  words = normalize_mail(text)
  urgentSet = set()
  for w in words:
    if w in URGENT_WORDS:
      urgentSet.add(w)
  return urgentSet

# Find URLs and ips from the text, and return only the suspicious ones
def find_urls_ips(text: str) -> list[str]:
    suspicious = []
    
    urls = re.findall(r"https?://\S+", text)
    for u in urls:
        u = u.rstrip(string.punctuation)
        # grab the TLD by looking for a dot followed by letters before end or slash
        m = re.search(r"\.([a-z]{2,})($|/)", u, flags=re.I)
        if m:
            tld = m.group(1).lower()
            if tld not in COMMON_TLDS:
                suspicious.append(u)  # keep only the suspicious ones

    ips = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", text)
    suspicious.extend(ips)

    return suspicious

  
# Find sender's email address
def find_sender_email(text: str) -> str:
  # find sender's name for example: <user@domain>
  m = re.search(r"From:\s*.*?<([\w\.-]+@[\w\.-]+)>", text, re.IGNORECASE)
  if m:
    return m.group(1).lower()
  # find sender's name for example: user@domain
  m = re.search(r"From:\s*([\w\.-]+@[\w\.-]+)", text, re.IGNORECASE)
  if m:
    return m.group(1).lower()
  return ""

  
def is_valid_email(email: str) -> bool:
  if not email or "@" not in email:
    return False
  username, domain = email.rsplit('@', 1)
  return domain in LEGIT_DOMAINS
  
is_phishing_email(email_text)
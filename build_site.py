import os
from zipfile import ZipFile

project_name = "multilang_website"
folders = [f"{project_name}/pages", f"{project_name}/js", f"{project_name}/css"]
for folder in folders:
    os.makedirs(folder, exist_ok=True)

html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <link rel="stylesheet" href="../css/style.css" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" />
</head>
<body>
  <header>
    <nav class="navbar">
      <div class="logo" data-key="Wajjiraa">Wajjiraa Abbaa Alangaa Kutaa <br>Magaalaa Kooyyee Faccee</div>
      <ul class="nav-links">
        <li><a href="../index.html" data-key="home">Fuul-Duraa</a></li>
        <li class="dropdown">
          <a href="about.html" data-key="about">Waa'ee</a>
          <ul class="dropdown-menu">
            <li><a href="mission.html" data-key="mission">Ergama</a></li>
            <li><a href="roles.html" data-key="roles">Gahee Hojii</a></li>
            <li><a href="message.html" data-key="message">Establishment</a></li>
            <li><a href="structure.html" data-key="structure">Caasaa</a></li>
            <li><a href="call.html" data-key="callToAction">Call to Action</a></li>
            <li><a href="concerns.html" data-key="concerns">Itti Waamamaa</a></li>
          </ul>
        </li>
        <li><a href="#" data-key="services">Tajaajiloota</a></li>
        <li><a href="#" data-key="laws">Seroota</a></li>
        <li><a href="#" data-key="news">Oduu</a></li>
        <li><a href="#" data-key="collection">Collection</a></li>
        <li><a href="#" data-key="contact">Contact</a></li>
      </ul>
      <select id="languageSwitcher">
        <option value="om">Afan Oromo</option>
        <option value="en">English</option>
        <option value="am">Amharic</option>
      </select>
    </nav>
  </header>
  <main>
    <h1 data-key="{key}">{heading}</h1>
    <p>This is the {title} page.</p>
  </main>
  <script src="../js/script.js"></script>
</body>
</html>
'''

pages = {
    "index.html": ("Home", "welcome", "Bagaa Gara Wajjiraa Nagaan Dhuftan"),
    "about.html": ("About", "about", "Waa'ee Wajjiraa"),
    "mission.html": ("Mission", "mission", "Ergama"),
    "roles.html": ("Roles", "roles", "Gahee Hojii"),
    "message.html": ("Establishment", "message", "Establishment"),
    "structure.html": ("Structure", "structure", "Caasaa"),
    "call.html": ("Call to Action", "callToAction", "Call to Action"),
    "concerns.html": ("Concerns", "concerns", "Itti Waamamaa"),
}

for filename, (title, key, heading) in pages.items():
    path = f"{project_name}/index.html" if filename == "index.html" else f"{project_name}/pages/{filename}"
    with open(path, "w", encoding="utf-8") as f:
        f.write(html_template.format(title=title, key=key, heading=heading))

# JavaScript
script_js = '''const translations = {
  en: {
    Wajjiraa: "Prosecutor Office", home: "Home", about: "About", mission: "Mission",
    roles: "Roles", message: "Establishment", structure: "Structure", callToAction: "Call to Action",
    concerns: "Concerns", services: "Services", laws: "Laws", news: "News", collection: "Collection",
    contact: "Contact", welcome: "Welcome"
  },
  om: {
    Wajjiraa: "Wajjiraa Abbaa Alangaa Kutaa Magaalaa Kooyyee Faccee", home: "Fuul-Duraa",
    about: "Waa'ee", mission: "Ergama", roles: "Gahee Hojii fi Itti Gaafatamummaa",
    message: "Establishment", structure: "Caasaa", callToAction: "Call to Action",
    concerns: "Itti Waamamaa", services: "Tajaajiloota", laws: "Seroota", news: "Oduu",
    collection: "Collection", contact: "Contact", welcome: "Bagaa Gara Wajjiraa Nagaan Dhuftan"
  },
  am: {
    Wajjiraa: "የአቃቢ አቃቢ ጽ/ቤት", home: "መነሻ", about: "ስለ", mission: "ተልዕኮ",
    roles: "ሚናዎች", message: "መመስረት", structure: "አዋቂ", callToAction: "ጥሪ",
    concerns: "አስተያየቶች", services: "አገልግሎቶች", laws: "ሕጎች", news: "ዜና",
    collection: "ስብስብ", contact: "አግኙን", welcome: "እንኳን ደህና መጡ"
  }
};

const languageSwitcher = document.getElementById('languageSwitcher');
let currentLang = localStorage.getItem('lang') || 'om';

function applyLanguage(lang) {
  document.querySelectorAll('[data-key]').forEach(el => {
    const key = el.getAttribute('data-key');
    if (translations[lang][key]) el.textContent = translations[lang][key];
  });
  localStorage.setItem('lang', lang);
  languageSwitcher.value = lang;
}

languageSwitcher.addEventListener('change', () => {
  applyLanguage(languageSwitcher.value);
});

document.addEventListener('DOMContentLoaded', () => {
  applyLanguage(currentLang);
});
'''
with open(f"{project_name}/js/script.js", "w", encoding="utf-8") as f:
    f.write(script_js)

# CSS
style_css = '''body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
.navbar { display: flex; justify-content: space-between; background: #004080; padding: 1rem; color: white; }
.nav-links, .dropdown-menu { list-style: none; padding: 0; margin: 0; }
.nav-links li { display: inline-block; margin: 0 10px; position: relative; }
.nav-links li a { color: white; text-decoration: none; }
.dropdown-menu { display: none; position: absolute; background: #0066cc; top: 100%; left: 0; }
.dropdown:hover .dropdown-menu { display: block; }
select { margin-left: 1rem; }
main { padding: 20px; }
'''
with open(f"{project_name}/css/style.css", "w", encoding="utf-8") as f:
    f.write(style_css)

# Zip it
with ZipFile(f"{project_name}.zip", "w") as zipf:
    for root, _, files in os.walk(project_name):
        for file in files:
            path = os.path.join(root, file)
            zipf.write(path, os.path.relpath(path, project_name))
print("✅ Website generated and zipped as multilang_website.zip")

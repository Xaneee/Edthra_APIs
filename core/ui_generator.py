def generate_basic_ui(title: str, theme: str = "dark"):
    return f"""<!DOCTYPE html>
<html>
<head>
  <title>{title}</title>
  <style>
    body {{ background: {'#000' if theme == 'dark' else '#fff'}; color: {'#fff' if theme == 'dark' else '#000'}; font-family: sans-serif; }}
    .header {{ font-size: 2em; margin-top: 2rem; text-align: center; }}
  </style>
</head>
<body>
  <div class="header">{title} – Powered by Edithra</div>
</body>
</html>"""

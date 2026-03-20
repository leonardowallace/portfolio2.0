
import logging

class PortfolioGenerator:
    def __init__(self, config):
        self.config = config
        self.personal = config['personal']
        self.experience = config['experience']
        self.projects = config['projects']
        self.contact = config['contact']
        self.education = config['education']
        self.skills = config['skills']

    def generate_html(self):
        """Builds premium semantic HTML5 structure."""
        
        # Nav links
        nav_html = "".join([f'<li><a href="#{item.lower()}">{item}</a></li>' for item in ["Home", "Experiência", "Projetos", "Contato"]])
        
        # Experience section
        exp_html = ""
        for exp in self.experience:
            status_tag = '<span class="current-tag">Atual</span>' if exp.get('current') else ''
            desc_list = "".join([f'<li>{d}</li>' for d in exp['description']])
            exp_html += f'''
            <div class="glass-card exp-item">
                <div class="exp-header">
                    <h3>{exp['role']} @ {exp['company']} {status_tag}</h3>
                    <span class="period">{exp['period']}</span>
                </div>
                <ul>{desc_list}</ul>
            </div>
            '''

        # Projects section
        proj_html = ""
        for proj in self.projects:
            proj_html += f'''
            <a href="{proj['link']}" target="_blank" class="glass-card project-card">
                <span class="proj-type">{proj['type']}</span>
                <h3>{proj['name']}</h3>
                <p>{proj['description']}</p>
                <div class="proj-arrow">ir para projeto ↗</div>
            </a>
            '''

        # Skills section
        skills_html = "".join([f'<span class="skill-tag">{skill}</span>' for skill in self.skills])

        # Main HTML Template
        html = f'''<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.personal['name']} | Portfólio</title>
    <link rel="icon" type="image/png" href="favicon.png">
    <link rel="stylesheet" href="index.css">
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap" rel="stylesheet">
</head>
<body>
    <div class="bg-glow"></div>
    
    <nav>
        <div class="logo">{self.personal['name'].split()[0]}<span>.</span></div>
        <ul>{nav_html}</ul>
    </nav>

    <main>
        <section id="home" class="hero">
            <div class="hero-content">
                <span class="badge">Disponível para novos desafios</span>
                <h1>{self.personal['name']}</h1>
                <h2>{self.personal['title']}</h2>
                <p class="about-text">{self.personal['about']}</p>
                <div class="hero-actions">
                    <a href="#projeos" class="btn-primary">Ver Projetos</a>
                    <a href="{self.personal['cv_link']}" class="btn-secondary" download>Baixar CV</a>
                </div>
            </div>
        </section>

        <section id="experiência" class="section">
            <h2 class="section-title">Experiência Profissional</h2>
            <div class="grid-container">
                {exp_html}
            </div>
        </section>

        <section id="projetos" class="section">
            <h2 class="section-title">Projetos em Destaque</h2>
            <div class="grid-container">
                {proj_html}
            </div>
        </section>

        <section class="section">
            <h2 class="section-title">Habilidades & Educação</h2>
            <div class="dual-grid">
                <div class="glass-card">
                    <h3>Minhas Skills</h3>
                    <div class="skills-flex">{skills_html}</div>
                </div>
                <div class="glass-card">
                    <h3>Educação</h3>
                    {"".join([f'<div class="edu-item"><strong>{e["degree"]}</strong><br>{e["institution"]} ({e["year"]})</div>' for e in self.education])}
                </div>
            </div>
        </section>

        <section id="contato" class="contact-section">
            <div class="glass-card contact-inner">
                <h2>Vamos trabalhar juntos?</h2>
                <p>Estou pronto para contribuir com suas soluções de TI e automação.</p>
                <div class="social-links">
                    <a href="{self.contact['linkedin']}" target="_blank">LinkedIn</a>
                    <a href="{self.contact['github']}" target="_blank">GitHub</a>
                    <a href="{self.contact['instagram']}" target="_blank">Instagram</a>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <p>© 2026 {self.personal['name']} - Gerado via Python Automation.</p>
    </footer>
</body>
</html>
'''
        return html

    def generate_css(self):
        """Generates a premium dark mode CSS with glassmorphism."""
        css = '''
:root {
    --bg: #050505;
    --card: rgba(255, 255, 255, 0.03);
    --border: rgba(255, 255, 255, 0.1);
    --accent: #7c7aff;
    --accent-glow: rgba(124, 122, 255, 0.3);
    --text: #ffffff;
    --text-dim: #e0e0e0;
    --nav-blur: rgba(2, 2, 2, 0.9);
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Outfit', sans-serif;
}

html {
    scroll-behavior: smooth;
}

body {
    background-color: var(--bg);
    background-image: linear-gradient(rgba(5, 5, 5, 0.8), rgba(5, 5, 5, 0.8)), url('../../data/input/bg.png');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: var(--text);
    line-height: 1.6;
    overflow-x: hidden;
}

.bg-glow {
    display: none; /* Imagem de fundo substitui o glow manual */
}

nav {
    position: fixed;
    top: 0;
    width: 100%;
    padding: 1.5rem 5%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: var(--nav-blur);
    backdrop-filter: blur(20px);
    z-index: 1000;
    border-bottom: 1px solid var(--border);
}

.logo {
    font-size: 1.5rem;
    font-weight: 800;
    letter-spacing: -1px;
}

.logo span { color: var(--accent); }

nav ul {
    display: flex;
    list-style: none;
    gap: 2rem;
}

nav a {
    text-decoration: none;
    color: var(--text-dim);
    transition: 0.3s;
    font-size: 0.9rem;
    font-weight: 400;
}

nav a:hover { color: var(--text); }

main {
    padding: 0 5%;
    max-width: 1200px;
    margin: 0 auto;
}

.hero {
    height: 100vh;
    display: flex;
    align-items: center;
    padding-top: 5rem;
}

.hero-content {
    max-width: 800px;
}

.badge {
    padding: 6px 12px;
    background: var(--accent-glow);
    border: 1px solid var(--accent);
    color: var(--accent);
    border-radius: 50px;
    font-size: 0.8rem;
    font-weight: 600;
}

h1 {
    font-size: clamp(2.5rem, 8vw, 4.5rem);
    font-weight: 800;
    margin: 1.5rem 0 0.5rem;
    letter-spacing: -2px;
    line-height: 1.1;
}

h2 {
    font-size: 1.5rem;
    color: var(--text-dim);
    font-weight: 400;
    margin-bottom: 2rem;
}

.about-text {
    font-size: 1.1rem;
    color: var(--text-dim);
    margin-bottom: 3rem;
    max-width: 600px;
}

.hero-actions {
    display: flex;
    gap: 1.5rem;
}

.btn-primary, .btn-secondary {
    padding: 12px 30px;
    border-radius: 12px;
    text-decoration: none;
    font-weight: 600;
    transition: 0.3s transform;
    display: inline-block;
}

.btn-primary {
    background: var(--accent);
    color: white;
}

.btn-secondary {
    background: var(--card);
    border: 1px solid var(--border);
    color: white;
}

.btn-primary:hover, .btn-secondary:hover {
    transform: translateY(-5px);
}

.section {
    padding: 8rem 0;
}

.section-title {
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 3rem;
    position: relative;
    padding-left: 1rem;
    border-left: 4px solid var(--accent);
}

.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 2rem;
}

.glass-card {
    background: var(--card);
    border: 1px solid var(--border);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 2rem;
    transition: 0.3s;
}

.glass-card:hover {
    border-color: var(--accent);
    background: rgba(255,255,255,0.05);
}

.exp-item h3 { font-size: 1.2rem; margin-bottom: 0.5rem; }
.exp-item .period { font-size: 0.9rem; color: var(--accent); display: block; margin-bottom: 1.5rem; }
.exp-item ul { list-style: none; }
.exp-item li { color: var(--text-dim); margin-bottom: 10px; position: relative; padding-left: 15px; }
.exp-item li::before { content: "•"; color: var(--accent); position: absolute; left: 0; }

.current-tag {
    font-size: 0.7rem;
    background: green;
    padding: 2px 8px;
    border-radius: 4px;
    margin-left: 10px;
    vertical-align: middle;
}

.project-card {
    text-decoration: none;
    color: inherit;
    display: flex;
    flex-direction: column;
}

.proj-type { font-size: 0.7rem; color: var(--accent); text-transform: uppercase; font-weight: 700; }
.project-card h3 { margin: 10px 0; }
.project-card p { color: var(--text-dim); font-size: 0.9rem; flex-grow: 1; }
.proj-arrow { font-size: 0.8rem; margin-top: 2rem; font-weight: 600; color: var(--accent); }

.dual-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
}

.skills-flex {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 1.5rem;
}

.skill-tag {
    background: var(--border);
    padding: 6px 15px;
    border-radius: 8px;
    font-size: 0.8rem;
}

.edu-item { margin-top: 1.5rem; }

.contact-section { padding: 10rem 0; text-align: center; }
.contact-inner { max-width: 600px; margin: 0 auto; }
.contact-inner h2 { font-size: 2.5rem; margin-bottom: 1rem; color: white; }
.social-links { display: flex; justify-content: center; gap: 2rem; margin-top: 3rem; }
.social-links a { text-decoration: none; color: white; font-weight: 600; border-bottom: 1px solid var(--accent); }

footer {
    padding: 4rem;
    text-align: center;
    border-top: 1px solid var(--border);
    color: var(--text-dim);
    font-size: 0.8rem;
}

@media (max-width: 768px) {
    nav ul { display: none; }
    .dual-grid { grid-template-columns: 1fr; }
    h1 { font-size: 3rem; }
}
'''
        return css

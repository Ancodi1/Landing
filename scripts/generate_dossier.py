from pathlib import Path
import sys

from PIL import Image
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.utils import ImageReader

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "public" / "Dossier-Angel-Collazo-Diaz.pdf"
W, H = A4
M = 16 * mm

BG = HexColor("#FBF7F1")
PAPER = HexColor("#FFFDF9")
INK = HexColor("#17171A")
MUTED = HexColor("#4D473F")
GREEN = HexColor("#263A34")
GOLD = HexColor("#A28757")
LINE = HexColor("#DED4C4")
SOFT = HexColor("#F1E8DA")

font_dir = Path("/usr/share/fonts/truetype/dejavu")
pdfmetrics.registerFont(TTFont("DV", font_dir / "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DV-Bold", font_dir / "DejaVuSans-Bold.ttf"))

styles = {
    "body": ParagraphStyle("body", fontName="DV", fontSize=9.5, leading=14, textColor=MUTED),
    "small": ParagraphStyle("small", fontName="DV", fontSize=8, leading=11, textColor=MUTED),
    "lead": ParagraphStyle("lead", fontName="DV", fontSize=12, leading=18, textColor=MUTED),
    "h1": ParagraphStyle("h1", fontName="DV-Bold", fontSize=29, leading=34, textColor=INK),
    "h2": ParagraphStyle("h2", fontName="DV-Bold", fontSize=22, leading=27, textColor=INK),
    "h3": ParagraphStyle("h3", fontName="DV-Bold", fontSize=14, leading=17, textColor=INK),
    "center": ParagraphStyle("center", fontName="DV", fontSize=9, leading=13, textColor=MUTED, alignment=TA_CENTER),
}


def p(c, text, x, y_top, width, style="body"):
    para = Paragraph(text, styles[style])
    _, height = para.wrap(width, H)
    para.drawOn(c, x, y_top - height)
    return y_top - height


def image(c, path, x, y, width, height, contain=True):
    path = ROOT / path
    with Image.open(path) as im:
        iw, ih = im.size
    scale = min(width / iw, height / ih) if contain else max(width / iw, height / ih)
    dw, dh = iw * scale, ih * scale
    c.saveState()
    c.rect(x, y, width, height, stroke=0, fill=0)
    c.clipPath(c.beginPath(), stroke=0, fill=0) if False else None
    c.drawImage(ImageReader(str(path)), x + (width - dw) / 2, y + (height - dh) / 2, dw, dh, mask="auto")
    c.restoreState()


def header(c, title):
    c.setFillColor(BG)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    c.setFont("DV-Bold", 7.5)
    c.setFillColor(GREEN)
    c.drawString(M, H - 12 * mm, title.upper())
    c.setStrokeColor(LINE)
    c.line(M, H - 15 * mm, W - M, H - 15 * mm)


def footer(c, number, label="Ángel Collazo Díaz · Dossier profesional"):
    c.setStrokeColor(LINE)
    c.line(M, 12 * mm, W - M, 12 * mm)
    c.setFillColor(MUTED)
    c.setFont("DV", 7)
    c.drawString(M, 8 * mm, label)
    c.drawRightString(W - M, 8 * mm, f"{number:02d}")


def kicker(c, text, x, y):
    c.setFont("DV-Bold", 7.5)
    c.setFillColor(GREEN)
    c.drawString(x, y, text.upper())


def tag(c, text, x, y):
    width = c.stringWidth(text, "DV-Bold", 7.2) + 5 * mm
    c.setFillColor(SOFT)
    c.roundRect(x, y - 5 * mm, width, 5.5 * mm, 2.2 * mm, stroke=0, fill=1)
    c.setFillColor(GREEN)
    c.setFont("DV-Bold", 7.2)
    c.drawString(x + 2.5 * mm, y - 3.5 * mm, text)
    return width


def tags(c, items, x, y, max_width):
    cursor_x, cursor_y = x, y
    for item in items:
        needed = c.stringWidth(item, "DV-Bold", 7.2) + 5 * mm
        if cursor_x + needed > x + max_width:
            cursor_x, cursor_y = x, cursor_y - 7 * mm
        cursor_x += tag(c, item, cursor_x, cursor_y) + 1.5 * mm


def card(c, x, y, w, h):
    c.setFillColor(PAPER)
    c.setStrokeColor(LINE)
    c.roundRect(x, y, w, h, 4 * mm, stroke=1, fill=1)


def project(c, y, title, meta, summary, result, tools, img, url="", contain=False, height=66 * mm):
    x, w = M, W - 2 * M
    card(c, x, y - height, w, height)
    image(c, img, x + 5 * mm, y - 47 * mm, 38 * mm, 38 * mm, contain=contain)
    tx, tw = x + 49 * mm, w - 55 * mm
    kicker(c, meta, tx, y - 8 * mm)
    cursor = p(c, title, tx, y - 12 * mm, tw, "h3") - 2 * mm
    cursor = p(c, summary, tx, cursor, tw, "body") - 2 * mm
    if result:
        c.setStrokeColor(GOLD)
        c.setLineWidth(1.5)
        c.line(tx, cursor, tx, cursor - 13 * mm)
        cursor = p(c, result, tx + 3 * mm, cursor, tw - 3 * mm, "small") - 2 * mm
    tags(c, tools, tx, cursor, tw)
    if url:
        c.setFillColor(GREEN)
        c.setFont("DV", 7)
        c.drawString(tx, y - height + 5 * mm, url)
    return y - height - 6 * mm


c = canvas.Canvas(str(OUT), pagesize=A4, pageCompression=1)
c.setTitle("Dossier profesional · Ángel Collazo Díaz")
c.setAuthor("Ángel Collazo Díaz")

# 1 · Portada
header(c, "Ángel Collazo Díaz · Dossier profesional")
card(c, M, 76 * mm, W - 2 * M, 174 * mm)
kicker(c, "Desarrollador full stack freelance en Galicia", M + 10 * mm, 230 * mm)
y = p(c, "Desarrollo web, diseño y marketing digital para empresas.", M + 10 * mm, 218 * mm, W - 2 * M - 20 * mm, "h1") - 7 * mm
p(c, "Ayudo a marcas y empresas de Galicia y del resto de España con desarrollo full stack, diseño web, SEO, campañas digitales y una estrategia clara para captar clientes.", M + 10 * mm, y, W - 2 * M - 20 * mm, "lead")
c.setFillColor(GREEN)
c.roundRect(M, 34 * mm, W - 2 * M, 30 * mm, 4 * mm, stroke=0, fill=1)
c.setFillColor(white); c.setFont("DV-Bold", 12); c.drawString(M + 7 * mm, 52 * mm, "Ángel Collazo Díaz")
c.setFont("DV", 9); c.drawString(M + 7 * mm, 44 * mm, "angelcollazodiaz@gmail.com  ·  www.angelcollazo.com")
footer(c, 1); c.showPage()

# 2 · Capacidades
header(c, "Perfil y capacidades")
kicker(c, "Conocimientos y habilidades", M, H - 25 * mm)
y = p(c, "Un perfil para desarrollar, comunicar y hacer crecer proyectos digitales.", M, H - 31 * mm, W - 2 * M, "h2") - 3 * mm
p(c, "Combino programación, marketing digital y diseño para ofrecer un servicio completo, desde la parte técnica hasta el posicionamiento y la captación de clientes.", M, y, W - 2 * M, "lead")
skills = [
    ("Desarrollo y tecnologías", ["PHP", "Java", "JavaScript", "C#", "HTML5", "CSS3", "Node.js", "Spring Boot"]),
    ("Bases de datos y herramientas", ["MySQL", "MariaDB", "SQL", "Git", "Docker", "XAMPP", "PrestaShop"]),
    ("Marketing digital", ["SEO", "SEM", "Google Ads", "GA4", "Analítica web", "Gestión de contenidos"]),
    ("Diseño y comunicación", ["Branding", "Diseño publicitario", "Canva", "Photoshop", "After Effects", "Premiere", "Probance"]),
    ("Certificaciones", ["Google Analytics", "Google Ads Measurement", "Hacking web y ethical hacking"]),
    ("Idiomas", ["Inglés · B2", "Portugués · B1", "Castellano · Nativo", "Gallego · Nativo"]),
]
top = 178 * mm
cw, ch = (W - 2 * M - 5 * mm) / 2, 46 * mm
for i, (title, items) in enumerate(skills):
    col, row = i % 2, i // 2
    x, y0 = M + col * (cw + 5 * mm), top - row * (ch + 5 * mm)
    card(c, x, y0 - ch, cw, ch)
    p(c, title, x + 5 * mm, y0 - 5 * mm, cw - 10 * mm, "h3")
    tags(c, items, x + 5 * mm, y0 - 23 * mm, cw - 10 * mm)
footer(c, 2); c.showPage()

# 3 · Proyectos destacados
header(c, "Selección de proyectos")
kicker(c, "Proyecto destacado", M, H - 25 * mm)
y = p(c, "Audiovisual para Venditalia 2026", M, H - 31 * mm, 110 * mm, "h2")
image(c, "public/imx/Venditalia-2026_800x800.jpg", W - M - 56 * mm, H - 91 * mm, 56 * mm, 56 * mm)
y = p(c, "Idea, diseño y montaje de todo el contenido audiovisual para un evento internacional B2B.", M, y - 5 * mm, 108 * mm, "lead") - 3 * mm
p(c, "El audiovisual se diseñó como una pieza central del stand para captar la atención en un entorno de gran afluencia. Se proyectó en bucle durante varias horas en pantallas de gran formato, consiguiendo visibilidad ante miles de asistentes.", M, y, 108 * mm, "body")
tags(c, ["Premiere", "After Effects", "Edición de vídeo", "Diseño audiovisual"], M, 174 * mm, 108 * mm)
project(c, 146 * mm, "Alma Matter", "Proyecto personal · Aplicación full stack", "Aplicación académica para gestionar alumnos, asignaturas y exámenes en entidades que imparten cursos o clases online.", "Aplicación funcional y responsive con CRUD, búsqueda, paginación, validaciones y seguridad web.", ["PHP", "MySQL", "JavaScript", "MVC"], "public/imx/logo.png", "github.com/Ancodi1/Academia-Alma-Matter-Ancodi", True, 75 * mm)
footer(c, 3, "Ángel Collazo Díaz · Proyectos"); c.showPage()

# 4 · Proyectos web
header(c, "Selección de proyectos")
p(c, "Desarrollo web y presencia digital", M, H - 25 * mm, W - 2 * M, "h2")
y = 237 * mm
y = project(c, y, "Nana Nails", "Trabajo finalizado · Web para negocio local", "Diseño y desarrollo web para representar la identidad del negocio, presentar sus servicios y mejorar su visibilidad en búsquedas locales.", "Web profesional, responsive y optimizada para facilitar el contacto con potenciales clientes.", ["Astro", "SEO local", "UX", "Responsive"], "src/imx/logonana.jpg", "www.nananailscarballo.com", False, 61 * mm)
y = project(c, y, "Guardia Omeya", "Proyecto personal · Comunidad gaming", "Espacio web de presentación, comunidad e identidad para un clan de Mount & Blade II: Bannerlord.", "", ["Diseño web", "Desarrollo", "Experiencia UX"], "src/imx/logoomeya.png", "www.guardiaomeya.com", True, 55 * mm)
project(c, y, "Coronas Ibéricas", "Trabajo finalizado · Colaboración web", "Colaboración en una web con conexiones en tiempo real a Discord y acciones dinámicas.", "", ["Colaboración web", "Desarrollo web"], "src/imx/logoci.webp", "www.coronasibericas.com", True, 55 * mm)
footer(c, 4, "Ángel Collazo Díaz · Proyectos"); c.showPage()

# 5 · Banners
header(c, "Diseño y comunicación visual")
kicker(c, "Banners sólidos", M, H - 25 * mm)
y = p(c, "Piezas promocionales adaptadas a distintos formatos", M, H - 31 * mm, W - 2 * M, "h2") - 2 * mm
p(c, "Selección de trabajos publicitarios realizados para marcas como Durex, Grefusa, Gullón y Eneryeti, entre otras.", M, y, W - 2 * M, "body")
image(c, "public/imx/MUESTRABANNERS.webp", M, 126 * mm, W - 2 * M, 100 * mm)
p(c, "Formatos móviles", M, 116 * mm, W - 2 * M, "h3")
image(c, "public/imx/banner-novedades-movil.png", M, 78 * mm, W - 2 * M, 28 * mm)
image(c, "public/imx/bannermovil445x154.png", M, 42 * mm, W - 2 * M, 25 * mm)
footer(c, 5, "Ángel Collazo Díaz · Diseño"); c.showPage()

# 6 · Flyers
header(c, "Diseño y comunicación visual")
kicker(c, "Flyers Venditalia 2026", M, H - 25 * mm)
y = p(c, "Diseño para feria internacional", M, H - 31 * mm, W - 2 * M, "h2") - 2 * mm
p(c, "Piezas utilizadas en Venditalia 2026, donde representé a la marca y participé activamente en la captación de nuevos clientes y en reuniones con potenciales socios comerciales.", M, y, W - 2 * M, "body")
fw = (W - 2 * M - 8 * mm) / 2
image(c, "public/imx/flyer-a.png", M, 27 * mm, fw, 205 * mm)
image(c, "public/imx/flyer-b.png", M + fw + 8 * mm, 27 * mm, fw, 205 * mm)
footer(c, 6, "Ángel Collazo Díaz · Diseño"); c.showPage()

# 7 · Contacto
header(c, "Contacto")
card(c, M, 74 * mm, W - 2 * M, 166 * mm)
kicker(c, "Disponible para proyectos freelance", M + 10 * mm, 220 * mm)
y = p(c, "Ángel Collazo Díaz", M + 10 * mm, 208 * mm, W - 2 * M - 20 * mm, "h2") - 4 * mm
y = p(c, "Disponible como desarrollador web y profesional de marketing digital freelance para proyectos en Galicia y toda España.", M + 10 * mm, y, W - 2 * M - 20 * mm, "lead") - 8 * mm
p(c, "<b>Correo</b><br/>angelcollazodiaz@gmail.com<br/><br/><b>Portfolio</b><br/>www.angelcollazo.com<br/><br/><b>GitHub</b><br/>github.com/Ancodi1<br/><br/><b>LinkedIn</b><br/>linkedin.com/in/ángel-collazo-díaz-4896742a9", M + 10 * mm, y, W - 2 * M - 20 * mm, "body")
p(c, "Este dossier contiene una selección autosuficiente del portfolio. Los enlaces se incluyen únicamente como referencia adicional.", M, 55 * mm, W - 2 * M, "small")
footer(c, 7); c.save()

print(OUT)

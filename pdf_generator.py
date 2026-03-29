from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
import io
import re

# ── Brand Colors ──
TEAL       = colors.HexColor("#00897B")
LIGHT_TEAL = colors.HexColor("#E0F2F1")
GOLD       = colors.HexColor("#FFB300")
DARK       = colors.HexColor("#212121")
GRAY       = colors.HexColor("#757575")

# ── Styles ──
def build_styles():
    title_style = ParagraphStyle(
        'CustomTitle',
        fontSize=28,
        textColor=colors.white,
        fontName='Helvetica-Bold',
        spaceAfter=6,
        alignment=1
    )
    subtitle_style = ParagraphStyle(
        'Subtitle',
        fontSize=13,
        textColor=GOLD,
        fontName='Helvetica',
        spaceAfter=4,
        alignment=1
    )
    section_style = ParagraphStyle(
        'Section',
        fontSize=16,
        textColor=TEAL,
        fontName='Helvetica-Bold',
        spaceBefore=16,
        spaceAfter=6
    )
    h2_style = ParagraphStyle(
        'H2',
        fontSize=13,
        textColor=DARK,
        fontName='Helvetica-Bold',
        spaceBefore=10,
        spaceAfter=4
    )
    h3_style = ParagraphStyle(
        'H3',
        fontSize=12,
        textColor=TEAL,
        fontName='Helvetica-Bold',
        spaceBefore=8,
        spaceAfter=4
    )
    day_title_style = ParagraphStyle(
        'DayTitle',
        fontSize=11,
        textColor=DARK,
        fontName='Helvetica-Bold',
        spaceBefore=6,
        spaceAfter=2
    )
    bullet_style = ParagraphStyle(
        'Bullet',
        fontSize=10,
        textColor=DARK,
        fontName='Helvetica',
        leftIndent=16,
        spaceAfter=3,
        leading=15
    )
    body_style = ParagraphStyle(
        'Body',
        fontSize=10,
        textColor=DARK,
        fontName='Helvetica',
        spaceAfter=6,
        leading=15
    )
    footer_style = ParagraphStyle(
        'Footer',
        fontSize=8,
        textColor=GRAY,
        fontName='Helvetica',
        alignment=1
    )
    return (
        title_style, subtitle_style, section_style,
        h2_style, h3_style, day_title_style,
        bullet_style, body_style, footer_style
    )


def parse_and_add_content(story, content, h2_style, h3_style, day_title_style, bullet_style, body_style):
    """Parse markdown-style text and add properly styled paragraphs to story."""

    for line in content.strip().split('\n'):
        line = line.strip()
        if not line:
            story.append(Spacer(1, 4))
            continue

        # H2 — ## Heading
        if line.startswith('## '):
            text = line.replace('## ', '').strip()
            text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
            story.append(Spacer(1, 10))
            story.append(Paragraph(text, h2_style))

        # H3 — ### Heading
        elif line.startswith('### '):
            text = line.replace('### ', '').strip()
            text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
            story.append(Spacer(1, 8))
            story.append(Paragraph(text, h3_style))

        # Bold-only lines — **Day 1: Title** (day titles)
        elif re.match(r'^[-•]?\s*\*\*[^*]+\*\*\s*$', line):
            text = re.sub(r'\*\*(.*?)\*\*', r'\1', line.lstrip('-•').strip())
            story.append(Paragraph(text, day_title_style))

        # Bullet lines — - text or • text
        elif line.startswith('-') or line.startswith('•'):
            text = line.lstrip('-•').strip()
            text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
            story.append(Paragraph(f"• {text}", bullet_style))

        # Normal body text
        else:
            text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
            story.append(Paragraph(text, body_style))


def generate_pdf(itinerary_output, food_output, budget_output, duration, budget_type):
    buffer = io.BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        topMargin=0.5 * inch,
        bottomMargin=0.75 * inch,
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch
    )

    (
        title_style, subtitle_style, section_style,
        h2_style, h3_style, day_title_style,
        bullet_style, body_style, footer_style
    ) = build_styles()

    story = []

    # ── Header Banner ──
    header_data = [[Paragraph("Vietnam Travel Plan", title_style)]]
    header_table = Table(header_data, colWidths=[7 * inch])
    header_table.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, -1), TEAL),
        ('TOPPADDING',    (0, 0), (-1, -1), 22),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 22),
        ('LEFTPADDING',   (0, 0), (-1, -1), 12),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 12),
    ]))
    story.append(header_table)

    # ── Info Strip ──
    info_data = [[
        Paragraph(f"Duration: {duration}", subtitle_style),
        Paragraph(f"Budget: {budget_type.title()}", subtitle_style),
    ]]
    info_table = Table(info_data, colWidths=[3.5 * inch, 3.5 * inch])
    info_table.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, -1), DARK),
        ('TOPPADDING',    (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('LEFTPADDING',   (0, 0), (-1, -1), 12),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 12),
    ]))
    story.append(info_table)
    story.append(Spacer(1, 24))

    def add_section(emoji, title, content):

        story.append(Paragraph(f"{emoji}  {title}", section_style))
        story.append(HRFlowable(
            width="100%", thickness=2,
            color=TEAL, spaceAfter=10
        ))
        # Parse and add content
        parse_and_add_content(
            story, content,
            h2_style, h3_style, day_title_style,
            bullet_style, body_style
        )
        story.append(Spacer(1, 16))

    # ── Three Sections ──
    add_section("🗺️",  "Your Itinerary",  str(itinerary_output))
    add_section("🍜",  "Food Guide",      str(food_output))
    add_section("💰",  "Budget Breakdown", str(budget_output))

    # ── Footer ──
    story.append(HRFlowable(width="100%", thickness=0.5, color=GRAY, spaceBefore=12))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "Generated by Vietnam Travel Agent • Powered by CrewAI &amp; Groq",
        footer_style
    ))

    doc.build(story)
    buffer.seek(0)
    return buffer
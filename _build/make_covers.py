"""Create branded 1200x675 WebP cover images for scheduled blog posts.

Run from the _build folder:  python make_covers.py
Only posts in _build/posts/*.py are processed. Existing covers are kept unless --force is given.
Needs Pillow (pip install pillow). Uses Windows fonts; edit FONT_DIR on other systems.
"""
import glob, html, io, os, re, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FONT_DIR = 'C:/Windows/Fonts/'
W, H = 1200, 675
NAVY, ORANGE = '#0b1533', '#ff6a00'


def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


def load_posts():
    """Execute the post files with tiny stand-ins for the helpers they use."""
    env = {'POSTS': [], 'EXTRA': {}}
    for n in ('P', 'ul', 'ol', 'table', 'tip', 'fig'):
        env[n] = lambda *a, **k: ''
    env['MID_CTA'] = ''
    for f in sorted(glob.glob(os.path.join(HERE, 'posts', '*.py'))):
        exec(io.open(f, encoding='utf-8').read(), env)
    return env['POSTS']


def plain(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s))


def wrap(draw, text, fnt, width):
    words, lines, line = text.split(), [], ''
    for w in words:
        test = (line + ' ' + w).strip()
        if draw.textlength(test, font=fnt) <= width:
            line = test
        else:
            lines.append(line)
            line = w
    if line:
        lines.append(line)
    return lines


def rounded(img, radius):
    mask = Image.new('L', img.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, img.size[0] - 1, img.size[1] - 1), radius, fill=255)
    return mask


def cover(p, out):
    im = Image.new('RGB', (W, H), NAVY)
    glow = Image.new('RGB', (W, H), NAVY)
    g = ImageDraw.Draw(glow)
    g.ellipse((760, -260, 1500, 420), fill='#7a3a10')
    g.ellipse((-320, 420, 420, 1060), fill='#1d2d6b')
    im = Image.blend(im, glow.filter(ImageFilter.GaussianBlur(130)), 1)
    d = ImageDraw.Draw(im)

    # device mock-up with a real portfolio screenshot
    slug = p.get('cover', 'ruvinara')
    shot = Image.open(os.path.join(ROOT, 'images/portfolio', f'{slug}-desktop.jpg')).convert('RGB').resize((500, 312))
    frame = Image.new('RGB', (518, 330), '#1f2a4d')
    frame.paste(shot, (9, 9))
    sh = Image.new('RGBA', (560, 372), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((20, 20, 540, 352), 18, fill=(0, 0, 0, 160))
    sh = sh.filter(ImageFilter.GaussianBlur(14))
    im.paste(sh, (642, 168), sh)
    im.paste(frame, (660, 182), rounded(frame, 16))
    phone = Image.open(os.path.join(ROOT, 'images/portfolio', f'{slug}-mobile.jpg')).convert('RGB').resize((132, 286))
    pf = Image.new('RGB', (146, 300), '#11182e')
    pf.paste(phone, (7, 7))
    im.paste(pf, (1012, 300), rounded(pf, 20))

    x = 64
    # category pill
    cat = plain(p['eyebrow']).upper()
    fp = font('seguisb.ttf', 20)
    tw = d.textlength(cat, font=fp)
    d.rounded_rectangle((x, 70, x + tw + 36, 112), 21, fill=ORANGE)
    d.text((x + 18, 91), cat, font=fp, fill='white', anchor='lm')

    # title, shrinking the font until it fits in five lines
    title = plain(p['title'])
    for size in (52, 48, 44, 40, 36):
        ft = font('segoeuib.ttf', size)
        lines = wrap(d, title, ft, 560)
        if len(lines) <= 5:
            break
    y = 140
    for ln in lines:
        d.text((x, y), ln, font=ft, fill='white')
        y += int(size * 1.22)

    # brand footer
    fb = font('segoeuib.ttf', 30)
    d.text((x, 585), 'Web', font=fb, fill='white')
    d.text((x + d.textlength('Web', font=fb), 585), 'Development', font=fb, fill=ORANGE)
    d.text((x + 2, 626), 'SRI LANKA  ·  webdevelopment.lk', font=font('seguisb.ttf', 17), fill='#9fb0d8')
    im.save(out, 'WEBP', quality=82, method=6)


if __name__ == '__main__':
    force = '--force' in sys.argv
    for p in load_posts():
        out = os.path.join(ROOT, 'images/blog', p['slug'] + '.webp')
        if os.path.exists(out) and not force:
            continue
        cover(p, out)
        print('cover', p['slug'])

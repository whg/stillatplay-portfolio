from markdown import markdown
from itertools import chain
from colorsys import hsv_to_rgb
import re

filename = "portfolio.md"
template = "template.html"
output = "index.html"

links = {
    'Pierre Chanquion': "https://twitter.com/p_chanq",
    'Marek Bereza': "http://mazbox.com",
    'EAVI': "http://eavi.goldsmithsdigital.com/",
    'Rebecca Fiebrink': "http://www.doc.gold.ac.uk/~mas01rf/Rebecca_Fiebrink_Goldsmiths/welcome.html",
    'Wekinator': "http://www.wekinator.org/",
    'Artisan': "http://artisan.co.uk",
    'United Visual Artists': "http://uva.co.uk",
    'd3': "http://www.d3technologies.com/",
    'Intel NUC': "http://www.intel.co.uk/content/www/uk/en/nuc/overview.html",
    'Poisson Surface Reconstruction': "https://www.cs.jhu.edu/~bolitho/Research/PoissonSurfaceReconstruction/",
    'Diederick Huijbers': "http://www.apollomedia.nl/",
    'Matt Watkins': "www.mattwatkinsdesign.com",
    'Hellicar & Lewis': "www.hellicarandlewis.com",
}

with open(filename) as f:
    data = f.read()

lines = data.split('\n')

tags = [line[2:] for line in lines if line.startswith("##")]

tags = [[t.strip() for t in tag.strip().split(",")] for tag in tags]

tags = set(chain(*tags))


for i, tag in enumerate(tags):
    r, g, b = hsv_to_rgb(float(i)/len(tags), 0.5, 0.9)

    s = '<span style="color: rgb(%d, %d, %d);">%s</span>' % (r*255, g*255, b*255, tag)
    # re.sub('##[^\n]*%s \n' % tag, data, s)
    data = data.replace(tag, '<span style="color: rgb(%d, %d, %d);">%s</span>' % (r*255, g*255, b*255, tag))


for term, link in links.items():
    data = data.replace(term, '[%s](%s)' % (term, link))
    
html = markdown(data)



t = open(template)
with open(output, 'w') as f:
    
    f.write(t.read().replace("<!-- data -->", html))

t.close()

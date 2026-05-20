# Gerar ícone SVG simples como base64 PNG
import base64

# SVG do ícone
svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512">
<rect width="512" height="512" rx="108" fill="#0a0f1a"/>
<rect x="30" y="30" width="452" height="452" rx="90" fill="#111827"/>
<text x="256" y="200" text-anchor="middle" font-size="140" fill="#10b981">🔋</text>
<text x="256" y="340" text-anchor="middle" font-family="Arial" font-weight="900" font-size="72" fill="#10b981">EX2</text>
<text x="256" y="410" text-anchor="middle" font-family="Arial" font-weight="700" font-size="36" fill="#64748b">GEELY</text>
</svg>'''

with open('/home/claude/geely-app/icon.svg', 'w') as f:
    f.write(svg)
print("SVG icon created")

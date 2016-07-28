display(Latex("""
The acceleration becomes
\\begin{align}
a(t) &= \\frac{d}{dt} v(t) = \\frac{d}{dt} l \\omega e_\\theta = \\frac{d}{dt} l \\omega \\begin{bmatrix} -\\sin\\theta \\\\ \\cos\\theta \\end{bmatrix} \\\\
     &= \\frac{d}{dt} \left( l \\ omega \\right) e_\\theta + l \\omega \\frac{d}{dt} \\begin{bmatrix} -\\sin\\theta \\\\ \\cos\\theta \\end{bmatrix} \\\\
     &= 0 + l \\omega^2 \\begin{bmatrix} -\\cos\\theta \\\\ -\\sin\\theta \\end{bmatrix} = - l \omega^2 e_r.  
\\end{align}
"""))
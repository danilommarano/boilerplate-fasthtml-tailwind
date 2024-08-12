from fasthtml.fastapp import * 

app, rt = fast_app(
    pico=False,
    hdrs=(
        Link(rel='stylesheet', href='styles/output.css', type='text/css'),
))

@app.get("/")
def home():
    return (
        Title("FastHTML + TailwindCSS"),
        Div( P("Let's do this!"), cls="bg-red-500 text-white")
    )

serve()
import simplekml
import pandas as pd
from pathlib import Path


input_file = "data/template_sites.xlsx"
output_file = "output/points.kml"

Path(output_file).parent.mkdir(parents=True, exist_ok=True)

df = pd.read_excel(input_file)

kml = simplekml.Kml()

for uf in df['UF'].unique():
    fol = kml.newfolder(name=uf)
    uf_df = df[df['UF'] == uf]

    for _, row in uf_df.iterrows():
        pnt = fol.newpoint(
            name=row['SITE ID'],
            coords=[(row['LONGITUDE_DECIMAL'], row['LATITUDE_DECIMAL'])]
        )
        pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'
        pnt.description = f"SITE: {row['SITE ID']}"
        pnt.style.iconstyle.color = 'ffff0000'
        pnt.snippet.maxlines = 1

kml.save(output_file)
print(f"KML de pontos salvo em: {output_file}")
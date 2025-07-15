import simplekml
import pandas as pd
from pathlib import Path


input_file = "data/template_links.xlsx"
output_file = "output/links.kml"


Path(output_file).parent.mkdir(parents=True, exist_ok=True)


df = pd.read_excel(input_file)
kml = simplekml.Kml()

for uf in df['UF'].unique():
    fol = kml.newfolder(name=uf)
    uf_df = df[df['UF'] == uf]
    sites = set()

    for _, row in uf_df.iterrows():
        for site_id, lat, lon in [
            (row['SITE ID A'], row['SITE A LAT'], row['SITE A LONG']),
            (row['SITE ID B'], row['SITE B LAT'], row['SITE B LONG']),
        ]:
            if site_id not in sites:
                pnt = fol.newpoint(name=site_id, coords=[(lon, lat)])
                pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'
                pnt.description = f"Latitude: {lat}\nLongitude: {lon}"
                sites.add(site_id)

        link = fol.newlinestring(
            name=f"{row['SITE ID A']} - {row['SITE ID B']}",
            coords=[
                (row['SITE A LONG'], row['SITE A LAT'], row['SITE A HEIGHT']),
                (row['SITE B LONG'], row['SITE B LAT'], row['SITE B HEIGHT']),
            ]
        )
        link.extrude = 1
        link.altitudemode = simplekml.AltitudeMode.relativetoground
        link.style.linestyle.width = 3
        link.style.linestyle.color = simplekml.Color.blue
        link.description = f"""
        {row['SITE ID A']}:
        Altura: {row['SITE A HEIGHT']} m

        {row['SITE ID B']}:
        Altura: {row['SITE B HEIGHT']} m
        """

kml.save(output_file)
print(f"KML de links salvo em: {output_file}")
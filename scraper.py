from dc_base_scrapers.xml_scraper import GmlScraper


stations_url = "http://www2.guildford.gov.uk/ishare5.2.web/getows.ashx?service=WFS&version=1.1.0&request=GetFeature&typeName=polling_places&mapsource=GBC/Inspire"
stations_fields = {
    '{http://mapserver.gis.umn.edu/mapserver}ogc_fid': 'ogc_fid',
    '{http://mapserver.gis.umn.edu/mapserver}pollingdistrict': 'pollingdistrict',
    '{http://mapserver.gis.umn.edu/mapserver}thoroughfare_name': 'thoroughfare_name',
    '{http://mapserver.gis.umn.edu/mapserver}northing': 'northing',
    '{http://mapserver.gis.umn.edu/mapserver}pai_update_status': 'pai_update_status',
    '{http://mapserver.gis.umn.edu/mapserver}pollingplace': 'pollingplace',
    '{http://mapserver.gis.umn.edu/mapserver}easting': 'easting',
    '{http://mapserver.gis.umn.edu/mapserver}register': 'register',
    '{http://mapserver.gis.umn.edu/mapserver}copyright': 'copyright',
    '{http://mapserver.gis.umn.edu/mapserver}mi_prinx': 'mi_prinx',
    '{http://mapserver.gis.umn.edu/mapserver}datatablename': 'datatablename',
    '{http://mapserver.gis.umn.edu/mapserver}datasource': 'datasource',
}

districts_url = "http://www2.guildford.gov.uk/ishare5.2.web/getows.ashx?service=WFS&version=1.1.0&request=GetFeature&typeName=polling_districts&mapsource=GBC/Inspire"
districts_fields = {
    '{http://mapserver.gis.umn.edu/mapserver}ogc_fid': 'ogc_fid',
    '{http://mapserver.gis.umn.edu/mapserver}borough_ward': 'borough_ward',
    '{http://mapserver.gis.umn.edu/mapserver}datatablename': 'datatablename',
    '{http://mapserver.gis.umn.edu/mapserver}constituency': 'constituency',
    '{http://mapserver.gis.umn.edu/mapserver}pai_update_status': 'pai_update_status',
    '{http://mapserver.gis.umn.edu/mapserver}pollingdistrictname': 'pollingdistrictname',
    '{http://mapserver.gis.umn.edu/mapserver}areahectares': 'areahectares',
    '{http://mapserver.gis.umn.edu/mapserver}parish': 'parish',
    '{http://mapserver.gis.umn.edu/mapserver}register': 'register',
    '{http://mapserver.gis.umn.edu/mapserver}county_division': 'county_division',
    '{http://mapserver.gis.umn.edu/mapserver}mi_prinx': 'mi_prinx',
    '{http://mapserver.gis.umn.edu/mapserver}copyright': 'copyright',
}

council_id = 'E07000209'


stations_scraper = GmlScraper(stations_url, council_id, 'stations', stations_fields, 'ogc_fid')
stations_scraper.scrape()
districts_scraper = GmlScraper(districts_url, council_id, 'districts', districts_fields, 'ogc_fid')
districts_scraper.scrape()

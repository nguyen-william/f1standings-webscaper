# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class F1StandingsPipeline:
    
    def process_item(self, item, spider):
        return item
        '''
        self.items = []
        self.race_order = [
            "FORMULA 1 GULF AIR BAHRAIN GRAND PRIX 2023",
            "FORMULA 1 STC SAUDI ARABIAN GRAND PRIX 2023",
            "FORMULA 1 ROLEX AUSTRALIAN GRAND PRIX 2023",
            "FORMULA 1 AZERBAIJAN GRAND PRIX 2023",
            "FORMULA 1 CRYPTO.COM MIAMI GRAND PRIX 2023",
            "FORMULA 1 GRAND PRIX DE MONACO 2023",
            "FORMULA 1 AWS GRAN PREMIO DE ESPAÑA 2023",
            "FORMULA 1 PIRELLI GRAND PRIX DU CANADA 2023",
            "FORMULA 1 ROLEX GROSSER PREIS VON ÖSTERREICH 2023",
            "FORMULA 1 ARAMCO BRITISH GRAND PRIX 2023",
            "FORMULA 1 QATAR AIRWAYS HUNGARIAN GRAND PRIX 2023",
            "FORMULA 1 MSC CRUISES BELGIAN GRAND PRIX 2023",
            "FORMULA 1 HEINEKEN DUTCH GRAND PRIX 2023",
            "FORMULA 1 PIRELLI GRAN PREMIO D’ITALIA 2023",
            "FORMULA 1 SINGAPORE AIRLINES SINGAPORE GRAND PRIX 2023",
            "FORMULA 1 LENOVO JAPANESE GRAND PRIX 2023",
            "FORMULA 1 QATAR AIRWAYS QATAR GRAND PRIX 2023",
            "FORMULA 1 LENOVO UNITED STATES GRAND PRIX 2023",
            "FORMULA 1 GRAN PREMIO DE LA CIUDAD DE MÉXICO 2023",
            "FORMULA 1 ROLEX GRANDE PRÊMIO DE SÃO PAULO 2023",
            "FORMULA 1 HEINEKEN SILVER LAS VEGAS GRAND PRIX 2023",
            "FORMULA 1 ETIHAD AIRWAYS ABU DHABI GRAND PRIX 2023"
        ]

    def process_item(self, item, spider):
        self.items.append(item)
        return item

    def close_spider(self, spider):
        # Sort items by predefined race order
        race_order_index = {race_name: index for index, race_name in enumerate(self.race_order)}
        self.items.sort(key=lambda x: race_order_index.get(x['race_name'], float('inf')))
        # Further processing can be done here
        for item in self.items:
            print(f'{item["race_name"]}: {item["racer_name"]} - {item["position"]}')
        return item
        '''

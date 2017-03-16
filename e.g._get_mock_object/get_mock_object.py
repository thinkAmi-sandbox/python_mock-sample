from cook import Cook

class Target:
    def run(self, material):
        # 引数materialは作るのに手間がかかるオブジェクト
        cook = Cook(material)
        cuisine = cook.bake()
        return {
            'name': 'maindish',
            'cuisine': cuisine.get_name(),
        }

from cuisine import Ham, Spam, Egg

class Cook:
    def __init__(self, material):
        self.__material = material

    def bake(self):
        try:
            # 実際には、materialの中身によって複雑な処理がある
            if material:
                return Ham()
            else:
                return Spam()
        except:
            # なかなかEggを出すデータを作れないとする
            return Egg()

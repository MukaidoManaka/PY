class Movies:
    def __init__(self,title,description,poster_url,trailer_url):    #self类似js中的this
        self.title = title
        self.description = description
        self.poster_url = poster_url
        self.trailer_url = trailer_url
    def show_description(self):
        print('Description————————','“' + self.description + '”')
   
m = Movies("乐透7","你的梦想是钱能买到的吗","url_1","url_2");   #实例化时，参数必须拉满
m.show_description()
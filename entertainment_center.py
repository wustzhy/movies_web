import fresh_tomatoes
import media


thunder_again = media.Movie('Pacific Thunder Again',
                            'The story takes place in 2035, ten years after the war ended',
                            'https://imgsrc.baidu.com/baike/pic/item/a71ea8d3fd1f413441bfe252291f95cad1c85e16.jpg',
                            'http://v.youku.com/v_show/id_XMzM4NjQxMjk0OA==.html?spm=a2h0j.11185381.Dramalist_wrap.5~5~5!3~A&s=d881989cfda611e3b2ad')

shape_of_water = media.Movie('The Shape of Water',
                             'A fantasy drama produced by the American company foss searchlight',
                             'https://imgsrc.baidu.com/baike/pic/item/f636afc379310a5564f6fcc6bb4543a982261035.jpg',
                             'http://v.youku.com/v_show/id_XMzQzMzM3MDc0NA==.html')

first_rate_player = media.Movie('No.1 Player',
                                'the story of the return of the king, Spielberg',
                                'http://image.thepaper.cn/wap/image/6/931/357.jpg',
                                'http://v.youku.com/v_show/id_XMzQzMTg3MjU5Ng==.html')

fresh_tomatoes.open_movies_page([thunder_again, shape_of_water, first_rate_player])

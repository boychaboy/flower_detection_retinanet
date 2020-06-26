

def get_kor_name(eng):
    eng_list = ['waterLily','rose','sunflower','lotus','carnation','daffodill','magnolia','camellia','dandelion','daisy']
    kor_list = ['수련','장미','해바라기','연꽃','카네이션','수선화','목련','동백','민들레','데이지']
    index = eng_list.index(eng)
    return kor_list[index]

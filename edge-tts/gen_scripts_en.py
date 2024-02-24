import numpy as np
import os

file_path = __file__
base_path = os.path.dirname(os.path.abspath(__file__))

speaker2path = {'zh-CN-YunyangNeural':'yunyang', 'zh-CN-XiaoxiaoNeural':'xiaoxiao'}

def get_mp3(speaker, mode='wav'):
    sen_list = []
    files = os.listdir('./en')
    audio_path = base_path + "/" + mode + "/"  + speaker2path[speaker] + "/en/" 

    if not os.path.exists(audio_path):
        print(audio_path)
        os.makedirs(audio_path)

    for file in files:
        if file not in ['.ipynb_checkpoints']:
            file_name = file.split('.')[0]
            file_path = os.path.join('./en', file)
            print(file_path)
            with open(file_path, "r", encoding='utf-8') as f:  #打开文本
                data = f.read()   #读取文本
                data = data.replace('\n', '').replace('\'','').strip()
                # print(data)
            sentence = data.split(".")[:-1]
            
            '''
                !!! 根据实际情况修改生成文件的目录
            '''
            for i, sen in enumerate(sentence):
                # print(sen, i)
                if i < 10:
                    step = "0" + str(i)
                else:
                    step = str(i)
                sen_list.append("edge-tts --voice " + speaker + " --text '" 
                + sen 
                +  "。' --write-media " 
                + "../" + mode + "/"  + speaker2path[speaker] + "/en/" 
                + file_name + "_" + step + "_" + speaker2path[speaker] +  "." + mode)

    return sen_list

def list2file(ls):
    with open(base_path + '/scripts/batch_tts.sh', 'w', encoding='utf-8') as f:
        for item in ls:
            f.write(str(item) + '\n') 



if __name__ == "__main__":
    # 生成命令
    # yunyang = get_mp3('zh-CN-YunyangNeural', 'wav')
    xiaoxiao = get_mp3('zh-CN-XiaoxiaoNeural', 'wav')

    # 将命令写入文件
    all_mp3 =  xiaoxiao
    list2file(all_mp3)






import os
import random
import pprint
import math
import shutil
import glob
import os.path

os.chdir('C:\\Project')

if not os.path.exists(os.path.join(os.getcwd(), 'merged output','train')):
    os.makedirs(os.path.join(os.getcwd(), 'merged output','train'))
if not os.path.exists(os.path.join(os.getcwd(),'merged output','remain')):
    os.makedirs(os.path.join(os.getcwd(),'merged output','remain'))

def merge(name,add,n,m):
    j = name + '.txt'
    for y in os.listdir(add) :
          if j == y:
              return
    if(name != 'validate'):
       q=int(n)
       for root, dirs, files in os.walk(os.path.join('C:\\Project','cs223_project','ADFA-LD and Weka KDD','ADFA-LD','ADFA-LD')):
             for d in dirs:
                 if(q == int(m)+1):
                     return
                 if(name!='training'):
                    k = name + '_' + str(q)
                 else:
                     k= name
                 if(m == '10'):
                     k1 = name + '_8'
                     k2 = name + '_9'
                     k3 = name + '_10'
                     if( (k1.upper() in str(d.upper())) or (k2.upper() in str(d.upper())) or (k3.upper() in str(d.upper()))):
                        for x in os.listdir(os.path.join(root,d)):
                            with open(os.path.join(add,j), 'a+') as outfile:
                                 with open((os.path.join(root,d,x))) as infile:
                                     shutil.copyfileobj(infile, outfile)
                                     outfile.write('-1 ')
                        if (name == 'training'):
                            return
                        q= q+1
                 else:
                     if k.upper() in str(d.upper()):
                         for x in os.listdir(os.path.join(root, d)):
                             with open(os.path.join(add, j), 'a+') as outfile:
                                 with open((os.path.join(root, d, x))) as infile:
                                     shutil.copyfileobj(infile, outfile)
                                     outfile.write('-1 ')
                         if (name == 'training'):
                             return
                         q = q + 1
    else:
       for root, dirs, files in os.walk(os.path.join('C:\\Project', 'cs223_project', 'ADFA-LD and Weka KDD', 'ADFA-LD', 'ADFA-LD','Validation_Data_Master')):
            for x in os.listdir(root):
                with open(os.path.join(add, j), 'a+') as outfile:
                    with open((os.path.join(root, x))) as infile:
                        shutil.copyfileobj(infile, outfile)
                        outfile.write('-1 ')
def generate_data(label):
    if label.endswith('.txt'):
        wr = label[:-4]
    for root, dirs, files in os.walk(os.path.join('C:\\Project','merged output')):
        for file in files:
            if(label == file):
                with open(os.path.join(root, file), "r") as auto:
                    num = auto.read().split()
                    i = 0
                    with open(os.path.join('C:\\Project','output.txt'), 'a+') as outfile:
                       while(i != len(num)):
                            temp={}
                            while(num[i+n-1]!= '-1'):
                                name = ''
                                for j in range(n - 1):
                                    name += str(num[i + j]) + ' '
                                name += str(num[i + n - 1])
                                temp.setdefault(name,0)
                                temp[name]+=1
                                i=i+1
                            i = i + n
                            a=0
                            for a in range(len(top_30_list)):
                                for b in top_30_list[a] :
                                    if b not in temp:
                                        outfile.write('0 ')
                                    else:
                                        outfile.write(str(temp[b]))
                                        outfile.write(' ')
                            outfile.write(wr.upper() + '\n')
                            #print(label)
                            temp.clear()


merge('adduser',os.path.join('C:\\Project','merged output','train'),'1','7')
merge('hydra_ftp',os.path.join('C:\\Project','merged output','train'),'1','7')
merge('hydra_ssh',os.path.join('C:\\Project','merged output','train'),'1','7')
merge('java_meterpreter',os.path.join('C:\\Project','merged output','train'),'1','7')
merge('meterpreter',os.path.join('C:\\Project','merged output','train'),'1','7')
merge('web_shell',os.path.join('C:\\Project','merged output','train'),'1','7')
merge('training',os.path.join('C:\\Project','merged output','train'),'1','1')

print("Enter input : ")
os.chdir(os.path.join(os.getcwd(),'merged output','train'))
n = input()
n = int(n)

try:
    os.remove(os.path.join('C:\\Project', 'output.txt'))
except OSError:
    pass
list_glob=[]

for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith(".txt"):
            with open(os.path.join(os.getcwd(), file), "r") as auto:
                num = auto.read().split()
                gram_local={}
                for i in range(len(num) - (n - 1)):
                    name = ''
                    for j in range(n - 1):
                        name += str(num[i + j]) + ' '
                    name += str(num[i + n - 1])
                    if str(-1) in name :
                        continue
                    else:
                        gram_local.setdefault(name, 0)
                        gram_local[name] += 1
                list_glob.append(gram_local.copy())
final=[]
top_30_list=[]
check={}
for j in range(len(list_glob)):
    top_30=[]
    k=math.ceil(len(list_glob[j])*(0.3))
    final=list(zip(list_glob[j].values(),list_glob[j].keys()))
    final.sort()
    q = len(final)
    for i in range(k):
        if(final[q-i-1][1] not in check):
            check[final[q-i-1][1]]=1
            top_30+=[final[q-i-1][1]]
    top_30_list.append(top_30.copy())
    final.clear()

i=0
abcd = 'feature' + str(n) + '.txt'
if not os.path.isfile(os.path.join('C:\\Project', abcd)):
    for i in range(len(top_30_list)):
        with open(os.path.join('C:\\Project', abcd), 'a+') as outfile:
            for item in top_30_list[i]:
                outfile.write("%s\n" % item)

merge('adduser',os.path.join('C:\\Project','merged output','remain'),'8','10')
merge('hydra_ftp',os.path.join('C:\\Project','merged output','remain'),'8','10')
merge('hydra_ssh',os.path.join('C:\\Project','merged output','remain'),'8','10')
merge('java_meterpreter',os.path.join('C:\\Project','merged output','remain'),'8','10')
merge('meterpreter',os.path.join('C:\\Project','merged output','remain'),'8','10')
merge('web_shell',os.path.join('C:\\Project','merged output','remain'),'8','10')
merge('validate',os.path.join('C:\\Project','merged output','remain'),'8','10')

generate_data('adduser.txt')
generate_data('hydra_ftp.txt')
generate_data('hydra_ssh.txt')
generate_data('java_meterpreter.txt')
generate_data('meterpreter.txt')
generate_data('web_shell.txt')
generate_data('training.txt')
generate_data('validate.txt')






